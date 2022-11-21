from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import re
import png
import pyqrcode as pq
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

"""@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('Доброго дня ми з України!!!')

    else:
        await message.answer('Я Вас не розумію :(')"""

@dp.message_handler()
async def create_qrcode(message: types.Message):
    await message.answer('Enter url: ')
    url = re.match('https?://[\S]+', message.text)
    if url != None:
        qr_code = pq.create(message.text)
        qr_code.png('code.png', scale=6)

        with open('code.png', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)
            await bot.send_message(message.chat.id, 'you are welcome!')
    else:
        await message.answer('Введите коректный  URL')


executor.start_polling(dp, skip_updates=True)