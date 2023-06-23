import telebot
import requests
from telebot import types

bot_token = '2120653489:AAEesZIxRz0iQiGgdDAGpvOd4YiAC4q3peE'
bot = telebot.TeleBot(bot_token)

compulsory_channel = "@jepthon"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not is_subscribed(message.chat.id):
        markup = types.InlineKeyboardMarkup()
        subscribe_button = types.InlineKeyboardButton(text="اشترك", url=f"https://t.me/jepthon")
        markup.add(subscribe_button)
        bot.send_message(message.chat.id, "عذرا عليك الاشتراك في قناة البوت @jepthon لكي تتمكن من استخدام البوت ", reply_markup=markup)
        return
    bot.reply_to(message, "اهلا بك في بوت الذكاء الاصطناعي ")

@bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id)
def reply_to_bot_message(message):
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

print('Done')
bot.infinity_polling()
