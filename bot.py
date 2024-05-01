import telebot
from newsapi import NewsApiClient

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='8a9b88d96a6c4c9e9be3a287133361f1')

# Initialize Telegram Bot
bot = telebot.TeleBot('6726808689:AAHgxQMjV61PEDhZ2FRcEjPlfmza_It9Rnc')

# Command to fetch top headlines
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to News Bot! Use /categories to see available categories, /location to set your location, and /news <category> to get news from a specific category.")

# Command to fetch news based on category
@bot.message_handler(commands=['news'])
def send_news_by_category(message):
    args = message.text.split()[1:]
    if args:
        category = args[0]
        if category.lower() not in ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology', 'forex', 'crypto']:
            bot.reply_to(message, "Invalid category. Please choose one of: business, entertainment, general, health, science, sports, technology, forex, crypto")
            return
        top_headlines = newsapi.get_top_headlines(category=category.lower(), language='en')
        articles = top_headlines['articles']
        for article in articles:
            title = article['title']
            description = article['description']
            url = article['url']
            bot.send_message(message.chat.id, f"*{title}*\n{description}\n[Read more]({url})", parse_mode="Markdown")
    else:
        bot.reply_to(message, "Please specify a category. Use /categories to see available categories.")

# Command to fetch news categories
@bot.message_handler(commands=['categories'])
def send_categories(message):
    bot.reply_to(message, "Available categories: business, entertainment, general, health, science, sports, technology, forex, crypto")

# Command to set user's location
@bot.message_handler(commands=['location'])
def set_location(message):
    bot.reply_to(message, "Please share your live location so we can provide news based on your location.")

# Handle unknown commands
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(message, "Sorry, I don't understand that command.")

# Handle location messages
@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    top_headlines = newsapi.get_top_headlines(language='en', latitude=latitude, longitude=longitude)
    articles = top_headlines['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        bot.send_message(message.chat.id, f"*{title}*\n{description}\n[Read more]({url})", parse_mode="Markdown")

# Polling for updates
bot.polling()
