import telebot
from telebot import types


bot = telebot.TeleBot('5602078896:AAFwYR4IBEdjguEYii4fsG03DPoAwpTqcQU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}, это бот ЭМШ! Ответьте на некоторые вопросы, чтобы я смог Вам помочь!".format(message.from_user))
    bot.send_message(message.chat.id, text="Для начала напишите свое ФИО!")
    bot.register_next_step_handler(message, fio)

def fio(message):
    fio = str(message.text).replace(" ", "").upper()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Школьник")
    btn2 = types.KeyboardButton("Родитель")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Выберите свой статус:", reply_markup=markup)

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
        bot.send_message(message.chat.id, text="Выберите формат обучения:", reply_markup=markup)

    if (message.text == "Онлайн") or (message.text == "Оффлайн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зачетные курсы/Юрьев день")
        btn2 = types.KeyboardButton("Перевод между подразделениями")
        btn3 = types.KeyboardButton("Прочее")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Теперь выберите тему своего вопроса:", reply_markup=markup)



bot.polling(none_stop=True)

