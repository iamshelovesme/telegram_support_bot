import copy

from telebot import types

import mysql_handler
from bot_start import bot
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_main_menu import markup_main_menu


@bot.message_handler(func=lambda message: message.text == "Вернуться в главное меню 🏠")
def back_to_main_menu(message):
    cur = mysql_handler.connection.cursor()
    cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
    user = cur.fetchone()
    temp_markup = copy.deepcopy(markup_main_menu)
    if user is None:
        temp_markup.row(types.KeyboardButton('Зарегистрироваться 🤝'))
        temp_markup.row(types.KeyboardButton('Авторизоваться'))
        bot.send_message(message.chat.id, "Вы вернулись в главное меню.", reply_markup=temp_markup)
    if user is not None:
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=markup_for_registrants)