import telebot

# Replace 'YOUR_TOKEN' with your actual bot token obtained from BotFather
TOKEN = '6726808689:AAHgxQMjV61PEDhZ2FRcEjPlfmza_It9Rnc'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Telegram Echo Bot.")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Run the bot
bot.polling()
