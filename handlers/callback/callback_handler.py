from main import *
from aiogram import types


@dp.callback_query_handler(lambda c: c.data == 'stop_activ')
async def process_callback_button_stop_activ(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text="сейчас Остановим/Запустим")


@dp.callback_query_handler(lambda call: 'announcement_' in call.data)
async def approve_announcement(call: types.CallbackQuery):
    db.confirm_announcements(call.data.split('_')[-1])
    await call.message.edit_text(text="Апрув")


@dp.callback_query_handler(lambda call: 'start_stop_' in call.data)
async def approve_start_end_my_resume(call: types.CallbackQuery):
    db.update__my_resume(call.data.split('_')[-1], not db.start_my_resume(call.data.split('_')[-1]))
    await call.message.edit_text(text="Апрув")


@dp.callback_query_handler(lambda call: 'confirm_resume_' in call.data)
async def approve_start_end_my_resume(call: types.CallbackQuery):
    db.confirm_my_resume(call.data.split('_')[-1])
    await call.message.edit_text(text="Апрув резюме")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def approve_announcement_user(call: types.CallbackQuery):
    db.update_announcements(call.data.split('_')[-1], not db.check_announcements(call.data.split('_')[-1]))
    await call.message.edit_text(text="Апрув")
