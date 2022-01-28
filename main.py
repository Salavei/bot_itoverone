from utils.db_api.db_api import SQLighter
from aiogram import Bot, Dispatcher, executor
import logging
import environ
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = environ.Env()
environ.Env.read_env()

TOKEN = env('TOKEN')
logging.basicConfig(level=logging.INFO)
db = SQLighter(env('db'))

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

admin_id = env('admin_id')

if __name__ == '__main__':
    print('Start bot...')
    from handlers.users.app import dp
    from handlers.users.fsm import dp

    executor.start_polling(dp, skip_updates=True)
