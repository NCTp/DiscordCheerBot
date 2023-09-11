import discord
import datetime
import time

from discord.ext import commands
from discord.ext import tasks
from itertools import cycle


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())

playing = cycle(['응원', '응원2'])

@tasks.loop(seconds=1)
async def every_hour_notice():
    if datetime.datetime.now().second == 50:
        await bot.get_channel(1097759845077225565).send("현재 {}시 {}분 입니다.".format(datetime.datetime.now().hour, datetime.datetime.now().minute))
        # 1초 sleep하여 중복 전송 방지
        time.sleep(1)
        
@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(playing)))
        
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    change_status.start()
    every_hour_notice.start()
 
@bot.command()
async def 응원해줘(message):
    await message.channel.send('오늘도 모두 좋은 하루 보내시길 바랍니다. 회원님들 모두 화이팅!')
 
bot.run('TOKEN')
