import discord
import datetime
import time

from discord.ext import commands
from discord.ext import tasks
from itertools import cycle


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())

playing = cycle(['응원', '응원2'])

@tasks.loop(seconds=1)
async def morning_cheer():
    if datetime.datetime.now().hour == 7 and datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
        await bot.get_channel(1097759845077225565).send("오늘도 모두 좋은 하루 보내시길 바랍니다. 회원님들 모두 화이팅!")
        # 1초 sleep하여 중복 전송 방지
        time.sleep(1)

@tasks.loop(seconds=1)
async def night_cheer():
    if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
        await bot.get_channel(1097759845077225565).send("오늘 하루도 고생 많으셨습니다. 회원님들 모두 화이팅!")
        # 1초 sleep하여 중복 전송 방지
        time.sleep(1)
        
@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(playing)))
        

@bot.command()
async def 응원해줘(message):
    await message.channel.send("오늘도 모두 좋은 하루 보내시길 바랍니다. 회원님들 모두 화이팅!")

@bot.command()
async def 데일리랄튜브(message):
    await message.channel.send("Test")

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    change_status.start()
    morning_cheer.start()
    night_cheer.start()
bot.run('코제키우이화이팅')
