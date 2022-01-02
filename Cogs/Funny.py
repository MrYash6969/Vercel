import discord
import requests
import os
import sys
import random
import main
from main import *
from requests.api import request
from settings import *
import random
from discord.ext import commands


class funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, member: discord.Member=None):

        r = requests.get(f'{api}/img/kiss').json()

        url = r['url']

        if member == None:
            embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
            await ctx.send(embed=embed)

        if member == ctx.author:
            await ctx.reply('You seem to love each other a lot, right?')
        
        else:

            embed = discord.Embed(
                color = color,
                description = f'`{ctx.author}` **Gave a kiss to** `{member}`'
            )
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member=None):

        r = requests.get(f'{api}/img/slap').json()

        url = r['url']

        if member == None:
            embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
            await ctx.send(embed=embed)

        if member == ctx.author:
            await ctx.reply('You seem to love each other a lot, right?')
        
        else:

            embed = discord.Embed(
                color = color,
                description = f'`{ctx.author}` **Slapped** `{member}`'
            )
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):

        r = requests.get(f'{api}/img/hug').json()

        url = r['url']

        if member == None:
            embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
            await ctx.send(embed=embed)

        if member == ctx.author:
            await ctx.reply('You seem to love each other a lot, right?')
        
        else:

            embed = discord.Embed(
                color = color,
                description = f'`{ctx.author}`** gave** `{member}`** a hug**'
            )
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def iq(self, ctx, user: discord.Member=None):

        iq = [
            "0 IQ LOL",
            "1 IQ HAHA",
            "10 IQ -_-",
            "20 IQ ??",
            "30 IQ WOW",
            "40 IQ",
            "50 IQ",
            "60 IQ",
            "70 IQ",
            "80 IQ",
            "90 IQ",
            "100 IQ",
            "∞ It's albert einstein"
        ]

        if user == None:

            embed = discord.Embed(
                title = f'Your iq is {random.choice(iq)}',
                color = color
            )
            embed.set_image(url='https://c.tenor.com/dp_hQBGT0rIAAAAC/think-smart.gif')
            embed.set_footer(text='Request by you.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            
        else:
            
            embed = discord.Embed(
                title = f'The IQ of {user} is {random.choice(iq)}',
                color = color
            )
            embed.set_image(url='https://c.tenor.com/dp_hQBGT0rIAAAAC/think-smart.gif')
            embed.set_footer(text='Request by you.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):

        r = requests.get('https://some-random-api.ml/meme').json()

        meme = r['image']

        embed = discord.Embed(
            color = color
        )
        embed.set_image(url=meme)
        await ctx.send(embed=embed)

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, message):

        r = requests.get(f'{api}/8ball').json()

        response = r['response']
        img = r['url']

        embed = discord.Embed(
            color = color,
            description = f'''
            Your question : **{message}**
            
            Response : **{response}**
            '''
        )
        embed.set_image(url=img)
        await ctx.send(embed=embed)

    @commands.command()
    async def tweet(self, ctx, *, message=None):

        if message == None:
            
            re = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.author.name}&text=hello-world').json()         
            
            embed = discord.Embed(
                color = color
                )
            embed.set_image(url=re['message'])
            await ctx.send(embed=embed)

        else:

            re = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.author.name}&text={message}').json()

            embed = discord.Embed(
                color = color
            )
            embed.set_image(url=re['message'])
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member=None):
        
        request = requests.get(f'{api}/img/pat').json()

        if member == None:
            embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
            await ctx.send(embed=embed)

        if member == ctx.author:
            await ctx.reply('You seem to love each other a lot, right?')
        
        else:
            embed = discord.Embed(
                color = color,
                description = f'**{ctx.author.name}** caressed **{member.name}**'
            )
            embed.set_image(url=request['url'])
            await ctx.send(embed=embed)

    @commands.command()
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        
        if a == b == c:
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
        else:
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

    @commands.command()
    async def ascii(self, ctx, *, message):
        
        r = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
        if len('```' + r + '```') > 2000:
            return
        await ctx.reply(f"```{r}```")

    @commands.command()
    async def dickside(self, ctx, user: discord.User=None):

        if user == bot.user:
            await ctx.reply('I think I am a woman?')

        else:
            
            if user is None:
                user = ctx.author
                
            size = random.randint(1, 50)
            dong = ""
            
            for _i in range(0, size):
                dong += "="
            await ctx.send(f"{user}'s D1ck size\n8{dong}D")

    @commands.command(name='youareidiot')
    async def _oyou(self, ctx):

        return

def setup(bot):
    bot.add_cog(funny(bot))