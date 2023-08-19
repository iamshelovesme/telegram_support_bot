import mysql_handler
from bot_start import bot
from bot_ui.markups.markup_for_registrants import markup_for_registrants
from bot_ui.markups.markup_register import markup_register
from check_is_back import check_is_back


def init_change_avatar():
    @bot.message_handler(func=lambda message: message.text == "Сменить аватар")
    def try_change_avatar(message):
        if check_is_back(message):
            return
        bot.send_message(message.chat.id, 'Отправьте Ваш аватар.', reply_markup=markup_register)
        bot.register_next_step_handler(message, change_avatar)

    def change_avatar(message):
        if check_is_back(message):
            return
        if message.json.get('photo') is None:
            bot.send_message(message.chat.id, 'Загрузите аватар ещё раз.')
            bot.register_next_step_handler(message, change_avatar)
            return
        avatar = message.json['photo'][len(message.json['photo']) - 1]['file_id']
        cur = mysql_handler.connection.cursor()
        sql_id = cur.execute("SELECT id FROM sellers WHERE user_id = %s", message.from_user.id)
        if avatar is not None:
            file = bot.get_file(avatar)
            downloaded_file = bot.download_file(file.file_path)
            with open('user_data/avatars/{}.jpg'.format(sql_id), 'wb') as new_file:
                new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Ваш аватар успешно изменён.', reply_markup=markup_for_registrants)
