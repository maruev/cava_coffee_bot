from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

# Клавиатура заглушка для карточки товара
product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton('S\n150р', callback_data='text'),
        InlineKeyboardButton('M\n250р', callback_data='text'),
        InlineKeyboardButton('L\n350р', callback_data='text'),
        ]
    ]
)

