from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command, Text
from main import dp, bot
from keyboards import default_kb
from sql import get_sql_response
from utils import get_reply_keyboard, get_inline_keyboard, _get_inline_buttons, _get_reply_buttons
import re


# Хэндлер для отправки пользователю стартового меню
@dp.message_handler(Command('start'))
async def main_menu(message: Message) -> None:
    await message.answer(text='Hello!', reply_markup=default_kb)

# Хэндлер для отправки пользователю стартового меню
@dp.message_handler(Text('Главное меню'))
async def back_to_main_menu(message: Message) -> None:
    await message.answer(text='Вернулись в главное меню', reply_markup=default_kb)

# Хэндлер для отправки пользователю стартового меню
@dp.callback_query_handler(Text('Главное меню'))
async def back_to_main_men(callback: CallbackQuery) -> None:
    await callback.answer('Выбран возврат в главное меню')
    await bot.send_message(chat_id=callback.from_user.id, text='f', reply_markup=default_kb)
    
# Хэндлер для отправки пользователю списка категорий товаров
@dp.message_handler(Text(equals=['Сделать заказ', 'Назад к категориям']))
async def category_menu(message: Message) -> None:
    categorys = get_sql_response('''SELECT category_name 
                                      FROM category''')
    optional_buttons = _get_reply_buttons([('Главное меню',)], 0)
    category_keyboard = get_reply_keyboard(list=categorys, cols_num=2, optional_buttons=optional_buttons, opt_buttons_cols_num=2)
    if message.text == 'Сделать заказ':
        text = 'Открываю категории'
    else:
        text = 'Вернулись к Категориям'
    await message.answer(text=text, reply_markup=category_keyboard)

# Хэндлер для отправка пользователю списка подкатегорий из выбранной категории
@dp.message_handler(Text(equals=[elem[0] for elem in get_sql_response('SELECT category_name FROM category')]))
async def subcategory_menu(message: Message) -> None:
    subcategorys = get_sql_response(f'''SELECT subcategory_name, category_name
                                          FROM subcategory
                                         WHERE category_name = "{message.text}"''')
    optional_buttons = _get_reply_buttons([('Назад к категориям',), ('Главное меню',)], 0)
    subcategory_keyboard = get_reply_keyboard(list=subcategorys, cols_num=2, optional_buttons=optional_buttons, opt_buttons_cols_num=2)
    text = f'Открываю {message.text}'
    await message.answer(text=text, reply_markup=subcategory_keyboard)

# Хэндлер для отправка пользователю списка подкатегорий из выбранной категории
@dp.message_handler(Text(equals=[f'Назад к {elem[0]}' for elem in get_sql_response('SELECT category_name FROM category')]))
async def back_to_subcategory_menu(message: Message) -> None:
    category = re.sub('Назад к ', '', message.text)
    subcategorys = get_sql_response(f'''SELECT subcategory_name
                                          FROM subcategory
                                         WHERE category_name = "{category}"''')
    optional_buttons = _get_reply_buttons([('Назад к категориям',), ('Главное меню',)], 0)
    subcategory_keyboard = get_reply_keyboard(list=subcategorys, cols_num=2, optional_buttons=optional_buttons, opt_buttons_cols_num=2)
    text = f'Вернулись к {category}'
    await message.answer(text=text, reply_markup=subcategory_keyboard)
    
# Хэндлер для отправки пользователю списка товаров из выбранной подкатегории
@dp.message_handler(Text(equals=[elem[0] for elem in get_sql_response('SELECT subcategory_name FROM subcategory')]))
async def product_menu(message: Message) -> None:
    products = get_sql_response(f'''SELECT product_name, category_name
                                      FROM product
                                      JOIN subcategory ON product.subcategory_name = subcategory.subcategory_name
                                     WHERE product.subcategory_name = "{message.text}"''')
    optional_buttons = _get_reply_buttons([(f'Назад к {products[0][1]}',), ('Главное меню',)], 0)
    subcategory_keyboard = get_reply_keyboard(list=products, cols_num=2, optional_buttons=optional_buttons, opt_buttons_cols_num=2)
    await message.answer(text=message.text, reply_markup=subcategory_keyboard)

# Хэндлер для отправки пользователю карточки товара
@dp.message_handler(Text(equals=[elem[0] for elem in get_sql_response('SELECT product_name FROM product')]))
async def product_card(message: Message) -> None:
    bytes_photo = get_sql_response(f'''SELECT product_photo FROM product
                                        WHERE product_name = "{message.text}"''')[0][0]
    product_description = get_sql_response(f'''SELECT product_description FROM product
                                               WHERE product_name = "{message.text}"''')[0][0]
    prices = get_sql_response(f'''SELECT product_name || " " || product_size_name || "\n Цена: " || product_price || " руб" FROM price
                                  WHERE product_name = "{message.text}"''')
    optional_buttons = _get_inline_buttons([('Главное меню',)], 0, 0)
    price_keyboard = get_inline_keyboard(list=prices, cols_num=1, optional_buttons=optional_buttons)
    await bot.send_photo(chat_id=message.from_user.id, photo=bytes_photo, 
                         reply_markup=price_keyboard, caption=product_description)
