from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

# خواندن توکن از فایل config.txt
def load_token():
    with open("config.txt", "r") as f:
        line = f.readline().strip()
        return line.split("=")[1]

TOKEN = load_token()

# تابعی که وقتی کاربر پیام می‌دهد اجرا می‌شود
def handle_message(update, context):
    user_text = update.message.text
    update.message.reply_text(f"پیامت رسید: {user_text}")

# شروع ربات
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # هر پیام متنی → تابع handle_message اجرا شود
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
