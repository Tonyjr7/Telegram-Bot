import telebot
from newsapi import NewsApiClient

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='8a9b88d96a6c4c9e9be3a287133361f1')

# Initialize Telegram Bot
bot = telebot.TeleBot('6726808689:AAHgxQMjV61PEDhZ2FRcEjPlfmza_It9Rnc')

# Command to fetch top headlines
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to News Bot! Use /news to get the latest headlines.")

# Command to fetch top headlines
@bot.message_handler(commands=['news'])
def send_news(message):
    top_headlines = newsapi.get_top_headlines(language='en')
    articles = top_headlines['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        bot.send_message(message.chat.id, f"*{title}*\n{description}\n[Read more]({url})", parse_mode="Markdown")

# Handle unknown commands
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Sorry, I don't understand that command.")

# Polling for updates
bot.polling()
