import discord
import requests
import random
import ctypes
from main import *
import hashlib
import io
import urllib
from urllib import parse, request
import re
from settings import *
from discord.ext import commands

def url_to_bytes(url):
    data = requests.get(url)
    content = io.BytesIO(data.content)
    filename = url.rsplit("/", 1)[-1]
    return {"content":content, "filename":filename}


class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, *, country_=None):

        if country_ == None:
            embed = discord.Embed(
                color = bad,
                description = f'**Oops** You need an argument country to use this command. :x: '
                )
            embed.set_footer(text=f'Example: {bot.command_prefix}Covid Chile')
            await ctx.send(embed=embed)            

        try:
            r = requests.get('https://corona-rest-api.herokuapp.com/Api/{}'.format(country_)).json()
            
            country = f"{r['Success']['country']}"
            cases = f"{r['Success']['cases']}"
            today_cases = f"{r['Success']['todayCases']}"
            deaths = f"{r['Success']['deaths']}"
            today_deaths = f"{r['Success']['todayDeaths']}"
            active_cases = f"{r['Success']['active']}"
            critical_cases = f"{r['Success']['critical']}"
            covid_test = f"{r['Success']['totalTests']}"

            embed = discord.Embed(
                color = color,
                description = f'''
                Covid cases in {country}

                Cases : `{cases}`
                Today Cases : `{today_cases}`
                All Dead In {country} : `{deaths}`
                Today Deaths : `{today_deaths}`
                Active Cases : `{active_cases}`
                Critical Cases : `{critical_cases}`
                All Covid Test [PCR] : `{covid_test}`
                '''
            )
            embed.set_footer(text=f'Requests by {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        except:
            
            embed = discord.Embed(
                color = bad,
                description = f'**Oops** This country is invalid or cannot be found, try another. :x: '
                )
            embed.set_footer(text='ERROR : Invalid request. :(')
            await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member=None):

        if member == None:

            embed = discord.Embed(
                title = f'Your avatar.',
                color = color
                )
            embed.set_author(name='{}'.format(ctx.author), icon_url='{}'.format(ctx.author.avatar_url))
            embed.set_image(url='{}'.format(ctx.author.avatar_url))
            await ctx.reply(embed=embed, mention_author=False)

        else:
            
            embed = discord.Embed(
                title = f'Avatar of {member}',
                color = color
                )
            embed.set_author(name='{}'.format(member), icon_url='{}'.format(member.avatar_url))
            embed.set_image(url='{}'.format(member.avatar_url))
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member=None):

        if member == None:
            await ctx.send('Reply')

        else:

            await ctx.send(f'{member}')

    @commands.command()
    async def randomnumber(self, ctx):

        number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99']

        get_number = random.choice(number)

        embed = discord.Embed(
            title = 'Random number',
            color = color,
            description = f'Your number is {get_number}'
        )
        embed.set_footer(text=f'Request by **{ctx.author}**', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def md5(self, ctx, *, msg:str):
        await ctx.send("{}".format(hashlib.md5(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def cat(self, ctx):
        
        re = requests.get('https://api.thecatapi.com/v1/images/search').json()

        img = re[0]['url']

        embed = discord.Embed(
            color = color
        )
        embed.set_image(url=img)
        await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):

        try:
            embed = discord.Embed(
                title = f'Server icon - {ctx.guild.name}',
                color = color
            )
            embed.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        except:
            return

    @commands.command()
    async def avatar_url(self, ctx):

        return
    
def setup(bot):
    bot.add_cog(utils(bot))