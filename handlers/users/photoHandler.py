from aiogram.types import Message
from random import randint

from loader import dp
from data.config import CHANNELS
from utils.db_api.dbxl import add_photo, get_language, get_data
from keyboards.inline.simpleKeyboard import simple_inline
from keyboards.inline.channelKeyboard import channel_inline


@dp.message_handler(content_types=['photo'])
async def bot_start(message: Message):
    # print(message)
    photo_id = message.photo[0].file_id
    unique_id = message.photo[0].file_unique_id + str(randint(1, 1000))
    lang = get_data("A1")
    
    add_photo(photo_id, unique_id, lang)
    caption = message.caption
    
    await message.answer_photo(
        photo=photo_id,
        caption = caption,
        reply_markup=simple_inline(unique_id, likes='', lang = get_language(unique_id))
    )
    
    info = dp.bot.get_current()
    member = await info.get_chat_member(chat_id = CHANNELS[0]  , user_id=message.from_user.id)
    
    if member.is_chat_admin():
        await dp.bot.send_photo(
            chat_id=CHANNELS[0], 
            photo=photo_id, 
            caption = caption,
            reply_markup=channel_inline(unique_id, likes='', lang = get_language(unique_id))
        )