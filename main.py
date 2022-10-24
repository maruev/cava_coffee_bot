from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    from utils import bot_start_notif

    print('Bot started')
    executor.start_polling(dp, on_startup=bot_start_notif)
