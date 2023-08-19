import copy

from telebot import types

import mysql_handler
from bot_start import bot
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_main_menu import markup_main_menu
from bot_ui.markups.markup_set_avatar import markup_set_avatar
from check_is_back import check_is_back


def init_exit_button():
    @bot.message_handler(func=lambda message: message.text == "Выйти из аккаунта")
    def try_exit(message):
        if check_is_back(message):
            return
        bot.send_message(message.chat.id, 'Вы точно хотите выйти из аккаунта?',
                         reply_markup=markup_set_avatar)
        bot.register_next_step_handler(message, user_ask_exit)

    def user_ask_exit(message, markup_for_register=None):
        if check_is_back(message):
            return
        temp_markup = copy.deepcopy(markup_main_menu)
        if message.text == 'Да':
            temp_markup.row(types.KeyboardButton('Зарегистрироваться 🤝'))
            temp_markup.row(types.KeyboardButton('Авторизоваться'))
            cur = mysql_handler.connection.cursor()
            cur.execute("UPDATE sellers SET user_id = NULL WHERE user_id = %s", message.from_user.id)
            mysql_handler.connection.commit()
            bot.send_message(message.chat.id, 'Вы успешно вышли из аккаунта.', reply_markup=temp_markup)
            return
        if message.text == 'Нет':
            bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=markup_for_registrants)
            return