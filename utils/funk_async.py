from aiogram import types
from keyboards.inline.keyboards import *
from keyboards.default.markup import *
from main import db, admin_id
from filters import IsAdmin
from handlers.admin.admin_handler import *


async def all_my_announcement(bot, message: types.Message):
    if not db.check_subscriber(message.from_user.id):
        db.add_subscriber(message.from_user.id)
        await bot.send_message(message.from_user.id, f'Добро пожаловать!!')
    elif not db.get_announcements_all():
        await bot.send_message(message.from_user.id, f'Объявлений нет!!')
    else:
        for unp in db.get_announcements_all():
            _, type_of_services, job_title, job_description, salary, phone, allow, _, _ = unp
            await bot.send_message(message.from_user.id,
                                   f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\nЗаработная Плата: {salary}\nНомер телефона: {salary}",
                                   )
        #reply_markup=await get_announce_edit() -- это будет для админа и только с апрувом


async def my_announcement(bot, message: types.Message):
    if len(db.get_announcements_my(message.from_user.id)) == 0:
        await bot.send_message(message.from_user.id, f'Нужно создать объявление', reply_markup=await get_announce_create())
    else:
        for unp in db.get_announcements_my(message.from_user.id):
            id, type_of_services, job_title, job_description, salary, phone, allow, _, _ = unp
            get_allow = {
                True: 'Остановить',
                False: 'Активировать',
            }
            await bot.send_message(message.from_user.id,
                                   f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\nЗаработная Плата: {salary}\nНомер телефона: {phone}",
                                   reply_markup=await get_announce_edit(id, get_allow[allow]))
        await bot.send_message(message.from_user.id, text='Создать обьявление:', reply_markup=await get_announce_create())


async def get_all_resume(bot, message: types.Message):
    if not db.get_resume_all():
        await message.answer( f'Резюме нет!!')
    else:
        for unp in db.get_resume_all():
            _, name, skills, area_of_residence, phone, _, _, _ = unp
            await message.answer(
                                   f"Имя: {name}\nНавыки: {skills}\nРайон проживания: {area_of_residence}\nНомер телефона: {phone}",
                                   reply_markup=button)


async def my_resume(bot, message: types.Message):
    if not db.get_resume_my(message.from_user.id):
        await bot.send_message(message.from_user.id, f'У вас нет резюме!!',reply_markup=await get_resumes_none())
    else:
        for unp in db.get_resume_my(message.from_user.id):
            id_resume, name, skills, area_of_residence, phone, allow, _, _ = unp
            get_allow = {
                True: 'Остановить',
                False: 'Активировать',
            }
            await bot.send_message(message.from_user.id,
                                   f"Имя: {name}\nНавыки: {skills}\nРайон проживания: {area_of_residence}\nНомер телефона: {phone}",
                                   reply_markup=await get_resumes_edit_keyboard(get_allow[allow], id_resume))




