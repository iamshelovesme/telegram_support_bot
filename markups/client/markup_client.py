from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Проблема с возвратом 📦')
markup.add(btn1)
btn2 = types.KeyboardButton('Проблема с оплатой 💳')
markup.add(btn2)
btn3 = types.KeyboardButton('Проблема с продавцом 💬')
markup.add(btn3)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)
