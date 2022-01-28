from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup()

inline_btn_edit = InlineKeyboardButton('Изменить', callback_data='edit')
inline_btn_stop_activ = InlineKeyboardButton('Остановить/Активировать', callback_data='stop_activ',)
inline_btn_edit_one = InlineKeyboardButton('Изменить(1)', callback_data='edit_one')
inline_btn_work = InlineKeyboardButton('Работа', callback_data='work')
inline_btn_so_work = InlineKeyboardButton('Подработка', callback_data='so_work')
inline_btn_create_one = InlineKeyboardButton('Создать', callback_data='create_one')
inline_btn_confirm = InlineKeyboardButton('Одобрить', callback_data='confirm')



async def get_announce_edit(id, allow) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'stop_start_an_{id}'),
            ]

        ]
    )
    return keyboard

async def get_announce_create() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('Создать', callback_data='create'),
            ]

        ]
    )
    return keyboard

async def get_resumes_edit_keyboard(start_stop_state,id_resume) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{start_stop_state}', callback_data=f'start_stop_{id_resume}',), #Остановить/Активировать
                InlineKeyboardButton('Изменить', callback_data='edit_one'),
             ]
        ]
    )
    return keyboard

async def get_resumes_none() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('Создать', callback_data='edit_one'),
             ]
        ]
    )
    return keyboard


async def get_announcement_admin() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('Одобрить', callback_data='confirm'),
             ]
        ]
    )
    return keyboard

async def get_announcement_admin_resume(id_resume) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('Одобрить', callback_data=f'confirm_resume_{id_resume}'),
             ]
        ]
    )
    return keyboard


async def add_announcement() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('Работа', callback_data='work'),
                InlineKeyboardButton('Подработка', callback_data='so_work'),
             ]
        ]
    )
    return keyboard


async def verifying_announcement(id_conf) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                # InlineKeyboardButton('Подтвердить', callback_data='verifying_ann'), #id_conf
                InlineKeyboardButton(text='Подтвердить', callback_data=f'announcement_{id_conf}', )
             ]
        ]
    )
    return keyboard

