from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_register = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_register.add(button_main_menu)



