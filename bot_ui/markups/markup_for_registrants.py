from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_for_registrants = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Профиль")
markup_for_registrants.add(btn1)
btn2 = types.KeyboardButton("Помощь")
markup_for_registrants.add(btn2)
markup_for_registrants.add(button_main_menu)