from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Клиент 🧑‍💼')
btn2 = types.KeyboardButton('Продавец 👨‍💼')
markup.row(btn1, btn2)
btn3 = types.KeyboardButton('Связаться с поддержкой ☎️')
markup.row(btn3)