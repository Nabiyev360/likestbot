from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def channel_inline(unique_id, post_id='', lang='uz', likes=''):
    publish = "Ulashish"
    if lang == 'ru':
        publish = "Поделиться"
        follow = 'Подпишитесь на канал'

    channel_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"👍 {likes}", callback_data=f"like_{unique_id}")
            ],
            [
                InlineKeyboardButton(text=publish, url=f"https://telegram.me/share/url?url=%F0%9F%91%89%20https://t.me/yangihayot_hokimligi/{post_id}")
            ]
        ]
    )

    return channel_keyboard