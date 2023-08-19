import re

import mysql_handler
from bot_start import bot
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from check_is_back import check_is_back


def init_change_nickname():
    @bot.message_handler(func=lambda message: message.text == "Сменить имя")
    def try_change_nickname(message):
        if check_is_back(message):
            return
        bot.send_message(message.chat.id, 'Отправьте Ваш пароль', reply_markup=markup_register)
        bot.register_next_step_handler(message, password_check)

    def password_check(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,'
                                              '?,&)')
            bot.register_next_step_handler(message, password_check)
            return
        password = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Ваш новый никнейм.')
        bot.register_next_step_handler(message, change_nickname, password)

    def change_nickname(message, password):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^[a-zA-Z]+$', message.text):
            bot.send_message(message.chat.id, 'Введите Ваш никнейм ещё раз.')
            bot.register_next_step_handler(message, change_nickname)
            return
        nickname = message.text.strip()
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE pass = %s', password)
        myresult = cur.fetchone()
        if myresult is None:
            bot.send_message(message.chat.id, 'Неправильно указан пароль.', reply_markup=markup_for_registrants)
            return
        cur.execute("UPDATE sellers SET nickname = %s WHERE pass = %s", (nickname, password))
        mysql_handler.connection.commit()
        bot.send_message(message.chat.id, 'Вы успешно сменили никнейм.',
                         reply_markup=markup_for_registrants)

