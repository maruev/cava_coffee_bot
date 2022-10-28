from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command, Text
from main import dp, bot
from keyboards import default_kb, reply_back_main_buttons, inline_back_main_buttons
from sql import get_sql_response
from utils import get_reply_keyboard, get_inline_keyboard


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
@dp.message_handler(Text('Сделать заказ'))
async def category_menu(message: Message) -> None:
    categorys = get_sql_response('''SELECT category_name 
                                      FROM category''')
    category_keyboard = get_reply_keyboard(list=categorys, cols_num=2, optional_buttons=reply_back_main_buttons)
    await message.answer(text='Категории', reply_markup=category_keyboard)

# Хэндлер для отправка пользователю списка подкатегорий из выбранной категории
@dp.message_handler(Text(equals=[elem[0] for elem in get_sql_response('SELECT category_name FROM category')]))
async def subcategory_menu(message: Message) -> None:
    subcategorys = get_sql_response(f'''SELECT subcategory_name
                                          FROM subcategory
                                         WHERE category_name = "{message.text}"''')
    subcategory_keyboard = get_reply_keyboard(list=subcategorys, cols_num=2, optional_buttons=reply_back_main_buttons)
    await message.answer(text=message.text, reply_markup=subcategory_keyboard)

# Хэндлер для отправки пользователю списка товаров из выбранной подкатегории
@dp.message_handler(Text(equals=[elem[0] for elem in get_sql_response('SELECT subcategory_name FROM subcategory')]))
async def product_menu(message: Message) -> None:
    products = get_sql_response(f'''SELECT product_name
                                      FROM product
                                     WHERE subcategory_name = "{message.text}"''')
    subcategory_keyboard = get_reply_keyboard(list=products, cols_num=2, optional_buttons=reply_back_main_buttons)
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
    price_keyboard = get_inline_keyboard(list=prices, cols_num=1, optional_buttons=inline_back_main_buttons)
    await bot.send_photo(chat_id=message.from_user.id, photo=bytes_photo, 
                         reply_markup=price_keyboard, caption=product_description)
