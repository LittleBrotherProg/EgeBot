import telebot
from telebot import types
import config
import pars
with open('token.txt') as token:
	token = token.read()
bot = telebot.TeleBot(token, 
		            parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("👋 Поздороваться")
	btn2 = types.KeyboardButton("Выбор предмета")
	markup.add(btn1, btn2)
	bot.send_message(
					message.chat.id, 
		  			text='Приветствую, я бот помощник к успешной сдачи ЕГЭ',
                    reply_markup=markup
					)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что пользуешся мной!)")
    elif(message.text == "Выбор предмета"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Информатика")
        btn2 = types.KeyboardButton("Математика")
        back = types.KeyboardButton("Физика")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    elif(message.text == "Информатика"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Тестовая часть")
        btn2 = types.KeyboardButton("Задания, не входящие в ЕГЭ этого года")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите задание", reply_markup=markup)
        u = pars.pars_link('https://inf-ege.sdamgia.ru/')
        answer = u.pars_link_task()
        for i, button in enumerate(answer):
            print(button['link task'])
            print('-' * 20)
            
             
	
bot.infinity_polling()