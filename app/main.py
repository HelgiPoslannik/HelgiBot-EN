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

app = FastAPI()

telegram_app = (
    Application
    .builder()
    .token(BOT_TOKEN)
    .build()
)

TELEGRAM_MAX_LENGTH = 4000

FREE_MESSAGE_LIMIT = 4
STARS_PACK_PRICE = 500          # цена пакета в Stars — подберите под себя
REQUESTS_PER_PACK = 20         # сколько запросов даёт один пакет
PACK_PAYLOAD = "requests_pack_20"

# Всё в оперативной памяти — при перезапуске Railway обнулится.
# Для боевого режима с реальными деньгами стоит перенести в Redis как можно скорее.
USER_FREE_USED = {}
USER_PAID_BALANCE = {}


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


async def send_pack_invoice(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_invoice(
        chat_id=chat_id,
        title=f"{REQUESTS_PER_PACK} запросов к ИИ-ассистенту",
        description=(
            f"Пакет из {REQUESTS_PER_PACK} дополнительных запросов "
            "к ИИ-ассистенту по психосоматике."
        ),
        payload=PACK_PAYLOAD,
        provider_token="",  # пусто — обязательно для Stars
        currency="XTR",
        prices=[LabeledPrice(label=f"{REQUESTS_PER_PACK} запросов", amount=STARS_PACK_PRICE)]
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я твой ИИ-ассистент по психосоматике.\n\n"
        f"Первые {FREE_MESSAGE_LIMIT} вопросов — бесплатно. "
        f"Дальше — пакеты по {REQUESTS_PER_PACK} запросов за {STARS_PACK_PRICE} ⭐️.\n\n"
        "Просто напиши, что тебя беспокоит."
    )


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    # Цифровой товар, ограничений по наличию нет — подтверждаем всегда
    await query.answer(ok=True)


async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id_str = str(user.id)
    payment = update.message.successful_payment

    if payment.invoice_payload == PACK_PAYLOAD:
        USER_PAID_BALANCE[user_id_str] = USER_PAID_BALANCE.get(user_id_str, 0) + REQUESTS_PER_PACK
        logger.info(f"User {user_id_str} bought a pack. New balance: {USER_PAID_BALANCE[user_id_str]}")
        await update.message.reply_text(
            f"Оплата получена! Начислено {REQUESTS_PER_PACK} запросов. "
            "Можешь продолжать 🙌"
        )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    user_id_str = str(user.id)

    free_used = USER_FREE_USED.get(user_id_str, 0)
    paid_balance = USER_PAID_BALANCE.get(user_id_str, 0)

    if free_used < FREE_MESSAGE_LIMIT:
        USER_FREE_USED[user_id_str] = free_used + 1
    elif paid_balance > 0:
        USER_PAID_BALANCE[user_id_str] = paid_balance - 1
    else:
        await update.message.reply_text(
            "Бесплатные и оплаченные запросы закончились. "
            "Вот пакет, чтобы продолжить:"
        )
        await send_pack_invoice(update.effective_chat.id, context)
        return

    logger.info(f"User {user.id}: {text}")
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
    logger.info("Standalone AI bot started")


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
