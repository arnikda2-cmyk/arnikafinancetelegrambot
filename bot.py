
import os
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from poster import make_demo_poster

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "آرنیکا فایننس آماده است.\n\n"
        "برای تست بنویس:\n"
        "طلای ۱۸\n\n"
        "نسخه آزمایشی فعلاً پوستر نمونه را با قالب ۱۲ کادر تولید می‌کند."
    )

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    if "طلای ۱۸" in text or text in ("طلا", "gold"):
        out = make_demo_poster()
        with open(out, "rb") as f:
            await update.message.reply_document(
                document=f,
                caption="پوستر آزمایشی آرنیکا فایننس — ۱۲ کادر"
            )
    else:
        await update.message.reply_text(
            "برای تست فعلی بنویس: «طلای ۱۸»"
        )

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN تنظیم نشده است.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
