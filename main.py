from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from agent import handle_message

TOKEN = "8290825217:AAHfZHzGzxRgXZEJfYgdTifVl7FdacW6X-A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ایجنت رمز ارز آنلاین شد!")

async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = handle_message(user_text)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, router))

    app.run_polling()

if __name__ == "__main__":
    main()
