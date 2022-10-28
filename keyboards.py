from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

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

inline_default_kb = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text='Сделать заказ', callback_data='Сделать заказ'),
            InlineKeyboardButton(text='О нас', callback_data='_'),
        ],
        [
            InlineKeyboardButton(text='Обратная связь', callback_data='_'),
            InlineKeyboardButton(text='Контакты', callback_data='_'),
        ],
    ]
)

