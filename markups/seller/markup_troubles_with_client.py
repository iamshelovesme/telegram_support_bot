from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Покупатель испортил товар 🤜👖')
markup.add(btn1)
btn2 = types.KeyboardButton('Покупатель перенаправляет на сторонние сервисы 👀')
markup.add(btn2)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)