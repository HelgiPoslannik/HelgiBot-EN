from fastapi import FastAPI, Request
from telegram import Update, LabeledPrice
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    PreCheckoutQueryHandler,
    ContextTypes,
    filters
)
from app.config import BOT_TOKEN
from app.coze_service import ask_coze
from app.logger import logger
from app.locales import (
    MESSAGES,
    FREE_MESSAGE_LIMIT,
    STARS_PACK_PRICE,
    REQUESTS_PER_PACK
)

app = FastAPI()

telegram_app = (
    Application
    .builder()
    .token(BOT_TOKEN)
    .build()
)

TELEGRAM_MAX_LENGTH = 4000
PACK_PAYLOAD = "requests_pack_20"

USER_FREE_USED = {}
USER_PAID_BALANCE = {}

# Кэш для автоматических переводов на редкие языки мира
DYNAMIC_TRANSLATIONS_CACHE = {}


def get_user_lang_code(update: Update) -> str:
    """Извлекает 2-буквенный код языка из интерфейса пользователя (например, 'kk', 'ja', 'es')."""
    user = update.effective_user
    if user and user.language_code:
        return user.language_code.split("-")[0].lower()
    return "en"


def get_messages_for_user(update: Update) -> dict:
    """
    1. Ищет язык в заранее подготовленном словаре MESSAGES (14 языков).
    2. Если нет — ищет в кэше DYNAMIC_TRANSLATIONS_CACHE.
    3. Если заходит редкий язык — на лету переводит через ИИ и закэширует.
    """
    lang = get_user_lang_code(update)

    # 1. Готовые популярные языки (мгновенный ответ)
    if lang in MESSAGES:
        return MESSAGES[lang]

    # 2. Ужe переводившиеся редкие языки (из кэша)
    if lang in DYNAMIC_TRANSLATIONS_CACHE:
        return DYNAMIC_TRANSLATIONS_CACHE[lang]

    # 3. Редкий язык — автоперевод ИИ в реальном времени
    try:
        user_id = update.effective_user.id
        prompt = (
            f"Translate the following Telegram bot welcome message precisely into the language code '{lang}'. "
            f"Keep emojis, formatting, and structural list.\n\n"
            f"Message:\n{MESSAGES['en']['welcome']}"
        )
        translated_welcome = ask_coze(user_id=user_id, message=prompt)

        translated_dict = {
            "welcome": translated_welcome,
            "limit_reached": MESSAGES["en"]["limit_reached"],
            "invoice_title": MESSAGES["en"]["invoice_title"],
            "invoice_desc": MESSAGES["en"]["invoice_desc"],
            "invoice_label": MESSAGES["en"]["invoice_label"],
            "payment_success": MESSAGES["en"]["payment_success"]
        }
        DYNAMIC_TRANSLATIONS_CACHE[lang] = translated_dict
        return translated_dict
    except Exception as e:
        logger.error(f"Error during dynamic translation for lang {lang}: {e}")
        return MESSAGES["en"]


async def send_long_message(message, text: str):
    if len(text) <= TELEGRAM_MAX_LENGTH:
        await message.reply_text(text)
        return
    chunks = []
    current = ""
    for paragraph in text.split("\n"):
        candidate = f"{current}\n{paragraph}" if current else paragraph
        if len(candidate) > TELEGRAM_MAX_LENGTH:
            if current:
                chunks.append(current)
            current = paragraph
        else:
            current = candidate
    if current:
        chunks.append(current)
    for chunk in chunks:
        await message.reply_text(chunk)


async def send_pack_invoice(chat_id: int, context: ContextTypes.DEFAULT_TYPE, texts: dict):
    await context.bot.send_invoice(
        chat_id=chat_id,
        title=texts["invoice_title"],
        description=texts["invoice_desc"],
        payload=PACK_PAYLOAD,
        provider_token="",  # Для Telegram Stars
        currency="XTR",
        prices=[LabeledPrice(label=texts["invoice_label"], amount=STARS_PACK_PRICE)]
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = get_messages_for_user(update)
    await update.message.reply_text(texts["welcome"], parse_mode="Markdown")


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)


async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id_str = str(user.id)
    payment = update.message.successful_payment
    texts = get_messages_for_user(update)

    if payment.invoice_payload == PACK_PAYLOAD:
        USER_PAID_BALANCE[user_id_str] = USER_PAID_BALANCE.get(user_id_str, 0) + REQUESTS_PER_PACK
        logger.info(f"User {user_id_str} bought a pack. New balance: {USER_PAID_BALANCE[user_id_str]}")
        await update.message.reply_text(texts["payment_success"])


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    user_id_str = str(user.id)
    texts = get_messages_for_user(update)

    free_used = USER_FREE_USED.get(user_id_str, 0)
    paid_balance = USER_PAID_BALANCE.get(user_id_str, 0)

    if free_used < FREE_MESSAGE_LIMIT:
        USER_FREE_USED[user_id_str] = free_used + 1
    elif paid_balance > 0:
        USER_PAID_BALANCE[user_id_str] = paid_balance - 1
    else:
        await update.message.reply_text(texts["limit_reached"])
        await send_pack_invoice(update.effective_chat.id, context, texts)
        return

    logger.info(f"User {user.id} [{get_user_lang_code(update)}]: {text}")
    answer = ask_coze(user_id=user.id, message=text)
    await send_long_message(update.message, answer)


telegram_app.add_handler(CommandHandler("start", start_command))
telegram_app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
telegram_app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


@app.on_event("startup")
async def startup():
    await telegram_app.initialize()
    await telegram_app.start()
    await telegram_app.updater.start_polling(drop_pending_updates=True)
    logger.info("Standalone AI bot started with multi-language support")


@app.on_event("shutdown")
async def shutdown():
    if telegram_app.updater:
        await telegram_app.updater.stop()
    await telegram_app.stop()
    await telegram_app.shutdown()


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}


@app.get("/")
async def home():
    return {"status": "Standalone AI bot is running"}
