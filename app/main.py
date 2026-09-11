from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from app.config import BOT_TOKEN
from app.subscription import check_subscription
from app.coze_service import ask_coze
from app.logger import logger

app = FastAPI()

telegram_app = (
    Application
    .builder()
    .token(BOT_TOKEN)
    .build()
)

TELEGRAM_MAX_LENGTH = 4000  # с небольшим запасом от лимита Telegram в 4096

FREE_MESSAGE_LIMIT = 5
# Счётчик бесплатных сообщений в оперативной памяти (user_id -> количество использованных).
# При перезапуске сервера на Railway счётчик обнулится — как и память диалогов.
USER_FREE_MESSAGES = {}

SUBSCRIBE_MESSAGE = """🛑 *Бесплатные вопросы закончились*

Чтобы продолжить пользоваться ИИ-ассистентом без ограничений, оформи подписку в закрытый клуб:

- Первый месяц — 9 €
- Далее — 11 €/месяц
- Год — 120 €

С подпиской у тебя будет:
— безлимитный доступ к ИИ-ассистенту
— обучение эмоциональному интеллекту и психосоматике
— доступ к закрытым эфирам
— полная база по болезням и эмоциям

👉 [Оформить подписку](https://t.me/tribute/app?startapp=s11Qp)"""


async def send_long_message(message, text: str):
    """
    Отправляет длинный текст, разбивая его на несколько сообщений,
    если он превышает лимит Telegram на длину одного сообщения.
    """
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


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if await check_subscription(user.id):
        await update.message.reply_text(
            "✅ Доступ подтверждён.\n"
            "Задавай свой вопрос."
        )
    else:
        await update.message.reply_text(
            "Привет! Я твой ИИ-ассистент по психосоматике.\n\n"
            f"У тебя есть {FREE_MESSAGE_LIMIT} бесплатных вопросов — можешь сразу "
            "написать, что тебя беспокоит."
        )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    user_id_str = str(user.id)

    is_subscribed = await check_subscription(user.id)

    if not is_subscribed:
        used = USER_FREE_MESSAGES.get(user_id_str, 0)
        if used >= FREE_MESSAGE_LIMIT:
            await update.message.reply_text(
                SUBSCRIBE_MESSAGE,
                parse_mode="Markdown"
            )
            return
        USER_FREE_MESSAGES[user_id_str] = used + 1

    logger.info(
        f"User {user.id}: {text}"
    )

    answer = ask_coze(
        user_id=user.id,
        message=text
    )

    await send_long_message(update.message, answer)


telegram_app.add_handler(
    CommandHandler(
        "start",
        start_command
    )
)
telegram_app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)


@app.on_event("startup")
async def startup():
    await telegram_app.initialize()
    await telegram_app.start()
    await telegram_app.updater.start_polling(
        drop_pending_updates=True
    )
    logger.info("Telegram bot started")


@app.on_event("shutdown")
async def shutdown():
    if telegram_app.updater:
        await telegram_app.updater.stop()
    await telegram_app.stop()
    await telegram_app.shutdown()


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(
        data,
        telegram_app.bot
    )
    await telegram_app.process_update(update)
    return {
        "ok": True
    }


@app.get("/")
async def home():
    return {
        "status": "Helgi AI Bot is running"
    }
