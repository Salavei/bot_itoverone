from main import *
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils import funk_async
from keyboards.default.markup import *
from utils.privacy import privacy
from filters import IsAdmin


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_subscriber(message.from_user.id):
        db.add_subscriber(message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(btnprivacy, btnoffers, btnannouncement, btnresume, btn_all_resume)
    await message.answer(f'Привет, {message.from_user.full_name}! Чтобы узнать правила использования введи /help',
                         reply_markup=keyboard)

#admin hendler

@dp.message_handler(commands=['admin'])
async def command_start(message: types.Message):
    if not await IsAdmin().check(message):
        db.get_admin(message.from_user.id, True)
        await message.answer('Вход в админ режим')
    else:
        db.get_admin(message.from_user.id, False)
        await message.answer('Выход из админ режима')

#########


async def error(bot, message):
    await message.delete()

async def send_privacy(bot, message):
    await message.answer(f'{privacy}')


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        'Список предложений': funk_async.all_my_announcement,
        'Мои обьявления': funk_async.my_announcement,
        'Мое Резюме': funk_async.my_resume,
        'Все Резюме': funk_async.all_resume,
        'Конфиденциальность': send_privacy,
    }
    await data.get(message.text, error)(bot, message)
