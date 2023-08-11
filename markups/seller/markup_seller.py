from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Проблeмы с сайтом 💻')
btn2 = types.KeyboardButton('Проблемы с доставкой 📦')
markup.add(btn1,btn2)
btn3 = types.KeyboardButton('Проблемы с покупателем 💬')
btn4 = types.KeyboardButton('Проблемы с обменом 🔄')
markup.add(btn3,btn4)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)