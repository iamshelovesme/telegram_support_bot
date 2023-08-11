from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу выложить объявление 🚫')
markup.add(btn1)
btn2 = types.KeyboardButton('Не была выдана табличка оригинальности ✅')
markup.add(btn2)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)