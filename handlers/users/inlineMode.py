from aiogram import types

from loader import dp, db
from keyboards.inline.simpleKeyboard import simple_inline

@dp.inline_handler()
async def share(query: types.InlineQuery):
    unique_id = query.query
    post = db.get_post(unique_id)
    photo_id = post[1]
    likes = post[4]
    caption = post(3)
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