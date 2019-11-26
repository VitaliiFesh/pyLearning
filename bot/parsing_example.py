# подключаем библиотеки
import requests
import random
from bs4 import BeautifulSoup
from datetime import date, timedelta
import telegram
import telebot

# будем брать информацию за вчерашний день
yesterday = date.today() - timedelta(1)
yesterday_str = yesterday.strftime('%d.%m.%Y')

# На некоторых сайтах стоит минимальная защита и они не отдают контент без user-agent
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
# чтобы избежать кэширования на любом уровне, на всякий случай добавим случайно число
r = requests.get('http://agentsclothes.com/?r=' + str(random.random()))

# парсинг заголовков и времени создания новости
soup = BeautifulSoup(r.text, 'html.parser')
h2s = soup.find_all('h2', class_='PostHeaderIcon-wrapper')
h2s = [x.text.strip() for x in h2s]
times = soup.find_all('div', class_='PostHeaderIcons metadata-icons')
times = [x.text.strip() for x in times]

print(h2s)
for k, t in enumerate(times):
    if t.split()[0] == yesterday_str:  # если новость за вчера, то постим
        # Непосредственно здесь идет отправка. Инициализируем бота с помощью токена
        bot = telebot.TeleBot('827493851:AAGkULKGOgq5nBQ1B6pWxtfKlLwQ5Qmn_Xs')
        chat_id = '309423855'
        # тест новости
        chat_text = 'Новая новость на <a href="http://agentsclothes.com/">сайте</a>:\n <b>{}</b>'.format(h2s[k])
        # отправка поста в канал. Маленькая тонкость - используется HTML разметка
        bot.send_message(chat_id=chat_id, text=chat_text, parse_mode=telegram.ParseMode.HTML)