from main import *
from aiogram import types


@dp.callback_query_handler(lambda c: c.data == 'stop_activ')
async def process_callback_button_stop_activ(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text="сейчас Остановим/Запустим")


@dp.callback_query_handler(lambda call: 'start_stop_' in call.data)
async def approve_start_end_my_resume(call: types.CallbackQuery):
    db.update__my_resume(call.data.split('_')[-1], not db.start_my_resume(call.data.split('_')[-1]))
    await call.message.edit_text(text="Апрув 2")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def approve_announcement_user(call: types.CallbackQuery):
    db.update_announcements(call.data.split('_')[-1], not db.check_announcements(call.data.split('_')[-1]))
    await call.message.edit_text(text="Апрув 1")


# ADMIN CALLBACK
@dp.callback_query_handler(lambda call: 'confirm_r_admin_' in call.data)
async def approve_resume_admin(call: types.CallbackQuery):
    db.confirm_resume_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Апрув резюме")


@dp.callback_query_handler(lambda call: 'reject_r_admin_' in call.data)
async def reject_resume_admin(call: types.CallbackQuery):
    db.reject_db_resume_admin(call.data.split('_')[-1])
    await call.message.edit_text(text='Резюме откланено')

@dp.callback_query_handler(lambda call: 'confirm_a_admin_' in call.data)
async def approve_announcement_admin(call: types.CallbackQuery):
    db.confirm_announcements_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Апрув объявления")


@dp.callback_query_handler(lambda call: 'reject_a_admin_' in call.data)
async def reject_announcement_admin(call: types.CallbackQuery):
    db.reject_db_announcement_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Объявление откланено")