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

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Молоко:\nКлассика', callback_data='_'),
            InlineKeyboardButton(text='Сироп:\nКарамель', callback_data='_'),
        ],
        [
            InlineKeyboardButton(text='Доп. шот эспрессо:\nНет', callback_data='_'),
        ],
        [
            InlineKeyboardButton(text='-', callback_data='_'),
            InlineKeyboardButton(text='1 шт.\n300 р.', callback_data='_'),
            InlineKeyboardButton(text='+', callback_data='_'),
        ],
        [
            InlineKeyboardButton(text='Добавить в корзину', callback_data='_'),
        ],
    ]
)

