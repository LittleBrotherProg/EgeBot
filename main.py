import telebot
from telebot import types
import config
import pars
with open('token.txt') as token:
	token = token.read()
bot = telebot.TeleBot(token, 
		            parse_mode=None)

params = ['Тестовая часть', 'Развёрнутая часть', 'Задания, не входящие в ЕГЭ этого года']
@bot.message_handler(commands=['start'], content_types=['text'])
def send_welcome(message):
	markup_welcom = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("👋 Поздороваться")
	btn2 = types.KeyboardButton("Выбор предмета")
	markup_welcom.add(btn1, btn2)
	bot.send_message(
					message.chat.id, 
		  			text='Приветствую, я бот помощник к успешной сдачи ЕГЭ',
                    reply_markup=markup_welcom
					)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что пользуешся мной!)")
    elif(message.text == "Выбор предмета"):
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("Информатика", callback_data=[params[0,2], 'Информатика'])
        btn2 = types.InlineKeyboardButton("Математика", callback_data='but2')
        btn3 = types.InlineKeyboardButton("Физика", callback_data='but3')
        btn4 = types.InlineKeyboardButton("Химия", callback_data='but4')
        btn5 = types.InlineKeyboardButton("Биология", callback_data='but5')
        btn6 = types.InlineKeyboardButton("География", callback_data='but6')
        btn7 = types.InlineKeyboardButton("Общество знание", callback_data='but7')
        btn8 = types.InlineKeyboardButton("Литература", callback_data='but8')
        btn9 = types.InlineKeyboardButton("История", callback_data='but9')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, text="Выбери предмет:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
     if call.data[0] == params[0,1] and call.data[1] == :
            new_menu = types.ReplyKeyboardMarkup()
            test02 = types.KeyboardButton('Тестовая часть',)
            new_menu.add(types.InlineKeyboardButton('Ничего нового', callback_data='but4'))
            bot.edit_message_text('Новое меню, кнопка 1', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu)
         
    # elif(message.text == "Информатика"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton("Тестовая часть")
    #     btn2 = types.KeyboardButton("Задания, не входящие в ЕГЭ этого года")
    #     btn3 = types.KeyboardButton("Развёрнутая часть")
    #     markup.add(btn1, btn2, back)
    #     bot.send_message(message.chat.id, text="Выберите задание", reply_markup=markup)
    #     u = pars.pars_link('https://inf-ege.sdamgia.ru/')
    #     answer = u.pars_link_task()
    #     for i, button in enumerate(answer):
    #         print(button['link task'])
    #         print('-' * 20)
    # elif (message.text == "Назад"):
    #     bot.send_message(message.chat.id, "Вы вернулись в меню",reply_markup=None)
            
             
	
bot.infinity_polling()