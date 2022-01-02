import requests
import discord
from discord.ext import commands


class osu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = ''

    @commands.command()
    async def osu(self, ctx):

        pass

def setup(bot):
    bot.add_cog(osu(bot))