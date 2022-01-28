# import aiogram
# from aiogram import types
# from main import bot, db
# from keyboards.inline.keyboards import verifying_announcement
# async def verifying_announcements(bot, message: types.Message):
#     admin_announ = db.get_admin_announcements_all()
#     print(admin_announ)
#     for i in range(len(admin_announ)):
#         unp = admin_announ[i]
#         _, type_of_services, job_title, job_description, salary, phone, allow, _, _ = unp
#         await bot.send_message(message.from_user.id, f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\nЗаработная Плата: {salary}\nНомер телефона: {salary}",
#                            reply_markup=await verifying_announcement())
