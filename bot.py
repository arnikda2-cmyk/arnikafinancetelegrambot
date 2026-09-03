import os
import logging
from pathlib import Path

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from poster import make_demo_poster

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get("PORT", "10000"))
RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL", "").rstrip("/")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

if not RENDER_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL is not available")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "ربات آرنیکا فایننس آماده است.\n\n"
        "برای تست عبارت «طلای ۱۸» را بفرست."
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip().lower()

    if "طلای ۱۸" in text or "طلا" in text or "gold" in text:
        poster_path = make_demo_poster()

        with open(poster_path, "rb") as f:
            await update.message.reply_document(
                document=f,
                filename=Path(poster_path).name,
                caption="پوستر آزمایشی آرنیکا فایننس"
            )
    else:
        await update.message.reply_text(
            "برای تست، عبارت «طلای ۱۸» را بفرست."
        )


def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )

    webhook_url = f"{RENDER_URL}/telegram"

    logger.info("Starting webhook on port %s", PORT)

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="telegram",
        webhook_url=webhook_url,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
