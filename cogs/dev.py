import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix = f"{config.prefix}") #config du bot


class Dev(commands.Cog):
    """Les commandes développeur."""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    @commands.is_owner()
    async def changelog(self, ctx, *, message):
      """Permet d'ajouter les mises-à-jour du bot"""
      await ctx.message.delete()
      par = ctx.author.name
      embed=discord.Embed(title=f"Changelog de {par}", colour=discord.Color.dark_blue())
      embed.add_field(name=f"Ajout de :", value=f"{message}")
      await ctx.send(embed=embed)
      return
      
        
        
def setup(bot):
    bot.add_cog(Dev(bot))
