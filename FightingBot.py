import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def 응원해줘(message):
    await message.channel.send('Hi!')
 
bot.run('MTE1MDY4MTQ0NjEwNTc1MTYxMg.GMl1Rr.N_KUFUo65PJYG0P0JTAjuhs3bIvFXbaoSIbYHQ')
