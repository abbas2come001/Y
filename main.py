import telebot
import requests
from telebot import types

bot_token = '2120653489:AAEesZIxRz0iQiGgdDAGpvOd4YiAC4q3peE'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اهلا بك في بوت الذكاء الاصطناعي ")

@bot.message_handler(func=lambda message: message.from_user.id == bot.get_me().id or message.text and message.text.lower() == "حسين")
def reply_to_hussein(message):
    if message.from_user.id == bot.get_me().id:
        response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={message.text}').text
        bot.reply_to(message, response)
    else:
        response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={message.text}').text
        bot.reply_to(message, response)

print('Done')
bot.infinity_polling()
