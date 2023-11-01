import discord
import datetime
import time

from discord.ext import commands
from discord.ext import tasks
from itertools import cycle


# 현재 상태를 저장하는 클래스 
class State:
    def __init__(self):
        self.state = "아직몰라"

    def set_state(self, newState):
        self.state = newState

    def get_state(self):
        return self.state

    
bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
Croquis_timer = 0
playing = ['크로키모드', '집중모드']
Bot_State = State()

'''
@tasks.loop(seconds=1)
async def morning_cheer():
    if datetime.datetime.now().hour == 7 and datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
        await bot.get_channel(1097759845077225565).send("오늘도 화이팅!")
        # 1초 sleep하여 중복 전송 방지
        time.sleep(1)

@tasks.loop(hours=1)
async def night_cheer():
    if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
        await bot.get_channel(1097759845077225565).send("내일도 화이팅!")
        # 1초 sleep하여 중복 전송 방지
        time.sleep(1)
'''


@tasks.loop(seconds=20)
async def Mode_Concentration():
    #await bot.get_channel(1097759845077225565).send(Bot_State.get_state())

    if Bot_State.get_state() == "집중모드":
        if datetime.datetime.now().minute == 55:
            await bot.get_channel(1097759845077225565).send("휴식")
        elif datetime.datetime.now().minute == 0:
            await bot.get_channel(1097759845077225565).send("집중")
    elif Bot_State.get_state() == "크로키모드":
        await bot.get_channel(1097759845077225565).send(Bot_State.get_state())


@bot.command()
async def 크로키모드(message):
    await bot.change_presence(activity = discord.Game("크로키모드"))


    Bot_State.set_state("크로키모드")
    if Bot_State.get_state() == "크로키모드":
        await message.channel.send(Bot_State.get_state())

@bot.command()
async def 집중모드(message):
    await bot.change_presence(activity = discord.Game("집중모드"))

    
    Bot_State.set_state("집중모드")
    if Bot_State.get_state() == "집중모드":
        await message.channel.send(Bot_State.get_state())

@bot.command()
async def 응원해줘(message):
    await message.channel.send("오늘도 모두 좋은 하루 보내시길 바랍니다. 회원님들 모두 화이팅!")

@bot.command()
async def 데일리랄튜브(message):
    await message.channel.send("Test")

@bot.command()
async def 지금은무슨상태(message):
    await message.channel.send("Test")



@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    #morning_cheer.start()
    #night_cheer.start()
    Mode_Concentration.start()
bot.run('코제키우이화이팅')
