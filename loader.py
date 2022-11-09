#ключевые переменные бота

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = '5474401021:AAFI1diUOVapRBd7qw6TNDl4k1ggdSQ4hnk'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)