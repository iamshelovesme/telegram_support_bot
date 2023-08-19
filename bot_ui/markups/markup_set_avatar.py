from telebot import types

from bot_ui.buttons.button_main_menu import button_main_menu

markup_set_avatar = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Да')
btn2 = types.KeyboardButton('Нет')
markup_set_avatar.add(btn1, btn2)
markup_set_avatar.row(button_main_menu)
