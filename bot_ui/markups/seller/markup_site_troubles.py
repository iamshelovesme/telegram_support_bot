from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_site_troubles = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Не могу выложить объявление 🚫')
markup_site_troubles.add(btn1)
btn2 = types.KeyboardButton('Не была выдана табличка оригинальности ✅')
markup_site_troubles.add(btn2)
markup_site_troubles.add(button_main_menu)