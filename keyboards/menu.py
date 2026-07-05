from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Каталог")],
            [KeyboardButton(text="КНОПКА НЕ РАБОТАЕТ"),
             KeyboardButton(text="О боте")
            ],
        ],
        resize_keyboard=True,
    )