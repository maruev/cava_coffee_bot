from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from main import dp, bot
from keyboards import default_kb, mock_inline_kb
from sql import sql_select, sql_insert
from utils import get_reply_keyboard, get_inline_keyboard, _get_reply_buttons
import re


# Хэндлер для отправки пользователю стартового меню
@dp.message_handler(Text(equals=('Главное меню', '/start')))
async def back_to_main_menu(message: Message) -> None:
    try:
        sql_insert(
            querry=f'''INSERT INTO user (tg_user_id, user_name) VALUES (?, ?)''',
            values=[message.from_user.id, message.from_user.first_name]
        )
    except Exception:
        print('Такой юзер уже есть в БД')
    text = 'Главное меню'
    await message.answer(text=text, reply_markup=default_kb)

# Хэндлер для отправки пользователю списка категорий товаров
@dp.message_handler(Text(equals=['Сделать заказ', 'Назад к категориям']))
async def category_menu(message: Message) -> None:
    select = sql_select(
        '''
        SELECT category_name 
          FROM category
        '''
    )
    opt_buttons = _get_reply_buttons(list=[('Главное меню',)])
    kb = get_reply_keyboard(
        list=select, 
        cols_num=2, 
        optional_buttons=opt_buttons, 
        opt_buttons_cols_num=2
    )
    text = message.text
    await message.answer(text=text, reply_markup=kb)

# Хэндлер для отправки/возврата списка подкатегорий из выбранной категории
@dp.message_handler(Text(equals=[f'Назад к {elem[0]}' for elem in sql_select('SELECT category_name FROM category')] + [elem[0] for elem in sql_select('SELECT category_name FROM category')]))
async def back_to_subcategory_menu(message: Message) -> None:
    category = re.sub('Назад к ', '', message.text)
    select = sql_select(
        f'''
        SELECT subcategory_name
          FROM subcategory
         WHERE category_name = "{category}"
        '''
    )
    opt_buttons_text = [('Назад к категориям',), ('Главное меню',)]
    opt_buttons = _get_reply_buttons(list=opt_buttons_text)
    kb = get_reply_keyboard(
        list=select, 
        cols_num=2, 
        optional_buttons=opt_buttons, 
        opt_buttons_cols_num=2
    )
    text = message.text
    await message.answer(text=text, reply_markup=kb)

# Хэндлер для отправки/возврата списка товаров из выбранной подкатегории
@dp.message_handler(Text(equals=
    [elem[0] for elem in sql_select(
        'SELECT subcategory_name FROM subcategory')] + 
    [f'Назад к {elem[0]}' for elem in sql_select(
        'SELECT subcategory_name FROM subcategory')]
))
async def product_menu(message: Message) -> None:
    subcategory = re.sub('Назад к ', '', message.text)
    products = sql_select(
        f'''
        SELECT product_name, category_name
          FROM product
          JOIN subcategory 
               ON product.subcategory_name = subcategory.subcategory_name
         WHERE product.subcategory_name = "{subcategory}"
        '''
    )
    opt_buttons_text = [(f'Назад к {products[0][1]}',), ('Главное меню',)]
    opt_buttons = _get_reply_buttons(list=opt_buttons_text)
    kb = get_reply_keyboard(
        list=products, 
        cols_num=3, 
        optional_buttons=opt_buttons, 
        opt_buttons_cols_num=2
    )
    await message.answer(text=message.text, reply_markup=kb)

# Хэндлер для отправки пользователю карточки товара
@dp.message_handler(Text(equals=[elem[0] for elem in sql_select('SELECT product_name FROM product')]))
async def product_card(message: Message) -> None:
    product_name = message.text
    product = sql_select(
        f'''
        SELECT product.product_name, 
               product_description, 
               product_photo, 
               product_size_name, 
               product_price,
               subcategory_name 
          FROM product JOIN price ON product.product_name = price.product_name
         WHERE product.product_name = "{product_name}"
        '''
    )

    buttons = [(f'Назад к {product[0][5]}',), ('Главное меню',),]
    back_main_kb = get_reply_keyboard(list=buttons,buttons_text_index=0,)
    text = f'Открываю {product_name}'
    await message.answer(text=text, reply_markup=back_main_kb)

    photo = product[0][2]
    description = product[0][1]
    prices = [(f'{elem[0]} {elem[3]}: {elem[4]} руб.', ) for elem in product]
    kb = get_inline_keyboard(list=prices, cols_num=1)
    await bot.send_photo(
        chat_id=message.from_user.id, 
        photo=photo, 
        reply_markup=kb, 
        caption=description
    )

@dp.callback_query_handler(Text
    (equals=[f'{elem[0]} {elem[1]}: {elem[2]} руб.' for elem in sql_select(
        '''
        SELECT product.product_name, 
               product_size_name, 
               product_price 
          FROM product JOIN price 
               ON product.product_name = price.product_name
        ''')]))
async def adding_to_cart(call: CallbackQuery) -> None:
    await call.answer(cache_time=20)
    await call.message.edit_reply_markup(reply_markup=mock_inline_kb)

