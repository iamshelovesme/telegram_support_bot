from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу привязать свою карту 🚫💳')
markup.row(btn1)
btn2 = types.KeyboardButton('Не могу привязать электронный кошелёк 🚫📱')
markup.row(btn2)
btn3 = types.KeyboardButton('Не вернулись деньги после отмены заказа от продавца из Китая 🚫💸🇨🇳')
markup.row(btn3)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.row(back)