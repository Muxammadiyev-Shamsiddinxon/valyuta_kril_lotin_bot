from loader import dp
from aiogram import types
from states.krilstate import Krilstate
from keyboards.default.menugaqaytish import menugaqaytish

# kril lotin kutubxonalari
from handlers.transliterate import to_cyrillic,to_latin




@dp.message_handler(state=Krilstate.krilstate)
async def imlo_bot(message: types.Message):
    xabar = message.text

    if xabar.isascii():
        javob = f"<code>{to_cyrillic(xabar)}</code>"
    else:
        javob = f"<code>{to_latin(xabar)}</code>"

    await message.reply(javob)


