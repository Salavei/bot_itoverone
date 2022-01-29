from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *
from keyboards.inline.keyboards import *
from handlers.callback.callback_handler import *


class FSMAannouncement(StatesGroup):
    type_of_services = State()
    job_title = State()
    job_description = State()
    salary = State()
    phone = State()
    print('Start объявления')


@dp.callback_query_handler(lambda c: c.data == 'create')
async def cm_start1(callback_query: types.CallbackQuery):
    await FSMAannouncement.type_of_services.set()
    await callback_query.message.edit_text('Выберите тип работы')
    await callback_query.message.edit_reply_markup(reply_markup=await add_announcement())


@dp.callback_query_handler(lambda call: "work" or "so_work" in call.data, state=FSMAannouncement.type_of_services)
async def choice_work_user(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'work': '👔 Работа',
        'so_work': '🦺 Подработка'
    }
    await state.update_data(type_of_services=choice[call.data])
    await FSMAannouncement.next()
    await call.message.edit_text(text="Введите название вакансии")


@dp.message_handler(state=FSMAannouncement.job_title)
async def load_job_title_invalid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job_title'] = message.text
    await FSMAannouncement.next()
    await message.answer('Введите описание вакансии')


@dp.message_handler(state=FSMAannouncement.job_description)
async def load_job_description(message: types.Message, state: FSMContext):
    if len(message.text) <= 55:
        async with state.proxy() as data:
            data['job_description'] = message.text
        await FSMAannouncement.next()
        await message.answer('💰 ЗП(подсказка: "20 в день, 10 в час, 600 за 21 день")')
    else:
        await message.answer('❌ Слишком большое описание.Не более 55 символов')


@dp.message_handler(state=FSMAannouncement.salary)
async def load_salary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['salary'] = message.text
    await FSMAannouncement.next()
    await message.answer('☎️ Номер телефона')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMAannouncement.phone)
async def load_phone_invalid(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMAannouncement.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements(data['type_of_services'], data['job_title'], data['job_description'], data['salary'],
                         data['phone'], user_id=message.from_user.id)
    await state.finish()


class FSMresume(StatesGroup):
    name = State()
    skills = State()
    area_of_residence = State()
    phone = State()
    print('Start Резюме')


@dp.callback_query_handler(lambda c: c.data == 'edit_one')
async def cm_start(callback_query: types.CallbackQuery):
    await FSMresume.name.set()
    await callback_query.message.edit_text(text="👤 Введите Ваше Имя:")


@dp.message_handler(state=FSMresume.name)
async def load_type_work(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMresume.next()
    await message.answer('🪛 Опишите Ваши навыки:')


@dp.message_handler(state=FSMresume.skills)
async def load_job_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['skills'] = message.text
    await FSMresume.next()
    await message.answer('🌍 Ваш район проживания:')


@dp.message_handler(state=FSMresume.area_of_residence)
async def load_job_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['area_of_residence'] = message.text
    await FSMresume.next()
    await message.answer('☎️ Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMresume)
async def load_phone_invalid(message: types):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMresume.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Резюме добавлено')
    data_d = {
        True: db.update_resume_my,
        False: db.add_resume
    }
    print(data)
    #TypeError: object sqlite3.Cursor can't be used in 'await' expression
    bool_db = bool(db.get_resume_my(message.from_user.id))
    await data_d[bool_db](data['name'], data['skills'], data['area_of_residence'],
                                                             data['phone'], user_id=message.from_user.id)
    await state.finish()
