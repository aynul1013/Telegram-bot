from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

ADMIN_ID = 5879673745  # এখানে আপনার Telegram ID দিন
BOT_TOKEN = "7512343478:AAHSFlr5DzJ1FgffKhAsyokDXbF-e_9gaLU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 স্বাগতম!\n\n📸 অনুগ্রহ করে আপনি যে এড দেখেছেন তার Screenshot পাঠান।"
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    caption = f"📥 New Screenshot\n👤 User: @{update.message.from_user.username}"

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption=caption
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

print("🤖 Bot is running...")
app.run_polling()