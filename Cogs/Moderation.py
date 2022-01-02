import discord
import requests
import os
import sys
from main import *
from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member=None, *, reason=None):
        try:
            if user == None:
                embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
                await ctx.send(embed=embed)
                
            elif user == bot.user:
                embed = discord.Embed(color = bad,description = f'**Oops** You need to mention a user to use this command. :x:')
                await ctx.send(embed=embed)
                
            else:
                await user.ban(reason=reason)
                embed = discord.Embed(
                    color = color,
                    description = f'`{user}` was banned by `{ctx.author}` reason : `{reason}`'
                    )
                await ctx.send(embed=embed)
                
        except:
            embed = discord.Embed(
                color = bad,
                description = f'**Oops** I cannot ban this person, remember to place my role above the role of the person you are trying to ban. :x: '
                )
            embed.set_footer(text='Recommendation: Put my role above all roles so that errors like this do not happen. [Insufficient permissions.]')
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member=None, *, reason=None):
        try:

            if user == None:
                embed = discord.Embed(color = bad, description = f'**Oops** You need to mention a user to use this command. :x:')
                await ctx.send(embed=embed)
                
            elif user == bot.user:
                embed = discord.Embed(color = bad,description = f'**Oops** You need to mention a user to use this command. :x:')
                await ctx.send(embed=embed)
                
            else:
                await user.ban(reason=reason)
                embed = discord.Embed(
                    color = color,
                    description = f'`{user}` was kick by `{ctx.author}` reason : `{reason}`'
                    )
                await ctx.send(embed=embed)
                
        except:
            embed = discord.Embed(
                color = bad,
                description = f'**Oops** I cannot kick this person, remember to place my role above the role of the person you are trying to ban. :x: '
                )
            embed.set_footer(text='Recommendation: Put my role above all roles so that errors like this do not happen. [Insufficient permissions.]')
            await ctx.send(embed=embed)
            
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):

        try:
            
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            
            embed = discord.Embed(
                title = 'Channel locked [#{}]'.format(channel),
                color = color
            )
            await ctx.send(embed=embed)

        except:
            
            embed = discord.Embed(
                color = bad,
                description = f'You do not have sufficient permissions to use this command. :x:'
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unlock(self, ctx, channel : discord.TextChannel=None):

        try:
            
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            
            embed = discord.Embed(
                title = 'Channel Unlocked [#{}]'.format(channel),
                color = color
            )
            await ctx.send(embed=embed)

        except:
            
            embed = discord.Embed(
                color = bad,
                description = f'You do not have sufficient permissions to use this command. :x:'
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['purge'])
    @commands.has_permissions(ban_members=True)
    async def nuke(self, ctx, amount: int=None):

        try:

            if amount == None:

                embed = discord.Embed(
                    color = color,
                    description = f'Invalid amount. :x:'
                )
                await ctx.send(embed=embed)
            
            else:
                await ctx.channel.purge(limit=amount)
                
                embed = discord.Embed(
                    title = f'{amount} Message deleted by {ctx.author}',
                    color = color
                )
                await ctx.send(embed=embed)
        
        except:
            
            await ctx.send('Missing permissions.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def sendmd(self, ctx, user: discord.User, *, message):
        try:
            await ctx.author.send(f'')
            embed = discord.Embed(
                color = color,
                description = f'{message}'
            )
            embed.set_footer(text=f'Message by {ctx.author}', icon_url=ctx.author.avatar_url)
            await user.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("This user might be having DMs blocked or it's a bot account...")

def setup(bot):
    bot.add_cog(mod(bot))