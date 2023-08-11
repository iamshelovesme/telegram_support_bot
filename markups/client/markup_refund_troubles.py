from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу оформить возврат товара от продавца из Китая 🚫🔄🇨🇳')
markup.row(btn1)
btn2 = types.KeyboardButton('Не вернулись деньги после возврата товара от продавца из Китая 🚫💸🇨🇳')
markup.row(btn2)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.row(back)