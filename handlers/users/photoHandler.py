from aiogram.types import Message
from random import randint

from loader import dp, db
from data.config import CHANNELS
# from utils.db_api.dbxl import add_photo, get_language, get_data
from keyboards.inline.simpleKeyboard import simple_inline
from keyboards.inline.channelKeyboard import channel_inline


@dp.message_handler(content_types=['photo'])
async def bot_start(message: Message):
    photo_id = message.photo[0].file_id
    unique_id = message.photo[0].file_unique_id + str(randint(1, 1000))
    lang = 'uz'

    caption = message.caption
    caption_ens = message.caption_entities

    db.add_post(post_lang=lang, file_id=photo_id, unique_id=unique_id, caption=caption, post_link="https://t.me/yangihayot_hokimligi")

    
    await message.answer_photo(
        photo=photo_id,
        caption = caption,
        caption_entities=caption_ens,
        reply_markup=simple_inline(unique_id, likes='', lang = db.get_language(unique_id))
    )
    
    info = dp.bot.get_current()
    member = await info.get_chat_member(chat_id=CHANNELS[0], user_id=message.from_user.id)
    
    if member.is_chat_admin():
        await dp.bot.send_photo(
            chat_id=CHANNELS[0], 
            photo=photo_id, 
            caption = caption,
            caption_entities=caption_ens,
            reply_markup=channel_inline(unique_id, likes='', lang=db.get_language(unique_id))
        )