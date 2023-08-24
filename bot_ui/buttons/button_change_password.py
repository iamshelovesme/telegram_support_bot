import random
from email.mime.text import MIMEText

import mysql_handler
from bot_start import bot
from bot_ui.email_server_handler import sender, email_server
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from check_is_back import check_is_back
import re


def init_change_password():
    @bot.message_handler(func=lambda message: message.text == "Сменить пароль")
    def ask_change_password(message):
        if check_is_back(message):
            return
        bot.send_message(message.chat.id, 'Введите Ваш текущий пароль.', reply_markup=markup_register)
        bot.register_next_step_handler(message, try_change_password)

    def try_change_password(message):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,'
                                              '?,&)')
            bot.register_next_step_handler(message, try_change_password)
            return
        user_password = message.text.strip()
        bot.send_message(message.chat.id, 'Введите Ваш новый пароль.')
        bot.register_next_step_handler(message, change_password, user_password)

    def change_password(message, user_password):
        if check_is_back(message):
            return
        if message.text is None or not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$', message.text):
            bot.send_message(message.chat.id, 'Введите пароль ещё раз. Минимальная длина пароля - 8 символов.'
                                              ' Пароль должен содержать числа, а также одну заглавную и '
                                              'прописную букву. Пароль НЕ должен содержать спец. символы(@,$,!,%,*,#,'
                                              '?,&)')
            bot.register_next_step_handler(message, change_password, user_password)
            return
        new_password = message.text.strip()
        bot.send_message(message.chat.id, 'Введите код с Вашей электронной почты. Также проверьте вкладку "Спам".')
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT email FROM sellers WHERE pass = %s', user_password)
        email = cur.fetchone()
        confirmation_code = random.randint(100000, 999999)

        try:
            msg = MIMEText(str(confirmation_code))
            msg["From"] = sender
            msg["To"] = email['email']
            msg["Subject"] = "Код для подтверждения регистрации"
            email_server.sendmail(sender, email['email'], msg.as_string())
        finally:
            bot.register_next_step_handler(message, confirm_change_password, user_password, confirmation_code,
                                           new_password)

    def confirm_change_password(message, user_password, confirmation_code, new_password):
        if check_is_back(message):
            return
        if str(confirmation_code) != message.text:
            bot.send_message(message.chat.id, 'Вы неправильно ввели код.')
            bot.register_next_step_handler(message, confirm_change_password, user_password, new_password,
                                           confirmation_code)
            return
        cur = mysql_handler.connection.cursor()
        cur.execute('SELECT * FROM sellers WHERE pass = %s', user_password)
        myresult = cur.fetchone()
        if myresult is None:
            bot.send_message(message.chat.id, 'Неправильный пароль.', reply_markup=markup_for_registrants)
            return
        else:
            cur.execute('UPDATE sellers SET pass = %s WHERE user_id = %s', (new_password, message.from_user.id))
            mysql_handler.connection.commit()
            bot.send_message(message.chat.id, 'Вы успешно сменили пароль.',
                             reply_markup=markup_for_registrants)
