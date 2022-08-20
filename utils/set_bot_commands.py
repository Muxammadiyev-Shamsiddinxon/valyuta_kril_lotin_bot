from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("admin", "admin komandalar")

        ]
    )
# bu buyruqlar </> shu belgini quyganda telegramda chiqadiku help,start,yana bir nimalar ushlarga qushib quyadi