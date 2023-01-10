from aiogram.types import CallbackQuery
from data.config import CHANNELS

from loader import dp, db
# from utils.db_api.dbxl import likeup_photo, get_language
from keyboards.inline.channelKeyboard import channel_inline

@dp.callback_query_handler(text_contains='like')
async def like_upper(call: CallbackQuery):
    user_id = call.from_user.id
    channel_id = CHANNELS[0]
    post_id = call.message.message_id

    info = dp.bot.get_current()
    member = await info.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)

    try:
        unique_id = call.message.reply_markup.inline_keyboard[0][0].callback_data[5:]
    except:
        unique_id = call.data[5:]

    # db dan like bosilgan post haqidagi ma'lumotlarni olamiz
    post_data = db.get_post(unique_id)
    post_lang = post_data[0]
    if member.is_chat_member():
        liked_users = post_data[5]

        if str(user_id) in liked_users:
            if post_lang == 'ru':
                text = "Вы уже проголосовали!"
            else:
                text = "Siz ovoz bergansiz!"
            await call.answer(text, show_alert=True)

        else:
            db.uplike(unique_id, user_id)
            like_count = post_data[4] + 1

            try:
                await call.message.edit_reply_markup(
                    reply_markup=channel_inline(
                        unique_id=unique_id,
                        post_id=post_id,
                        lang=post_lang,
                        likes=like_count))
                await call.answer("+👍")

            except Exception as ex:
                text = "Siz ovoz bergansiz!"
                if post_lang == 'ru':
                    text = "Вы уже проголосовали!"
                await call.answer(text, show_alert=True)
                print(ex)

        # Add post_link to db
        post_link = post_data[6]

        if post_link[-1] != '/':
            db.add_post_link(unique_id, "https://t.me/" + 'yangihayot_hokimligi' + '/' + str(post_id) + '/')

    else:
        text = "Ovoz berish uchun kanalga obuna bo'ling!"
        if post_lang == 'ru':
            text = "Вы должны подписаться на канал, чтобы проголосовать!"
        await call.answer(text, show_alert=True)
