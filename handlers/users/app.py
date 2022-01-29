from main import *
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils import funk_async
from keyboards.default.markup import keyboard, keyboard_admin
from utils.privacy import privacy
from filters import IsAdmin


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_subscriber(message.from_user.id):
        db.add_subscriber(message.from_user.id)
    await message.answer(f'Привет, быстрее начни мной пользоваться!',
                         reply_markup=keyboard)

#admin hendler

@dp.message_handler(commands=['admin'])
async def command_start(message: types.Message):
    if not await IsAdmin().check(message):
        if not db.why_get_admin(message.from_user.id):
            db.get_admin(message.from_user.id, True)
            await message.answer('⚠️ Вход в админ режим ⚠️', reply_markup=keyboard_admin)
        else:
            db.get_admin(message.from_user.id, False)
            await message.answer('❌ Выход из админ режима ❌', reply_markup=keyboard)
    else:
        db.get_admin(message.from_user.id, False)
        await message.answer('❌ Вы не админ, команда не будет работать ❌', reply_markup=keyboard)


from keyboards.inline.keyboards import *


# async def all_resume(bot, message: types.Message):
#     data = {
#         True: get_all_resume_for_adm,
#         False: get_my_resume,
#     }
#     await data[await IsAdmin().check(message)](message)


async def get_all_resume_for_adm(bot, message: types.Message):
    if not db.get_resume_for_adm():
        await message.answer(f'❌ Нет резюме для апрува ‼️')
    else:
        for unp in db.get_resume_for_adm():
            id_resume, name, skills, area_of_residence, phone, allow, _, _, _ = unp
            await message.answer(
                f"👤 Имя: {name}\n🪛 Навыки: {skills}\n🌍 Район проживания: {area_of_residence}\n☎️ Номер телефона: {phone}",
                reply_markup=await get_confirm_admin_resume(id_resume))


#ОБьявления для апрува от админа

async def get_all_announcement_for_adm(bot, message: types.Message):
    if not db.get_announcement_for_adm():
        await message.answer(f'❌ Нет объявлений для апрува ‼️')
    else:
        for unp in db.get_announcement_for_adm():
            id, type_of_services, job_title, job_description, salary, phone, allow, _, _, _ = unp
            await message.answer(f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\n💰 Заработная Плата: {salary}\n☎️ Номер телефона: {phone}",
                                   reply_markup=await get_confirm_announcement_admin(id))


data_admin = {
            'Объявления для Верификации': get_all_announcement_for_adm,
            'Резюме для Верификации': get_all_resume_for_adm,
        }









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
        'Все Резюме': funk_async.get_all_resume,
        'Конфиденциальность': send_privacy,
    }
    await data.get(message.text, error)(bot, message)
    await data_admin.get(message.text, error)(bot, message)
