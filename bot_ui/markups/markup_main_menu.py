from telebot import types

markup_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Клиент 🧑‍💼')
btn2 = types.KeyboardButton('Продавец 👨‍💼')
markup_main_menu.row(btn1, btn2)
btn3 = types.KeyboardButton('Связаться с поддержкой ☎️')
markup_main_menu.row(btn3)
