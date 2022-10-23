from config import BOT_TOKEN, admins_id
from aiogram import Bot, Dispatcher, executor

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


