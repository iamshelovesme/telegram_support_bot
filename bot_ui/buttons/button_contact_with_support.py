import time
from bot_start import bot

owner_chat_id = "1098631749"
user_last_message = {}


def init_contact_with_support():
    @bot.message_handler(func=lambda message: message.text == "Связаться с поддержкой ☎️")
    def forward_messages(message):
        current_time = int(time.time())
        user_id = message.from_user.id
        if user_id in user_last_message and current_time - user_last_message[user_id]['timestamp'] < 24 * 60 * 60:
            bot.send_message(message.chat.id, 'Вы уже отправили сообщение в течение последних 24 часов.')
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение, которое вы хотите отправить')
            bot.register_next_step_handler(message, send_message_to_owner)

    def send_message_to_owner(message):
        user_id = message.from_user.id
        msg = (f'Ссылка на телеграм аккаунт пользователя: t.me/{message.from_user.username}\n\nСообщение '
               f'от пользователя {message.from_user.id}:\n\n{message.text}')
        bot.send_message(owner_chat_id, msg)
        bot.send_message(message.chat.id, 'Ваше сообщение успешно отправлено владельцу бота.')
        user_last_message[user_id] = {'timestamp': int(time.time())}
