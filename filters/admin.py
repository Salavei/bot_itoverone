from aiogram.dispatcher.filters import Filter
from aiogram import types
from main import db, admin_id


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: types.Message):
        # return message.from_user.id in db.why_get_admin()
        return message.from_user.id != int(admin_id)
