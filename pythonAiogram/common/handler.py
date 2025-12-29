from random import randint
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from sqlalchemy import text, Column, Connection, MetaData, Table, Integer, String, Engine, create_engine, BigInteger
from common.keyboards import inl, inline_times, times, buy_kb, intsr
import aiosqlite
import random
from datetime import timedelta, datetime


handler_router = Router()


key = random.randint(0, 9_223_372_036_854_775_807)

@handler_router.message(CommandStart())
async def start_cmd(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    photo_path = r'C:\Users\SKM\Documents\Bandicam\photo_2025-12-02_20-31-10.jpg'
    text = f'''Привет! 👋 Добро пожаловать на KUR VPN! 🚀
Хотите защиту в интернете? 🛡️
Или скорость без ограничений? ⚡
У нас есть всё, чтобы вы были онлайн безопасно и быстро! 😎
'''

    await message.answer_photo(
        photo=types.FSInputFile(
            path=photo_path
        ),
        caption=text,
        reply_markup=inl
    )

@handler_router.callback_query(F.data == 'buyvpn')
async def traffic(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Отлично! Выберите тариф, чтобы продолжить: 📦', reply_markup=await inline_times())
@handler_router.callback_query(F.data.startswith("time_"))
async def time_choice(callback: CallbackQuery):
    # Находим выбранный тариф
    chosen = next(t for t in times if t["id"] == callback.data)
    # Получаем клавиатуру с кнопкой "Оплатить"
    keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Оплатить', callback_data='pay')], [InlineKeyboardButton(text='⬅Назад', callback_data='back')]])
    # Меняем сообщение
    await callback.message.edit_text(
        f'''Вы выбрали тариф: {chosen['label'][0:2]} мес. 🗓️
Для продолжения нажмите кнопку ниже, чтобы оплатить 💳''',
        reply_markup=keyb)



@handler_router.callback_query(F.data == 'my_prof_vpn')
async def my_vpn(callback: CallbackQuery):
    keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅Назад', callback_data='main_menu')]])
    async with aiosqlite.connect('datesql.db') as db:
        cur = await db.execute('SELECT date_time FROM user_date')
        res = await cur.fetchone()
    await callback.answer('')
    await callback.message.answer(f'⏳ Действует до: {''.join(res)}\n🔑 Ключ доступа:\n<pre>{key}</pre>\n❗️Просто нажмите на ключ один раз, чтобы скопировать его и начать пользоваться',
                                  parse_mode=ParseMode.HTML, reply_markup=keyb)


@handler_router.callback_query(F.data =='instructions')
async def instr(callback: CallbackQuery):
    await callback.message.answer('Выерите устройство: ', reply_markup=intsr)







@handler_router.callback_query(F.data == 'back')
async def back_ck(callback: CallbackQuery):
    await callback.message.edit_text('Отлично! Выберите тариф, чтобы продолжить: 📦', reply_markup=await inline_times())


@handler_router.callback_query(F.data == 'main_menu')
async def back(callback: CallbackQuery):
    photo_path = r'C:\Users\SKM\Documents\Bandicam\photo_2025-12-02_20-31-10.jpg'
    text = f'''Привет! 👋 Добро пожаловать на KUR VPN! 🚀
Хотите защиту в интернете? 🛡️
Или скорость без ограничений? ⚡
У нас есть всё, чтобы вы были онлайн безопасно и быстро! 😎
'''

    await callback.message.answer_photo(
        photo=types.FSInputFile(
            path=photo_path
        ),
        caption=text,
        reply_markup=inl)


@handler_router.message(Command('cancel'))
async def cancel(message: Message):
    photo_path = r'C:\Users\SKM\Documents\Bandicam\photo_2025-12-02_20-31-10.jpg'
    text = 'Вы вернулись в главное меню'
    await message.answer_photo(photo=types.FSInputFile(
            path=photo_path
        ),
        caption=text,
        reply_markup=inl)
