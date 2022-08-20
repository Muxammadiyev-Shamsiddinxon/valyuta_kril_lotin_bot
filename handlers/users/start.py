import datetime as dt
from time import strftime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

from keyboards.default.menuKeyboard import Menu
from keyboards.default.menugaqaytish import menugaqaytish
from loader import dp,  bot



# Kursni aniqlovchi kutubxonalarni chaqirish
import math
import requests



# KURSNI ANIQLASH UCHUN KOD
kod =  'bfb4ae90a65e63cc7a717986'  #API dan olgan kodim ExchangeRate-API

davlat_ru='RUB' #AQSH USD, ROSIYA RUB, UZB UZS,
davlat_aqsh='USD'



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.full_name

#await bot.send_message(chat_id=ADMINS[0], text=err)
#bitta tepada #quyilgan xatolikni kursatmaydi ..UNIQUE constraint failed: Users.id.. shuni kursatadi agar # olib tashlasak

    javob = f"Assalom Alaykum <b>...{message.from_user.first_name}...</b> Xush kelibsiz! \nKril-Lotin ,"
    javob += "Lotin-Kril botman😎😎. \nBo'lim tanlang:   "

    await message.reply(javob,reply_markup=Menu)

    # Adminga xabar beramiz
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{message.from_user.username}</b>\n "
    msg += f"<b>{message.from_user.full_name}</b>\n"
    msg += f" <b>{message.from_user.id}</b>\n\n"

    await bot.send_message(chat_id="5280188027", text=msg,reply_markup=Menu)


@dp.message_handler(CommandHelp())
async def bot_start(message: types.Message):
    text = "Botdan foydalanish uchun bo'limlarni tanlang"
    await message.reply(text,reply_markup=Menu)


@dp.message_handler(text="Krill-Lotin, Lotin-Krill ⌛️⏳")
async def send_link(message: types.Message):
    await message.answer("So'z yuboring ",reply_markup=menugaqaytish)



@dp.message_handler(text="Valyuta Kursi")
async def send_link(message: types.Message):


    # url ga murojat qilib Kursni aniqlash.

    url_aqsh = f"https://v6.exchangerate-api.com/v6/{kod}/pair/{davlat_aqsh}/UZS"
    url_ru = f"https://v6.exchangerate-api.com/v6/{kod}/pair/{davlat_ru}/UZS"

    javob_aqsh = requests.get(url_aqsh)  # Saytdan qaytgan javob <requests> taminlayapmiz
    javob_ru = requests.get(url_ru)  # Saytdan qaytgan javob <requests> taminlayapmiz

    kurs_aqsh = javob_aqsh.json()
    kurs_ru = javob_ru.json()

    kurs_aqsh = kurs_aqsh['conversion_rate']
    kurs_ru = kurs_ru['conversion_rate']


    # sana va vaqtni aniqlash
    hozir=dt.datetime.now()
    sana=hozir.date()
    soat=strftime("%H:%M:%S")


    javob =f"<b>Valyuta Kurslari.</b>\n\n📅  {sana} \n\n🕔  {soat}  "
    javob += f"\n\n<b>1-Aqsh dollar  = {math.ceil(kurs_aqsh)} so'm</b>"
    javob += f"\n<b>1-Russian ruble  = {math.ceil(kurs_ru)} so'm</b>"

    await message.answer(javob, reply_markup=menugaqaytish)






@dp.message_handler(text="◀️Ortga")
async def send_link(message: types.Message):
    await message.answer("Asosiy menu ",reply_markup=Menu)

