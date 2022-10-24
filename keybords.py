from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import get_sql_keyboard

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

category_kb = get_sql_keyboard('category', 'category_name')
