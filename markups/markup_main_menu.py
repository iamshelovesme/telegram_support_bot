from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Клиент 🧑‍💼')
btn2 = types.KeyboardButton('Продавец 👨‍💼')
markup.row(btn1, btn2)
btn3 = types.KeyboardButton('Связаться с поддержкой ☎️')
btn4 = types.KeyboardButton('Зарегистрироваться 🤝')
markup.row(btn3,btn4)