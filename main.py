import copy
from bot_ui.buttons.button_profile import init_button_profile
from telebot import types
from bot_ui.markups.markup_for_registrants import markup_for_registrants
import mysql_handler
from bot_start import bot
from bot_ui.buttons.button_contact_with_support import init_contact_with_support
from bot_ui.buttons.button_register import init_register
from bot_ui.buttons.button_client import init_button_client
from bot_ui.buttons.button_seller import init_button_seller
from bot_ui.buttons.button_authorization import init_authorization
from bot_ui.markups.markup_main_menu import markup_main_menu
from bot_ui.buttons.button_change_avatar import init_change_avatar
from bot_ui.buttons.button_change_nickname import init_change_nickname
from bot_ui.buttons.button_exit import init_exit_button
from bot_ui.buttons.button_bind_number import init_bind_number

init_register()
init_contact_with_support()
init_button_client()
init_button_seller()
init_authorization()
init_button_profile()
init_change_avatar()
init_change_nickname()
init_exit_button()
init_bind_number()


@bot.message_handler(commands=['start'])
def start(message):
    cur = mysql_handler.connection.cursor()
    cur.execute('SELECT * FROM sellers WHERE user_id = %s', message.from_user.id)
    user = cur.fetchone()
    temp_markup = copy.deepcopy(markup_main_menu)
    if user is None:
        temp_markup.row(types.KeyboardButton('Зарегистрироваться 🤝'))
        temp_markup.row(types.KeyboardButton('Авторизоваться'))
        bot.send_message(message.chat.id, 'Привет! Я телеграм-бот техподдержки reused team. В '
                                          'интерактивном меню снизу выбери кто ты, чтобы я помог '
                                          'решить твою проблему.', reply_markup=temp_markup)
    if user is not None:
        bot.send_message(message.chat.id, 'Привет! Я телеграм-бот техподдержки reused team. В '
                                          'интерактивном меню снизу выбери кто ты, чтобы я помог '
                                          'решить твою проблему.', reply_markup=markup_for_registrants)


print('Бот запустился')

bot.infinity_polling()
