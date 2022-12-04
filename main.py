from aiogram import types, executor, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from func import get_first_receipts, write_to_json
from keyboards import kb, kb_receipt
from config import TOKEN
import json

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

receipts = []
temp = iter(receipts)
latest_url = "0"


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(text="Привет! Я бот - кулинарная книга! \n ", reply_markup=kb)
    write_to_json(name=message.from_user.username, url=[])


@dp.message_handler(Text(equals="Функционал"))
async def process_help_command(message: types.Message):
    await message.answer(text="Напиши мне название блюда или ингредиенты и получишь ссылку на рецепт! \n"
                              "Ты также можешь добавить понравившиеся рецепты в свою кулинаруную книгу!",
                         reply_markup=kb)


@dp.message_handler(Text(equals='Следующий рецепт'))
async def process_next_command(message: types.Message):
    try:
        global latest_url
        latest_url = next(temp)
        await message.answer(text=latest_url, reply_markup=kb_receipt)
    except (RuntimeError, StopIteration):
        await message.answer(text='По вашему запросу закончились рецепты!', reply_markup=kb)


@dp.message_handler(Text(equals='Добавить в мою книгу'))
async def process_add_command(message: types.Message):
    global latest_url
    write_to_json(name=message.from_user.username, url=latest_url)
    await message.answer(text='Ваша книга обновлена!')

#
# @dp.message_handler(Text(equals='Отмена последнего действия'))
# async def process_delete_command(message: types.Message):
#     with open("user_books.json", 'w') as jf:
#         jf_file = json.load(jf)
#         jf_file[message.from_user.username].pop()
#         json.dump(jf_file, jf, indent=4)
#     await message.answer(text='Ваша книга обновлена!', reply_markup=kb_receipt)


@dp.message_handler(Text(equals='Моя кулинарная книга'))
async def process_book_command(message: types.Message):
    with open("user_books.json", 'r') as jfr:
        jf_file = json.load(jfr)
    for value in jf_file[message.from_user.username]:
        await message.answer(text=value)


@dp.message_handler()
async def text(msg: types.Message):
    url = "https://eda.ru/recipesearch?onlyEdaChecked=true&q=" + '%20'.join(msg.text.split())
    get_first_receipts(url)
    try:
        with open("receipts_dict.json", "r") as file:
            global receipts
            receipts = json.load(file)
            global temp
            temp = iter(receipts)
        global latest_url
        latest_url = next(temp)
        await msg.answer(text=latest_url, reply_markup=kb_receipt)
    except (RuntimeError, StopIteration):
        await msg.answer(text="Попробуйте ввести другие данные", reply_markup=kb_receipt)


if __name__ == '__main__':
    executor.start_polling(dp)
