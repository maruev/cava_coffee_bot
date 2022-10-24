from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import get_list_of_keyboard_buttons

buttons_back_mainmenu = [
    KeyboardButton(text='Назад'),
    KeyboardButton(text='Главное меню'),
]

default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О нас'),
        ],
        [
            KeyboardButton(text='Обратная связь'),
            KeyboardButton(text='Контакты'),
        ],
    ], resize_keyboard=True
)

