from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def channel_inline(unique_id, likes = '', lang = 'uz'):
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
                InlineKeyboardButton(text=publish, url="tg://msg/url?url=https://t.me/asosiy_uzb/")
            ]
        ]
    )
    
    return channel_keyboard