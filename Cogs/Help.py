from os import name
import discord
from discord.ext import commands
from settings import *

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        try:
            
            embed = discord.Embed(
                title = title,
                color = color,
            description = f'''Hello! **{ctx.author.name}** :wave:, Thanks for asking for my command list.\n\nImportant moderation administrator permission required.'''
            )
            embed.add_field(
            name='Funny Commands.',
            value=f'''
            `{prefix}kiss <@Member>`
            `{prefix}hug <@Member>`
            `{prefix}slap <@Member>`
            `{prefix}iq <@Member>`
            `{prefix}8ball <Question>`
            `{prefix}meme`
            `{prefix}tweet <Message>`
            `{prefix}cat`
            `{prefix}slot`
            `{prefix}ascii <Text>`
            `{prefix}dickside <@Member>`
            ''', inline=True)
            embed.add_field(
            name='Utils Commands.',
            value=f'''
            `{prefix}avatar <@Member>`
            `{prefix}covid <Country>`
            `{prefix}randomnumber`
            `{prefix}md5 <Message>`
            `{prefix}servericon`
            ''', inline=True)
            embed.add_field(
            name = 'Moderation Commands.',
            value=f'''
            `{prefix}ban <@Member> <Reason>`
            `{prefix}kick <@Member> <Reason>`
            `{prefix}sendmd <@Member> <Message>`
            `{prefix}lock <#Channel or None>`
            `{prefix}unlock <#Channel or None>`
            `{prefix}nuke or purge <Amount>`
            `{prefix}sendmd <Message> <@Member>`
            ''', inline=True
            )
            embed.add_field(
                name='Image Commands.',
                value=f'''
                `{prefix}magik <@Member>`
                `{prefix}deepfry <@Member>`
                '''
            )
            embed.set_footer(text='Powered by beete.xyz', icon_url='https://pbs.twimg.com/profile_images/1476251761644126213/zDZG9LW__400x400.jpg')
            await ctx.send(embed=embed)

        except:

            await ctx.send(f'{ctx.author.mention}')
            embed = discord.Embed(
                color = color,
                description = f'You need to have your private messages activated in order to use this command.'
            )
            await ctx.send(embed=embed)
        



def setup(bot):
    bot.add_cog(help(bot))