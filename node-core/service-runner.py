# node-core/service-runner.py

import os
import time
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging agar tetap terlihat sistemik
logging.basicConfig(
    format='[SYS] %(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("TG_BOT_TOKEN")
OWNER_ID = os.getenv("BOT_OWNER_ID")

if not TOKEN:
    raise EnvironmentError("Token not found in environment variable: TG_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot aktif dan berjalan pada sistem daemon.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Sistem telemetry berjalan stabil.")

if __name__ == "__main__":
    logging.info("Starting background telemetry service daemon...")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    asyncio.run(app.run_polling())
