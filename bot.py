#coding:utf8
import requests, urllib.request, json, time
import telebot
import sys
import requests
global infoPhones
from bs4 import BeautifulSoup
import getopt
import pyperclip
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers
import argparse
import requests
import random
from telebot import types
from pycbrf.toolbox import ExchangeRates
import datetime
from datetime import datetime, timedelta
global keyboard
global keyboard_script
global keyboard_music
import os, sys
import random
users_amount = [0]
chat_ids_file = 'chat_ids.txt'
stiker_epilep_id = 'AACAgIAAxkBAAK7dV69lfgFHAzZH78-4vIQ7ph98WrBAALzngEAAWOLRgwVfa67bOkhFxkE'
token = str(os.environ.get('BOT_TOKEN'))
bot = telebot.TeleBot(token)
types = telebot.types
##############################################
#                SAVE_CHAT_ID                #
##############################################
def save_chat_id(chat_id):

    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return

#####################################
#            GETPROXY               #
#####################################
@bot.message_handler(commands=['getproxy'])
def getprox(message):
	chat = message.chat.id
	f = open('prox.txt','w')
	def get_site(site):
		r = requests.get(site)
		return r.text
	def datas(html):
		soup = BeautifulSoup(html, 'lxml')
		line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')

		for tr in line:
			td = tr.find_all('td')
			ip = td[1].text
			port = td[2].text
			data = ip+':'+port
			f.write(data + '\n')
		f.close()

	def main():
		url = 'http://foxtools.ru/Proxy'
		datas(get_site(url))
	main()
	e = open('prox.txt','rb')
	bot.send_document(chat,e)
	e.close()

#####################################
#			  CORONA                #
#####################################
import requests
from bs4 import BeautifulSoup
@bot.message_handler(commands = ['corona'])
def corona(message):
	chat = message.chat.id


	url = "https://xn--80aesfpebagmfblc0a.xn--p1ai//#"
	soup = BeautifulSoup(requests.get(url).content, "html.parser")
	convert = soup.findAll("div", {"class": "cv-countdown__item-value"})
	msg = '---------------------------------'
	msg += "\nЗаболевших: " + convert[1].text
	msg += "\nЗаболевших за сутки: " + convert[2].text
	msg += "\nВыздоровело: " + convert[3].text
	msg += "\nУмерло: " + convert[4].text
	msg += '\n----------------------------------'
	bot.send_message(chat,msg)
#####################################
#			   PASSGEN              #
#####################################
@bot.message_handler(commands=['passgen'])
def begin(message):
	chat = message.chat.id
	msg = bot.send_message(chat,'Введи ключевые слова, для создания словаря(без пробелов):')
	bot.register_next_step_handler(msg,mainw)
def mainw(message):
	chat = message.chat.id
	text = message.text
	a = 'qehbieuwidwfcretjh5jebyj8w3hmcpmdf'
	paser = text
	b = random.choice(a)
	os.system('python passgen.py -f -o'+' '+'pass.txt'+' '+paser)
	w = open('pass.txt','rb')
	bot.send_document(chat,w)
	w.close()
	print(f"{chat}: {message.text}")



def shopen(message):
	chat = message.chat.id
	keyboard_shopen = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	etud = types.KeyboardButton(text='РеволюционныйЭтюд')
	exit = types.KeyboardButton(text='Назад')
	buttons = [etud,exit]
	keyboard_shopen.add(*buttons)
	bot.send_message(chat,'Это пока что все песни, которые я смог скачать;(\nНо список будет пополняться!',reply_markup=keyboard_shopen)
def scorp(message):
	chat = message.chat.id
	keyboard_scorp = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	still = types.KeyboardButton(text='ImStillLovinYou')
	exit = types.KeyboardButton(text='Назад')
	buttons = [still,exit]
	keyboard_scorp.add(*buttons)
	bot.send_message(chat,'Это пока что все песни, которые я смог скачать;(\nНо список будет пополняться!',reply_markup=keyboard_scorp)
def KisS(message):
	chat = message.chat.id
	keyboard_kiss = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	bt1 = types.KeyboardButton(text='I was made for Lovin\' You')
	exit = types.KeyboardButton(text='Назад')
	buttons = [bt1,exit]
	keyboard_kiss.add(*buttons)
	bot.send_message(chat,'Это пока что все песни, которые я смог скачать;(\nНо список будет пополняться!',reply_markup=keyboard_kiss)
def deep_purple(message):
	chat = message.chat.id
	keyboard_dp = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	smoke = types.KeyboardButton(text='SmokeOnTheWater')
	sold = types.KeyboardButton(text='SolderOfLove')
	ex = types.KeyboardButton(text='Назад')
	btn = [smoke,sold,ex]
	keyboard_dp.add(*btn)
	bot.send_message(chat,'Вот все, что я смок скачать;(\nНо список будет пополняться!',reply_markup=keyboard_dp)
def music_menu(message):
	chat = message.chat.id
	keyboard_music = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	xcho = types.KeyboardButton(text='Xcho')
	dp = types.KeyboardButton(text='Deep Purple')
	shopen = types.KeyboardButton(text='Shopen')
	kis = types.KeyboardButton(text='Kiss')
	scorp = types.KeyboardButton(text='Scorpions')
	exit = types.KeyboardButton(text='Назад')
	buttons = [xcho,shopen,dp,kis,scorp,exit]
	keyboard_music.add(*buttons)
	bot.send_message(chat,'Вот немного райской музыки ;3',reply_markup=keyboard_music)
	'''
	elif text == 'Бустер':
		bus = open('dim_buster.mp3','rb')
		bot.send_audio(chat,bus)
	elif text == 'Трэп':
		trap = open('trap.m4a','rb')
		bot.send_audio(chat,trap)
	elif text == 'Kiss':
		KisS(messages)
	elif text == 'Мияги&Эндшпиль':
		cap = open('miyagi_capitan.mp3','rb')
		samurai = open('miyagi_-_samuray.mp3','rb')
		plak = open('miyagi-endshpil_-_zaplakannaya-ft-amigo.mp3','rb')
		poy = open('miyagi_-_rodnaya-poy-ft-kadi.mp3','rb')
		bot.send_audio(chat,plak)
		bot.send_audio(chat,cap)
		bot.send_audio(chat,poy)
		bot.send_audio(chat,samurai)
	elif text == 'Shopen':
		bot.send_message(chat,'Революционный этюд Шопена')
		shop = open('etud_shopen.mp3','rb')
		bot.send_audio(chat,shop)
	elif text == 'Xcho':
		icanfly = open('Xcho - I Can Fly.mp3','rb')
		bot.send_audio(chat,icanfly)
	elif text == 'AYE':
		vor = open('tbilisi.mp3','rb')
		tom = open('tomas_shelby.mp3','rb')
		bot.send_audio(chat,vor)
		bot.send_audio(chat,tom)
	elif text == 'Назад':
		bot.send_message(chat,'...',keyboard(message))
'''

#bot.send_message(message.chat.id, "Вы написали: {0}".format(message.text))

'''
def pasgen(message):

	import random
	f = open('pass.txt','w')

	chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	bot.send_message(message.chat.id,'Введите количество паролей(просто цифру):')
	time.sleep(2)
	number = message.from_user.id
	bot.send_message(message.chat.id,'Введит длину пароля:')
	length = message.from_user.id
	number = int(number)
	length = int(length)
	for n in range(number):
		password =''
		for i in range(length):
			password += random.choice(chars)
			print(password)
	f.write(password + "\n")
	passw = open('pass.txt','rb')
	bot.send_document(message.chat.id,passw)
	f.close()
'''



def keyboard(message):
	chat = message.chat.id
	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	commands = types.KeyboardButton(text='Команды📜')
	infor = types.KeyboardButton(text='Об авторе🐱‍💻')
	lol = types.KeyboardButton(text='Наркомания💊')
	love = types.KeyboardButton(text='Доза любви❤️')
	music = types.KeyboardButton(text='Музыка🎧')
	off = types.KeyboardButton(text='Генератор обзываний🤬')
	info = types.KeyboardButton(text='Эдем - что это?')
	scripts = types.KeyboardButton(text='Скриптики(и не только)')
	buttons = [commands, infor,lol,music,off,info,scripts]
	keyboard.add(*buttons)
	bot.send_message(chat,'Выберите',reply_markup=keyboard)

banner = '''
______hi,_my_______honey.
____i'm_really___happy_that
__my_mailbox_is_full_of_those
_pretty_hearts_every_day.__so,
i_just_thought_i_would_return
the_favor,_just_in_case_you'd
_not_yet_realized_just_how_i
___love_you.__you_are_just
_____so_very,_very,_very
_______extraordinarily
________special_and
___________i_adore
_____________you
______________!
'''
"""
@bot.message_handler(commands=["pas"])

def handle_text(message):


	import random
	f = open('pass.txt','w')

	chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	bot.send_message(message.chat.id,'Введите количество паролей(просто цифру):')

	time.sleep(2)
	number = message.from_user.id
	bot.send_message(message.chat.id,'Введит длину пароля:')
	length = message.from_user.id
	number = int(number)
	length = int(length)
	for n in range(number):
		password =''
		for i in range(length):
			password += random.choice(chars)

	f.write(password + "\n")
	passw = open('pass.txt','rb')
	bot.send_document(message.chat.id,passw)
	f.close()
  """



def exchangeusd(message):
	chat = message.chat.id
	now = datetime.now()
	rates = ExchangeRates(str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')))
	rates.date_requested
	rates.date_received
	rates.dates_match
	rates['USD'].name
	rates['R01235'].name
	rates['840'].name
	a = str(rates['USD'].name + "\n")
	a += str(rates['USD'].rate)
	bot.send_message(chat,a)
def exchangeeur(message):
	chat = message.chat.id
	now = datetime.now()
	rates = ExchangeRates(str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')))
	rates.date_requested
	rates.date_received
	rates.dates_match
	rates['EUR'].name
	a = (str(rates['EUR'].name)+'\n'+str(rates['EUR'].rate))
	bot.send_message(chat,a)
def exchangeuah(message):
	chat = message.chat.id
	now = datetime.now()
	rates = ExchangeRates(str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')))
	rates.date_requested
	rates.date_received
	rates.dates_match
	rates['UAH'].name
	a = (str(rates['UAH'].name)+'\n'+str(rates['UAH'].rate))
	bot.send_message(chat,a)
#######################################
#				START                 #
#######################################
@bot.message_handler(commands=['start'])
def start(message):
	chat = message.chat.id
	bot.send_message(chat,'Привет, у меня ты найдешь немного хорошей музыки, скриптиков и мануалов\'Кроме того у меня есть еще немного полезных функций;)\nОбщайся и лови кайф\nЖизнь - игра, играй красиво ;3 ')
	keyboard(message)
	print(f"{chat}: {message.text}")
	save_chat_id(message.chat.id)
##########################################
#               TEXT                     #
##########################################
@bot.message_handler(content_types=['text'])
def text(message):
	chat = message.chat.id
	text = message.text
	if text == 'Команды' or text == 'Команды📜' or text == 'команды':
		bot.send_message(chat,'Вот список моих скромных возможностей:\n---Приветcтвия:---\nку\nQ\nq\nпривет\nПривет\nсалам\n---Цитаты:---\nцитата\nфраза\nЦитата\nФраза\nцитаты\n---Нецензурная лексика(Бог все видит):---\nблять\nсука\nебать\nбля\nхуй\nпидор\n---Курс ЦБ(EUR,USD)---\nкурс\n---прЕклы---\nсердце\nДоза любви\nдоза любви\nнаркомания\nНаркомания\n---Музыка !в разработке!---\nмузыка\nМузыка\n---Пароли---\n/passgen - создать базу паролей для брута\n---Статистика COVID в РФ---\n/corona\n---Райские PROXY---\n/getproxy\nАвтор: @foxeditor')
	elif text == 'курс':
		exchangeusd(message)
		exchangeeur(message)
		exchangeuah(message)
	elif text == 'ген':
		pas(message)
	elif text == 'Генератор обзываний🤬' or text == 'обген' or text == 'обозвать':
		list = ['педик газированный','жертва хаотической репликации хромосом','какашка ежа','махраджабик чернопопый','личинка ежа','петрушка нерассортированная','епталох обыкновенный','шалапай волосатый','непомерно зассанный, недоразвитый и инфантильный дерьмоссанник','писькожуй обыкновенный','человек нетрадиционной ориентации(гей)','патау додс','футбольный мячик','институка проклятая','калоед необразованный']
		bot.send_message(chat,random.choice(list))
	elif text == 'Наркомания💊' or text == 'Наркомания' or text == 'наркомания':

		bot.send_sticker(chat,'CAACAgIAAxkBAAK8aF69ouJXaxBftfw6eYuFnx4lEzQSAALzngEAAWOLRgwVfa67bOkhFxkE') #привет эпилептики
	#elif text == 'пасген' or text == 'сгенерировать' or text == 'ген':
#		pasgen(message)
	elif text == 'I was made for Lovin\' You':
		kiss_love = open('music/Kiss - I Was Made For Lovin You.mp3','rb')
		bot.send_audio(chat,kiss_love)
	elif text == 'Deep Purple':
		deep_purple(message)

	elif text == 'Музыка🎧' or text == 'музыка':
		music_menu(message)

	elif text == 'Kiss':
		KisS(message)


	elif text == 'Shopen':
		bot.send_message(chat,'Революционный этюд Шопена')
		shop = open('etud_shopen.mp3','rb')
		bot.send_audio(chat,shop)
	elif text == 'Xcho':
		icanfly = open('Xcho - I Can Fly.mp3','rb')
		bot.send_audio(chat,icanfly)

	elif text == 'Назад':
		bot.send_message(chat,'...',keyboard(message))
	elif text == 'SmokeOnTheWater':
		smk = open('Deep Purple - Smoke On The Water.mp3','rb')
		bot.send_audio(chat,smk)
	elif text == 'SolderOfLove':
		sold = open('Deep Purple - Soldier Of Fortune.mp3','rb')
		bot.send_audio(chat,sold)
	elif text == 'Scorpions':
		scorp(message)
	elif text == 'ImStillLovinYou':
		sl = open('Scorpions - Still Loving You (Comeblack Version).mp3','rb')
		bot.send_audio(chat,sl)





	elif text == 'Доза любви❤️' or text == 'Доза любви' or text == 'сердце' or text == 'доза любви':
		bot.send_message(chat,banner)
	elif text == 'Эдем - что это?':
		bot.send_message(chat,'По Библии Эдем - местопребывание человека до грехопадения, проще говоря земной рай. С израильтянского языка Эдем(e\'den) - \'наслаждение\'\nТот же рай, в который мы попадаем после смерти. \'«Блаженны падшие в сраженье: Теперь они вошли в эдем, и потонули в наслажденье, не отравляемом ничем.» А.С Пушкин.\'\nНа сегодняшний день, смертный человек попадает в эдем только после смерти. Вход в него закрылся после грехопадения Адама и Евы.\n')



	elif text == 'ку' or text == 'Q' or text == 'q' or text == 'привет' or text == 'Привет' or text == 'салам':
		bot.send_message(chat,'Прветствую в Райском притоне;3\nЧувствуй себя как дома!')
	elif text == 'цитата' or text == 'фраза' or text == 'Цитата' or text == 'Фраза' or text == 'цитаты' or text == 'фразы':
		citati = ['Запомни одну фразу: все будет, но не сразу','Лев боится капканов, а лиса — волков, следовательно, надо быть подобным лисе, чтобы уметь обойти капканы, и льву, чтобы отпугнуть волков.','Если тебя друзья величают хакером, знай - ламер ты, ибо настоящего хакера не видно, не слышно и нет у него никаких друзей, кроме компьютера…\nУслышал от Айвена;)','На любой секрет найдётся хакер… Если секрет знает один, то этот секрет… может передаваться другим… воздушно- капельным путём, как вирус! На любого хакера найдётся анти-хакер, а на любой «вирус» - свой «анти-вирус»…','Денег, которые я заработал, хватит мне до конца жизни, если я умру сегодня в 16.00.','Новогоднее настроение – это когда рад видеть даже тех, кто ошибся дверью.','Ничто так не выдает человека, как то, над чем он смеётся.']
		rand = random.choice(citati)
		bot.send_message(chat,rand)
	elif text == 'блять' or text == 'сука' or text == 'ебать' or text == 'бля' or text == 'хуй' or text == 'пидор' or text == 'секс' or text == 'пизда' or text == 'пиздец':
		bot.send_message(chat,'В нашем храме мат запрещен. Просьба учесть это и больше не выражаться)')
	elif text == 'Об авторе🐱‍💻' or text == 'автор' or text == 'снуп':
		bot.send_message(chat,'Автор: @foxeditor\n\nБот не несет никакой смысловой нагрузки(кроме некоторых цитат)\n\nКанал: @montelisa\n C тебя подписка ;)')
	elif text == 'Скриптики(и не только)':
		keyboard_script = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
		vk_komms = types.KeyboardButton(text='Накрутка комментов вк')
		Dzen = types.KeyboardButton(text='Курс Дзен')
		nord = types.KeyboardButton(text='Аккаунты NordVpn')
		fish = types.KeyboardButton(text='Скрипт VK фишинга')
		nvuti = types.KeyboardButton(text='Nvuti')
		bomber = types.KeyboardButton(text='Bomber scripts')
		boom = types.KeyboardButton(text='BOOM кряк')
		exit = types.KeyboardButton(text='Назад')
		buttons = [vk_komms,Dzen,nord,fish,nvuti,bomber,boom,exit]
		keyboard_script.add(*buttons)
		bot.send_message(chat,'Забирайте подгоны ;3',reply_markup=keyboard_script)

	elif text == 'Накрутка комментов вк':
		kom = open('vk_komms.py','rb')
		bot.send_document(chat,kom)
	elif text == 'Курс Дзен':
		dzen = open('Dzen.zip','rb')
		bot.send_document(chat,dzen)
	elif text == 'Аккаунты NordVpn':
		Nord = open('nord.zip','rb')
		bot.send_document(chat,Nord)
	elif text == 'Скрипт VK фишинга':
		vk = open('fish.zip','rb')
		bot.send_document(chat,vk)
	elif text == 'Nvuti':
		bot.send_message(chat,'Скрипт не проверял, он просто есть ;3')
		nvuti = open('Nvuti.zip','rb')
		bot.send_document(chat,nvuti)
	elif text == 'Bomber scripts':
		bomber = open('bombers.zip','rb')
		bot.send_document(chat,bomber)
	elif text == 'BOOM кряк':
		boom = open('boom.zip','rb')
		bot.send_document(chat,boom)
	elif text == 'Назад':
		bot.send_message(start(message))



	else:
		bot.send_message(chat,'Это слово я не знаю, извини.')
	print(f"{chat}: {message.text}")






bot.polling(none_stop=True)

