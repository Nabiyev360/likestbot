from aiogram import types

from loader import dp
from keyboards.inline.simpleKeyboard import simple_inline
from utils.db_api.dbxl import get_like, get_photo, get_caption

@dp.inline_handler()
async def share(query: types.InlineQuery):
    unique_id = query.query
    photo_id = get_photo(unique_id)
    likes = get_like(unique_id) 
    caption = get_caption(unique_id)
    if likes == 0:
        likes = ''
        
    await query.answer(
    results=[
            types.InlineQueryResultPhoto(
                id=unique_id,
                photo_url=photo_id,
                thumb_url="https://ibb.co/vwrTKHn",
                caption=caption,
                reply_markup=simple_inline(unique_id, likes)
            ),
        ]
    )