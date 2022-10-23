from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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

