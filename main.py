from telebot import types

import mysql_handler
from bot_start import bot
from bot_ui.buttons.button_contact_with_support import init_contact_with_support as init_contact_with_support
from bot_ui.buttons.button_register import init_register as init_register
from bot_ui.buttons.button_client import init_button_client as init_button_client
from bot_ui.buttons.button_seller import init_button_seller as init_button_seller
from bot_ui.markups.markup_main_menu import markup_main_menu as markupMainMenu
from mysql_handler import connection

init_register()
init_contact_with_support()
init_button_client()
init_button_seller()


@bot.message_handler(commands=['start'])
def start(message):
    cur = mysql_handler.connection.cursor()
    cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
    user = cur.fetchone()
    temp_markup = markupMainMenu
    if user is None:
        temp_markup.row(types.KeyboardButton('Зарегистрироваться 🤝'))
        temp_markup.row(types.KeyboardButton('Авторизоваться'))
    if user is not None:
        temp_markup.add(types.KeyboardButton('Профиль'))
    bot.send_message(message.chat.id, 'Привет! Я телеграм-бот техподдержки reused team. В '
                                      'интерактивном меню снизу выбери кто ты, чтобы я помог '
                                      'решить твою проблему.', reply_markup=temp_markup)


print('Бот запустился')

bot.infinity_polling()
