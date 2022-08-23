import telebot
import requests

token = "5472843285:AAF2eWPawyb-uqKZQi3PSqWXyF1iKCUImA8"
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(messages):
    bot.reply_to(messages, 'Welcome')


@bot.message_handler(commands=['recipe'])
def send_welcome(messages):
    get_data = requests.get("http://127.0.0.1:8000/api/posts/")
    get_data_text = get_data.text
    bot.reply_to(messages, str(get_data_text))


bot.infinity_polling()
