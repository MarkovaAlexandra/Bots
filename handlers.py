
from loader import dp
from aiogram import types
from loader import bot



total = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    print(message)
    await message.answer(f'Приветики, {message.from_user.first_name}! '
                            'Игра "забери конфеты" ходим по очереди, берем от 1 до 28 конфет'
                            ' кто заберет последние - победил'
                            ' для установки первоначального количества конфет набери команду /set число(через пробел)')

@dp.message_handler(commands=['set'])

async def mes_set(message: types.Message):
    while True:
        global total
        count = message.text.split()[1]
        try:
            total = abs(int(count))
            # break
            await message.answer(f'Установили новое количество конфет = {total} Сколько берешь? Введи число от 1 до 28' )
            break
        except:
            ValueError
            await bot.send_message(message.from_user.id, ' команда /set пробел число  ')
            break
    # await message.answer(f'Установили новое количество конфет - {total} Сколько берешь? Введи число от 1 до 28' )

    

@dp.message_handler(text = 'дурак')
async def mes_sensored(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Не выражайся')




@dp.message_handler()
async def mes_all(message: types.Message):
    global total
  
    if message.text.isdigit():
   
        while True:
            try_candies_player = int(message.text)
            if 0 < try_candies_player < 29 and try_candies_player <=total:
                candies_player = try_candies_player
                break
            else:
                await bot.send_message(message.from_user.id, f'от 1 до 28 плиз, но не больше, чем осталось ({total})')
                break
                


        total -= candies_player
        await bot.send_message(message.from_user.id, f' Конфет на столе осталось {total}')
        if total == 0:
            await bot.send_message(message.from_user.id, f'ты победил')
            
            
        else:
            candies_bot = total % 29
            if candies_bot == 0:
                candies_bot = total % 28
            total -= candies_bot
            await bot.send_message(message.from_user.id, f'Я беру {candies_bot}, осталось {total}')
            if total == 0:
                await bot.send_message(message.from_user.id, f'я победил')
            
                
    else:
        await bot.send_message(message.from_user.id, f' я умею только играть в конфеты, '
        f'если хочешь продолжить - введи количество конфет, которое берешь (сейчас на столе {total})'
         
        ' Если хочешь начать сначала - установи начальное количество кофет (команда /set пробел число) ')



    # await message.answer(f'Гляди, че поймал - {message.text}')