from bot_start import bot
from utility import read_text_message
from bot_ui.markups.seller.markup_seller import markup_seller as markupSeller
from bot_ui.markups.seller.markup_site_troubles import markup_site_troubles as markupSiteTroubles
from bot_ui.markups.seller.markup_delivery_troubles import markup_delivery_troubles as markupDeliveryTroubles
from bot_ui.markups.seller.markup_troubles_with_client import markup_troubles_with_client as markupTroublesWithClient
from bot_ui.markups.seller.markup_trade_troubles import markup_trade_troubles as markupTradeTroubles


def init_button_seller():
    @bot.message_handler(func=lambda message: message.text == "Продавец 👨‍💼")
    def seller_menu(message):
        bot.send_message(message.chat.id, 'Выберите свою проблему', reply_markup=markupSeller)

    @bot.message_handler(func=lambda message: message.text == "Проблeмы с сайтом 💻")
    def site_troubles(message):
        bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupSiteTroubles)

    @bot.message_handler(func=lambda message: message.text == "Проблемы с доставкой 📦")
    def delivery_troubles(message):
        bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupDeliveryTroubles)

    @bot.message_handler(func=lambda message: message.text == "Проблемы с обменом 🔄")
    def trade_troubles(message):
        bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupTradeTroubles)

    @bot.message_handler(func=lambda message: message.text == "Проблемы с покупателем 💬")
    def troubles_with_client(message):
        bot.send_message(message.chat.id, 'А конкретнее?', reply_markup=markupTroublesWithClient)

    @bot.message_handler(func=lambda message: message.text == "Не могу выложить объявление 🚫")
    def troubles_with_announcement(message):
        bot.send_message(message.chat.id,
                         read_text_message('txt_files/seller_troubles/Не могу выложить объявление.txt'))

    @bot.message_handler(func=lambda message: message.text == "Не была выдана табличка оригинальности ✅")
    def troubles_with_legit_check(message):
        bot.send_message(message.chat.id, read_text_message(
            'txt_files/seller_troubles/Не была выдана табличка оригинальности.txt'))

    @bot.message_handler(
        func=lambda message: message.text == "Не могу отследить посылку или товар был потерян в пути ✈️")
    def troubles_with_package(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Не могу отследить посылку или '
                                                            'товар был потерян в пути.txt'))

    @bot.message_handler(func=lambda message: message.text == "Покупатель испортил товар 🤜👖")
    def client_ruined_clothes(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Покупатель испортил товар.txt'))

    @bot.message_handler(func=lambda message: message.text == "Покупатель перенаправляет на сторонние сервисы 👀")
    def suspicious_client(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Покупатель перенаправляет '
                                                            'на сторонние сервисы.txt'))

    @bot.message_handler(func=lambda message: message.text == "Товар не высвечивается в меню обмена 🚫👖")
    def troubles_with_site(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Товар не высвечивается в меню '
                                                            'обмена.txt'))

    @bot.message_handler(func=lambda message: message.text == "Хочу отменить обмен 🚫🤝")
    def canceled_trade(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Хочу отменить обмен.txt'))

    @bot.message_handler(func=lambda message: message.text == "Пришло не то, что было в заказе 🙅👖")
    def wrong_clothes(message):
        bot.send_message(message.chat.id, read_text_message('txt_files/seller_troubles/Пришло не то,'
                                                            ' что было в заказе.txt'))
