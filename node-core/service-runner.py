import os
import time
import json
import logging
import asyncio
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
TOKEN = os.getenv("TG_BOT_TOKEN")
OWNER_ID = os.getenv("BOT_OWNER_ID")

logging.basicConfig(format='[SYS] %(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()
    if user_id not in data:
        data[user_id] = {
            "balance": 0,
            "referrals": [],
            "last_claim": None
        }
        if context.args:
            referrer = context.args[0]
            if referrer != user_id and referrer in data:
                if user_id not in data[referrer]["referrals"]:
                    data[referrer]["referrals"].append(user_id)
                    data[referrer]["balance"] += 10  # reward referral
        save_data(data)
    await update.message.reply_text("🤖 Selamat datang! Gunakan /claim untuk klaim harian atau /me untuk cek saldo.")

async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()
    now = datetime.utcnow()

    if user_id not in data:
        await update.message.reply_text("⚠️ Anda belum terdaftar. Gunakan /start terlebih dahulu.")
        return

    last_claim = data[user_id].get("last_claim")
    if last_claim:
        last_time = datetime.strptime(last_claim, "%Y-%m-%d")
        if now.date() <= last_time.date():
            await update.message.reply_text("⏳ Anda sudah klaim hari ini. Coba lagi besok.")
            return

    data[user_id]["balance"] += 5
    data[user_id]["last_claim"] = now.strftime("%Y-%m-%d")
    save_data(data)
    await update.message.reply_text("✅ Klaim berhasil! +5 poin 🎁")

async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()

    if user_id not in data:
        await update.message.reply_text("⚠️ Anda belum terdaftar. Gunakan /start terlebih dahulu.")
        return

    bal = data[user_id]["balance"]
    await update.message.reply_text(f"💼 Saldo Anda: {bal} poin")

async def referrals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()

    if user_id not in data:
        await update.message.reply_text("⚠️ Anda belum terdaftar. Gunakan /start terlebih dahulu.")
        return

    refs = data[user_id].get("referrals", [])
    if refs:
        msg = f"🔗 Anda telah mereferensikan {len(refs)} pengguna:\n\n" + "\n".join([f"• {r}" for r in refs])
    else:
        msg = "❌ Belum ada referral aktif."
    await update.message.reply_text(msg)

if __name__ == "__main__":
    if not TOKEN:
        raise EnvironmentError("Missing environment variable: TG_BOT_TOKEN")

    logging.info("Starting bot in stealth mode...")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("claim", claim))
    app.add_handler(CommandHandler("me", me))
    app.add_handler(CommandHandler("referrals", referrals))

    asyncio.run(app.run_polling())
