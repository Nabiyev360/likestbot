from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.dbxl import set_language

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nPost tagiga like qo'yish uchun avval postni yuboring💁‍♂️")
    
    
@dp.message_handler(commands=['uz'])
async def set_lang(message: types.message):
    set_language('uz')
    await message.reply("🇺🇿 O'zbek tili tanlandi!")


@dp.message_handler(commands=['ru'])
async def set_lang(message: types.message):
    set_language('ru')
    await message.reply("🇷🇺 Rus tili tanlandi!")    