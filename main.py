import telebot
from telebot import types
import config
import json
with open('token.txt') as token:
	token = token.read()
bot = telebot.TeleBot(token, 
		            parse_mode=None)

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
        with open('all_task.json', 'r', encoding='utf-8') as all_task:
              academic_subjects = json.load(all_task)
        all_btn = list()
        markup = types.InlineKeyboardMarkup(row_width=2)
        for index, academic_subject in enumerate(academic_subjects):
              key_academic_subject = academic_subject.keys()
              name_academic_subject = ''.join(key_academic_subject)
              all_task = academic_subject.get(name_academic_subject)
              btn = types.InlineKeyboardButton(name_academic_subject, callback_data=[str(index), 'academic_subject'])
              all_btn.append(btn)
        markup.add(*all_btn)
        bot.send_message(message.chat.id, text="Выбери предмет:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.back[1] == 'academic_subject':
        with open('all_task.json', 'r', encoding='utf-8') as all_task:
                academic_subjects = json.load(
                                                all_task
                                                )
        task = academic_subjects[int(call.data)]
        new_menu = types.InlineKeyboardMarkup(row_width=1)
        all_btn = list()
        for index, task in enumerate(task.get(''.join(task.keys()))):
                key_task =  task.keys()
                name_task = ''.join(key_task)
                if len(task.get(name_task)) != 0:  
                    btn = types.InlineKeyboardButton(name_task, callback_data=int(call.back[0]))
                else:
                    continue
                all_btn.append(btn)
        new_menu.add(*all_btn)
        bot.edit_message_text('ВЫберите категорию', call.message.chat.id, call.message.message_id,
                                reply_markup=new_menu)
         #  if call.data[0] == "academic_subject" :
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