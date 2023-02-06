from loader import dp
from aiogram.types import Message
import game
import random

@dp.message_handler()
async def take(message: Message):
        for duel in game.total:
            if message.from_user.id == duel[0]:

                count = message.text
                name = duel[1]
                if count.isdigit() and 0 < int(count) < 29:
                    duel[2] -= int(count)
                    # if await check_win(message, 'Ты',duel):
                    #     return True
                    
                    await message.answer(f'{name} взял {count} конфет, на столе осталось {duel[2]}\n')
                                            
                    if await check_win(message, 'Ты',duel):
                        return True
                    

                    bot_take = duel[2] % 29 if duel[2] > 28 else duel[2]
                    if bot_take == 0:
                        bot_take = random.randint(1,duel[2])
                    duel[2] -= bot_take
                    # if await check_win(message, 'Бот', duel):
                    #     return True
                    await message.answer(f' Бот взял {bot_take} конфет, на столе осталось {duel[2]}\n')
                                            
                    if await check_win(message, 'Бот', duel):
                        return True

                else:
                    await message.answer('Введи число от 1 до 28 ')

async def check_win(message: Message, win: str, total: list):
    if total[2] <= 0:
        await message.answer(f' {win} победил. \n'
                            f'Для игры сначал набери команду /start')
      
        game.total.remove(total)
        return True
    return False