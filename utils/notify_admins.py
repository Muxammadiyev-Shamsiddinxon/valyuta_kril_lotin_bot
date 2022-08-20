import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            xabar=f"<b>Boshliq bot ishga tushdi......⌛️⏳</b>"
            await dp.bot.send_message(admin, xabar)

        except Exception as err:
            logging.exception(err)
