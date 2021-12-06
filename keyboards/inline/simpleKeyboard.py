from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def simple_inline(unique_id, likes = '', lang = 'uz'):
    follow = "Kanalga ulaning"
    publish = "Ulashish"
    
    if lang == 'ru':
        follow = 'Подпишитесь на канал'
        publish = "Поделиться"
        
    simple_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"👍 {likes}", url="https://t.me/asosiy_uzb")
            ],
            [
                InlineKeyboardButton(text = follow, url = "https://t.me/asosiy_uzb")
            ],
            [
                InlineKeyboardButton(text=publish, switch_inline_query=f"{unique_id}")
            ]
        ]
    )
    
    return simple_keyboard