from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Товар не высвечивается в меню обмена 🚫👖')
markup.add(btn1)
btn2 = types.KeyboardButton('Хочу отменить обмен 🚫🤝')
markup.add(btn2)
btn3 = types.KeyboardButton('Пришло не то, что было в заказе 🙅👖')
markup.add(btn3)
back = types.KeyboardButton('Вернуться в главное меню 🏠')
markup.add(back)