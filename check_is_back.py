from bot_ui.buttons.button_main_menu_handler import back_to_main_menu


def check_is_back(message):
    if message.text is None:
        return False
    if message.text == 'Вернуться в главное меню 🏠':
        back_to_main_menu(message)
        return True
    return False