from aiogram.types import CallbackQuery
from data.config import CHANNELS

from loader import dp
from utils.db_api.dbxl import likeup_photo, get_language
from keyboards.inline.channelKeyboard import channel_inline

@dp.callback_query_handler(text_contains = 'like')
async def like_upper(call: CallbackQuery):
    info = dp.bot.get_current()
    member = await info.get_chat_member(chat_id =CHANNELS[0], user_id=call.from_user.id)
    
    try:
        # unique_id = call.message.photo[0].file_unique_id
        unique_id = call.message.reply_markup.inline_keyboard[0][0].callback_data[5:]
    except:
        unique_id = call.data[5:]
        # print(unique_id)
    
    if member.is_chat_member():
        # print(call)
        user_id = call.from_user.id
        # print(user_id)
        
        # if not in database
        likes = likeup_photo(unique_id, user_id)
        
        if likes == 0:
            likes = ''
            
        try:
            await call.message.edit_reply_markup(reply_markup=channel_inline(unique_id, likes, lang=get_language(unique_id)))
            await call.answer("+👍")
        except Exception as ex:
            text = "Siz ovoz bergansiz!"
            if get_language(unique_id) == 'ru':
                text = "Вы уже проголосовали!"
            await call.answer(text, show_alert=True)
    else:
        text = "Ovoz berish uchun kanalga obuna bo'ling!"
        if get_language(unique_id) == 'ru':
            text = "Вы должны подписаться на канал, чтобы проголосовать."
        await call.answer(text, show_alert=True)