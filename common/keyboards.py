from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder



inl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Купить/Продлить💳', callback_data='buyvpn')],
    [InlineKeyboardButton(text='Мой VPN📲', callback_data='my_prof_vpn')],
    [InlineKeyboardButton(text='Инструкция📖', callback_data='instructions')],
    [InlineKeyboardButton(text='Поддержка🛠️', callback_data='support', url='https://t.me/mdjabrailov')]

])

intsr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Android📱', callback_data='android')],
    [InlineKeyboardButton(text='IOS📱', callback_data='iphone')],
    [InlineKeyboardButton(text='Windows 💻', callback_data='wimdows')],
    [InlineKeyboardButton(text='macOS 💻', callback_data='macos')],
    [InlineKeyboardButton(text='TV 🖥', callback_data='tv')]
])


times = [
    {"label": "1 мес. - 149Р️", "id": "time_1"},
    {"label": "3 мес. - 299Р️", "id": "time_3"},
    {"label": "6 мес. - 649Р️", "id": "time_6"},
    {"label": "12 мес. - 999Р️", "id": "time_12"}

]

async def inline_times():
    keyboard = InlineKeyboardBuilder()
    for t in times:
        keyboard.button(text=t["label"], callback_data=t["id"])
    keyboard.button(text='⬅Назад', callback_data='main_menu')
    keyboard.adjust(2)  # 2 кнопки в ряду
    return keyboard.as_markup()



buy_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅Назад', callback_data='back')]
    ])

