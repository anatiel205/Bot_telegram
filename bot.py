import os
import telebot
from flask import Flask, request
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações
TOKEN = os.getenv('TOKEN_BOT')
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Comandos do bot
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛒 Comprar Número", "💰 Ver Saldo")
    bot.send_message(
        message.chat.id,
        "🤖 *Bot de Números Virtuais*\nEscolha uma opção:",
        reply_markup=markup,
        parse_mode='Markdown'
    )

# Webhook
@app.route('/webhook/' + TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('X-Telegram-Bot-Api-Secret-Token') != WEBHOOK_SECRET:
        return "Acesso não autorizado", 403
    
    json_data = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(
        url=f"https://{os.getenv('RENDER_APP_NAME')}.onrender.com/webhook/{TOKEN}",
        secret_token=WEBHOOK_SECRET
    )
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
