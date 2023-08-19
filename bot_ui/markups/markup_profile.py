from telebot import types
from bot_ui.buttons.button_main_menu import button_main_menu

markup_profile = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Сменить email')
btn2 = types.KeyboardButton('Сменить пароль')
markup_profile.add(btn1, btn2)
btn3 = types.KeyboardButton('Сменить имя')
btn4 = types.KeyboardButton('Сменить аватар')
markup_profile.add(btn3,btn4)
btn5 = types.KeyboardButton('Выйти из аккаунта')
markup_profile.add(btn5)
markup_profile.add(button_main_menu)
