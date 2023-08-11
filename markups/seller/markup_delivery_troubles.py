from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу отследить посылку или товар был потерян в пути ✈️')
markup.add(btn1)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)