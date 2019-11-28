import telebot
from parsing_1 import sort_in_list

#chat.id=309423855
bot = telebot.TeleBot('827493851:AAGkULKGOgq5nBQ1B6pWxtfKlLwQ5Qmn_Xs')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard1.row('Жуляны', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, sort_in_list[2])
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()