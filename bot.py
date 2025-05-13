import telegram
from telegram.ext import Updater, CommandHandler

# Substitua pelo seu token do bot
TOKEN = "7764227131:AAGflLcQQlh7XtkjJuvKGXiKwJjXVObg9QU"

def start(update, context):
    update.message.reply_text("Olá! Eu sou o seu bot.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()7764227131:AAGflLcQQlh7XtkjJuvKGXiKwJjXVObg9QU
