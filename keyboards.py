from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import _get_inline_buttons, _get_reply_buttons

default_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сделать заказ'),
            KeyboardButton(text='О нас'),
        ],
        [
            KeyboardButton(text='Обратная связь'),
            KeyboardButton(text='Контакты'),
        ],
    ], resize_keyboard=True
)

inline_back_main_buttons = _get_inline_buttons([('Назад',), ('Главное меню',)], 0, 0) 
reply_back_main_buttons = _get_reply_buttons([('Назад',), ('Главное меню',)], 0)

