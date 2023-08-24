from telebot import types

from bot_ui.buttons.button_main_menu import button_main_menu

markup_send_email = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Отправить письмо')
markup_send_email.row(btn1)
markup_send_email.add(button_main_menu)