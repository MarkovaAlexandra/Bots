from loader import dp
from aiogram.types import Message
from loader import bot
import game





@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    print(message)
    
    await bot.send_message(477720457,f' к чату присоединился {message.from_user.first_name}')
    # await dp.bot.send_message(477720457,f' к чату присоединился {message.from_user.first_name}')
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('играешь уже ж')
            break
    

    else:   
            await message.answer(f'Приветики, {message.from_user.first_name}! '
                            'Игра "забери конфеты" ходим по очереди, берем от 1 до 28 конфет'
                            ' кто заберет последние - победил'
                            ' для установки первоначального количества конфет набери команду /set число(через пробел)')
            my_game = [message.from_user.id, message.from_user.first_name, 150]
            game.total.append(my_game) 
            await mes_set(message)


@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    while True:
        candies = message.text.split()[1]
        try:
            candies = abs(int(candies))
            await message.answer(f'установили {candies} конфет \n'
                                'твой ход -  бери конфеты')
            break
        except:
            ValueError
            break

    for my_game in game.total:
        if message.from_user.id == my_game[0]:
            print('дошли  до установки конфет')
            my_game[2]=candies
