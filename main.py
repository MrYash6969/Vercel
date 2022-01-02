import discord
import requests
import os
import sys
import random
import asyncio
import datetime
from discord.ext import commands, tasks
from settings import *
import datetime
import time
from time import sleep

start_time = time.time()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_connect():
    print(f'''
    {bot.user} - Connected!
    {prefix} - Prefix
    ''')

@bot.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(f'Hey, this command is not available.')

@bot.event
async def on_message(message):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    
    mention = f'<@!{bot.user.id}>'
    if message.content == mention:

        embed = discord.Embed(
            color = color,
        )
        embed.add_field(name='Prefix', value=f'```{prefix}```', inline=True)
        embed.add_field(name=f'Uptime', value=f'```{text}```', inline=True)
        embed.set_footer(text='Powered by https://beete.xyz')
        await message.channel.send(embed=embed)
    await bot.process_commands(message)

async def ch_pr(): # Custom status. For vercel.
    await bot.wait_until_ready()

    while not bot.is_closed():
        
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Vercel - Viewing {len(bot.guilds)} servers"))

        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))

        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))

        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))

        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Counter-Strike: Global Offensive"))

        await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Fortnite"))

        await asyncio.sleep(5)


bot.loop.create_task(ch_pr())

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(token)
    os.system('pause')