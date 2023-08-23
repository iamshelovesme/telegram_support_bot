import re

from bot_start import bot
import mysql_handler
from bot_ui.buttons.button_contact_with_support import user_last_message
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from bot_ui.markups.markup_set_avatar import markup_set_avatar
from check_is_back import check_is_back
import time


def init_bind_number():

    @bot.message_handler(func=lambda message: message.text == "Привязать номер")
    def time_bind_number(message):
        current_time = int(time.time())
        user_id = message.from_user.id
        if user_id in user_last_message and current_time - user_last_message[user_id]['timestamp'] < 1 * 60 * 60:
            bot.send_message(message.chat.id, 'Вы уже пытались изменить номер в течение последнего часа.')
            return
        else:
            bot.send_message(message.chat.id, 'Вы точно хотите привязать номер телефона?',
                             reply_markup=markup_set_avatar)
        user_last_message[user_id] = {'timestamp': int(time.time())}
        bot.register_next_step_handler(message, ask_bind_number)

    def ask_bind_number(message):
        if check_is_back(message):
            return
        if message.text == 'Да':
            bot.send_message(message.chat.id, 'Введите Ваш номер телефона.', reply_markup=markup_register)
            bot.register_next_step_handler(message, bind_number)
            return
        if message.text == 'Нет':
            bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=markup_for_registrants)
            return
        bot.send_message(message.chat.id, 'Нажмите одну из кнопок на клавиатуре.')
        bot.register_next_step_handler(message, ask_bind_number)

    def bind_number(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                                 message.text):
            bot.send_message(message.chat.id, 'Введите Ваш номер ещё раз.')
            bot.register_next_step_handler(message, bind_number)
            return
        number = message.text.strip()
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE number = %s', number)
        num = cur.fetchone()
        if num is None:
            cur.execute('UPDATE sellers SET number = %s WHERE user_id = %s', (number, message.from_user.id))
            mysql_handler.connection.commit()
            bot.send_message(message.chat.id, 'Вы успешно привязали номер.', reply_markup=markup_for_registrants)
        if num is not None:
            bot.send_message(message.chat.id, 'Вы уже привязали номер телефона', reply_markup=markup_for_registrants)