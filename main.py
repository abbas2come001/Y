import telebot

import requests

from telebot import types

bot_token = '1763050398:AAEQIm8VolEnlLpKl9NdwHDQiMZ9_a1A9Xo'

bot = telebot.TeleBot(bot_token)

compulsory_channel = "@jepthon"

@bot.message_handler(commands=['start'])

def send_welcome(message):

    # Check if the user is subscribed to the compulsory channel

    if not is_subscribed(message.chat.id):

        # Create the subscription markup

        markup = types.InlineKeyboardMarkup()

        subscribe_button = types.InlineKeyboardButton(text="اشترك", url=f"https://t.me/jepthon")

        markup.add(subscribe_button)

        # Send the subscription message

        bot.send_message(message.chat.id, "عذرا عليك الاشتراك في قناة البوت @jepthon لكي تتمكن من استخدام البوت ", reply_markup=markup)

        return

    bot.reply_to(message, "اهلا بك في بوت الذكاء الاصطناعي ")

@bot.message_handler(func=lambda message: True)

def echo_all(message):

    text = message.text

    response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text

    bot.reply_to(message, response)

def is_subscribed(chat_id):

    try:

        chat_member = bot.get_chat_member(compulsory_channel, chat_id)

        if chat_member.status == 'member' or chat_member.status == 'creator' or chat_member.status == 'administrator':

            return True

    except telebot.apihelper.ApiException:

        pass

    return False

print ('Done')
bot.infinity_polling()
