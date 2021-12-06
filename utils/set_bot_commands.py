from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("uz", "O'zbek tili"),
            types.BotCommand("ru", "Русский")
        ]
    )
