from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import get_sql_keyboard

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

category_kb = get_sql_keyboard(table='category', col='category_name', where=None)
