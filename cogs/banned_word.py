import discord
from discord.ext import commands
import json

################################Import config.py from parent folder################################
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import config


bot = commands.Bot(command_prefix = f"{config.prefix}") #config du bot

class bword(commands.Cog):
    '''Add banned word command.'''
    def __init__(self, bot):
        self.bot = bot
    
    @bot.event
    async def on_message(ctx):
        await ctx.send("pong !")




def setup(bot):
    bot.add_cog(bword(bot))

