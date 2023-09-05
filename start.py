# Потрібні бібілотеки
import googletrans

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.language_reply_key import languages
from keyboards.inline.choiсes import dynamic_en_choice, dynamic_uk_choice, dynamic_it_choice, dynamic_inline_kb_uk, dynamic_inline_kb_it, dynamic_inline_kb_en

from loader import dp

translator = googletrans.Translator()

# Команда /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # Вибір мови
    await message.answer("Choose your language / Оберіть мову / Scegli la tua lingua 🗣", reply_markup=languages)


# Вибір англійською
@dp.message_handler(text="English")
async def english_language(message: types.Message):
    await message.answer(text=f"Hi, {message.from_user.full_name} 👋!")
    await message.answer(f'''This bot will help you find a movie🍿
Enjoy the using!''')
    await message.answer("Choose an action⤵️",
                        reply_markup=dynamic_en_choice())

# Вибір українською
@dp.message_handler(text="Українська")
async def ukrainian_language(message: types.Message):
    start_menu_uk = translator.translate(f'''This bot will help you find a movie🍿
Enjoy the using!''', src='en', dest='uk')
    choice_uk = translator.translate("Choose an action⤵️", src='en', dest='uk')
    await message.answer(text=f"Привіт, {message.from_user.full_name} 👋!")
    await message.answer(text=start_menu_uk.text)
    await message.answer(text=choice_uk.text, 
                        reply_markup=dynamic_uk_choice())

# Вибір італійською
@dp.message_handler(text="Italiano")
async def italian_language(message: types.Message):
    start_menu_it = translator.translate(f'''This bot will help you find a movie🍿
Enjoy the using!''', src='en', dest='it')
    choice_it = translator.translate("Choose an action⤵️", src='en', dest='it')
    await message.answer(text=f"Ciao, {message.from_user.full_name} 👋!")
    await message.answer(text=start_menu_it.text)
    await message.answer(text=choice_it.text, 
                        reply_markup=dynamic_it_choice())


# Вибір жанрів англійською
@dp.callback_query_handler(lambda call: "en" in call.data)
async def english_language_genre(call: types.CallbackQuery):
    await call.message.edit_text(text='Сhoose a movie genre🎭', 
                        reply_markup=dynamic_inline_kb_en())

# Вибір жанрів українською
@dp.callback_query_handler(lambda call: "uk" in call.data)
async def ukrainian_language_genre(call: types.CallbackQuery):
    await call.message.edit_text(text='Оберіть жанр фільму🎭', 
                        reply_markup=dynamic_inline_kb_uk())

# Вибір жанрів італійською
@dp.callback_query_handler(lambda call: "it" in call.data)
async def italian_language_genre(call: types.CallbackQuery):
    await call.message.edit_text(text='Seleziona un genere di film🎭', 
                        reply_markup=dynamic_inline_kb_it())