from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_client = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Проблема с возвратом 📦')
markup_client.add(btn1)
btn2 = types.KeyboardButton('Проблема с оплатой 💳')
markup_client.add(btn2)
btn3 = types.KeyboardButton('Проблема с продавцом 💬')
markup_client.add(btn3)
markup_client.add(button_main_menu)
