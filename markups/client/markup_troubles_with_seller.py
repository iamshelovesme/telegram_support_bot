from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Продавец не отправляет заказ 🚫📦')
markup.row(btn1)
btn2 = types.KeyboardButton('Продавец перенаправляет на другие сервисы 👀')
markup.row(btn2)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.row(back)