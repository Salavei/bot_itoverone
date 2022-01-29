from aiogram.types import KeyboardButton
from aiogram import types
# main_user button #
btnprivacy = KeyboardButton('Конфиденциальность')
btnoffers = KeyboardButton('Список предложений')
btnannouncement = KeyboardButton('Мои обьявления')
btnresume = KeyboardButton('Мое Резюме')
btn_all_resume = KeyboardButton('Все Резюме')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(btnprivacy,btnoffers,btnannouncement,btnresume,btn_all_resume)

#admin button
admin_resume = KeyboardButton('Объявления для Верификации')
admin_announcement = KeyboardButton('Резюме для Верификации')

keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.add(admin_resume, admin_announcement)