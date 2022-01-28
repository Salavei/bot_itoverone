from aiogram import types
from keyboards.inline.keyboards import *
from keyboards.default.markup import *
from main import db, admin_id
from filters import IsAdmin
from handlers.admin.admin_handler import *


async def all_my_announcement(bot, message: types.Message):
    # если юзера нет в базе, добавляем его
    if not db.check_subscriber(message.from_user.id):
        db.add_subscriber(message.from_user.id)
        await bot.send_message(message.from_user.id, f'Добро пожаловать!!')
    elif not db.get_announcements_all():
        await bot.send_message(message.from_user.id, f'Объявлений нет!!')
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnprivacy,btnoffers,btnannouncement,btnresume,btn_all_resume)
        # all_announ = db.get_announcements_all()
        for unp in db.get_announcements_all():
            # unp = all_announ[i]
            _, type_of_services, job_title, job_description, salary, phone, allow, _, _ = unp
            await bot.send_message(message.from_user.id,
                                   f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\nЗаработная Плата: {salary}\nНомер телефона: {salary}",
                                   )
        #reply_markup=await get_announce_edit() -- это будет для админа и только с апрувом


async def my_announcement(bot, message: types.Message):
    if len(db.get_announcements_my(message.from_user.id)) == 0:
        await bot.send_message(message.from_user.id, f'Нужно создать объявление', reply_markup=await get_announce_edit())
    else:
        # my_announ = db.get_announcements_my(message.from_user.id)
        for unp in db.get_announcements_my(message.from_user.id):
            # unp = my_announ[i]
            id, type_of_services, job_title, job_description, salary, phone, allow, _, _ = unp
            get_allow = {
                True: 'Остановить',
                False: 'Активировать',
            }
            await bot.send_message(message.from_user.id,
                                   f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\nЗаработная Плата: {salary}\nНомер телефона: {phone}",
                                   reply_markup=await get_announce_edit(id, get_allow[allow]))
        await bot.send_message(message.from_user.id, text='Создать обьявление:', reply_markup=await get_announce_create())





async def get_all_resume_for_adm(message: types.Message):
    if not db.get_resume_for_adm():
        await message.answer(f'Нет резюме для апрува !!')
    else:
        # subscriptions = db.get_resume_for_adm()
        for unp in db.get_resume_for_adm():
            # unp = subscriptions[i]
            id_resume, name, skills, area_of_residence, phone, allow, _, _ = unp
            await message.answer(
                f"Имя: {name}\nНавыки: {skills}\nРайон проживания: {area_of_residence}\nНомер телефона: {phone}",
                reply_markup=await get_announcement_admin_resume(id_resume))
    await message.answer(text='Вы админ')


async def get_my_resume(message: types.Message):
    if not db.get_resume_all():
        await message.answer( f'Резюме нет!!')
    else:
        # subscriptions = db.get_resume_all()
        for unp in db.get_resume_all():
            # unp = subscriptions[i]
            _, name, skills, area_of_residence, phone, _, _, _ = unp
            await message.answer(
                                   f"Имя: {name}\nНавыки: {skills}\nРайон проживания: {area_of_residence}\nНомер телефона: {phone}",
                                   reply_markup=button)


async def my_resume(bot, message: types.Message):
    if not db.get_resume_my(message.from_user.id):
        await bot.send_message(message.from_user.id, f'У вас нет резюме!!',reply_markup=await get_resumes_none())
    else:
        # subscriptions = db.get_resume_my(message.from_user.id)
        for unp in db.get_resume_my(message.from_user.id):
            # unp = subscriptions[i]
            id_resume, name, skills, area_of_residence, phone, allow, _, _ = unp
            print(id_resume)
            get_allow = {
                True: 'Остановить',
                False: 'Активировать',
            }
            await bot.send_message(message.from_user.id,
                                   f"Имя: {name}\nНавыки: {skills}\nРайон проживания: {area_of_residence}\nНомер телефона: {phone}",
                                   reply_markup=await get_resumes_edit_keyboard(get_allow[allow], id_resume))


async def all_resume(bot, message: types.Message):
    data = {
        True: get_all_resume_for_adm,
        False: get_my_resume,
    }
    await data[await IsAdmin().check(message)](message)


