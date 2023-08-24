from telebot import types

markup_for_registrants = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Профиль")
markup_for_registrants.add(btn1)
btn2 = types.KeyboardButton("Помощь")
markup_for_registrants.add(btn2)