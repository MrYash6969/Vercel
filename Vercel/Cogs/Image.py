import discord
import requests
from settings import *
from discord.ext import commands

class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def magik(self, ctx, member: discord.Member):

        if member is None:
            
            json_mk = 'https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image='
            avatar = str(ctx.author.avatar_url_as(format="png"))
            json_mk += avatar
            r = requests.get(json_mk).json()
            embed = discord.Embed(
                title = f'{ctx.author}',
                color = color
            )
            embed.set_footer(text=f'Request by you.')
            embed.set_image(url=r['message'])
            await ctx.send(embed=embed)

        else:

            end = 'https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image='
            av = str(member.avatar_url_as(format="png"))
            end += av
            req = requests.get(end).json()
            
            embed = discord.Embed(
                title = f'{member}',
                color = color
            )
            embed.set_footer(text=f'Request by {ctx.author} for {member}')
            embed.set_image(url=req['message'])
            await ctx.send(embed=embed)

    @commands.command()
    async def deepfry(self, ctx, member: discord.Member=None):

        if member == None:
            base = f'https://nekobot.xyz/api/imagegen?type=deepfry&image={ctx.author.avatar_url}'
            request = requests.get(base).json()

            embed_ = discord.Embed(
                title = ctx.author,
                color = color
            )
            embed_.set_image(url=request['message'])
            embed_.set_footer(text='Request by you')
            await ctx.send(embed=embed_)

        else:
            ba = f'https://nekobot.xyz/api/imagegen?type=deepfry&image={member.avatar_url}'
            req = requests.get(ba).json()
            
            embed = discord.Embed(
                title = f'{member}',
                color = color
            )
            embed.set_footer(text=f'Request by {ctx.author} for {member}')
            embed.set_image(url=req['message'])
            await ctx.send(embed=embed)            


def setup(bot):
    bot.add_cog(image(bot))