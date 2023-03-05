import telebot
from telebot import types
import pandas as pd

dataset = pd.read_csv('baza.csv', delimiter=',', names = ['FIO', 'COURSE1', 'COURSE2'])
group = pd.read_csv('group.csv', encoding = 'utf-8', delimiter=',', names = ['NAME', 'LINK'])

bot = telebot.TeleBot('5602078896:AAFwYR4IBEdjguEYii4fsG03DPoAwpTqcQU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Школьник")
    btn2 = types.KeyboardButton("Родитель")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Ответь на некоторые вопросы, чтобы мы смогли тебе помочь!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def info(message):
    if (message.text == "Школьник") or (message.text == "Родитель"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("8")
        btn2 = types.KeyboardButton("9")
        btn3 = types.KeyboardButton("10")
        btn4 = types.KeyboardButton("11")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите класс обучения:", reply_markup=markup)

    if (message.text == "8") or (message.text == "9") or (message.text == "10") or (message.text == "11"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Онлайн")
        btn2 = types.KeyboardButton("Оффлайн")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Выбери формат обучения:", reply_markup=markup)

    if (message.text == "Онлайн") or (message.text == "Оффлайн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зачетные курсы/Юрьев день")
        btn2 = types.KeyboardButton("Перевод между подразделениями")
        btn3 = types.KeyboardButton("Прочее")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Теперь выбери тему своего вопроса:", reply_markup=markup)
        bot.register_next_step_handler(message, dop)

def dop(message):
    if (message.text == "Зачетные курсы/Юрьев день"):
        bot.send_message(message.chat.id, text="Введите ФИО")
        bot.register_next_step_handler(message, course)
    if (message.text == "Перевод между подразделениями"):
        bot.send_message(message.chat.id, text="Укажите причину перевода")
        bot.register_next_step_handler(message, trans)
    if (message.text == "Прочее"):
        bot.send_message(message.chat.id, text="Напишите свой запрос")
        bot.register_next_step_handler(message, trans)

def course(message):
    fio = str(message.text).replace(" ", "").upper()
    a = dataset[dataset.FIO == fio]
    a1 = ((str(a.COURSE1)).split())
    a2 = ((str(a.COURSE2)).split())
    a1 = a1[1:len(a1) - 4]
    a2 = a2[1:len(a2) - 4]

    s1 = str(a1[0])
    for elem in a1[1:]:
        s1 = s1 + " " + str(elem)
    s2 = str(a2[0])
    for elem in a2[1:]:
        s2 = s2 + " " + str(elem)

    b1 = group[group.NAME == str(s1)]
    b2 = group[group.NAME == str(s2)]
    bot.send_message(message.chat.id, text = "Ваши зачетные курсы:\n" + s1 + ": " + (str(b1.LINK)).split()[1] +"\n" + s2 + ": " + (str(b2.LINK)).split()[1])


def trans(message):
    bot.send_message(message.chat.id, text="Ваш запрос отправлен Совету. Ожидайте ответа!")

#def other(message):
#    bot.send_message(message.chat.id, text="Ваш запрос отправлен Совету. Ожидайте ответа!")



bot.polling(none_stop=True)















