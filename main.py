import discord
from discord.ext import commands, tasks
import random
import json
import os
import config
import sys


bot = commands.Bot(command_prefix = f"{config.prefix}", description = f"{config.name}") #config du bot
status = [f"{config.prefix}help",
        "A votre service",
        "Powered by ender_creeps and Fusity.tar.gz",
        "regarder les demandes de la PacifiqueCreation"
        ]

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


@bot.command()
async def start(ctx, secondes = 5):
    changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.online, activity = game)

@bot.event
async def on_ready():
    print("La shard est bien connectée.")
    print(f'\n\nLogged as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    changeStatus.start()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:PacifiqueCreation22:676896410184056856> Il manque un argument. - <:PacifiqueCreation22:676896410184056856>")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("<:PacifiqueCreation22:676896410184056856> - Vous n'avez pas les permissions pour faire cette commande. - <:PacifiqueCreation22:676896410184056856>")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("<:PacifiqueCreation22:#676896410184056856#> - Oups... vous ne pouvez utilisez cette commande. - <:PacifiqueCreation22:676896410184056856>")
    if isinstance(error, discord.Forbidden):
        await ctx.send("<:PacifiqueCreation22:676896410184056856> - Oups... je n'ai pas les permissions nécessaires pour faire cette commmande! - <:PacifiqueCreation22:676896410184056856>")
    else:
        await ctx.send("\n" + error + "\n")
        await ctx.send("Merci de contacter ender_creeps#4934 en cas de ce type de message suivi si possible d'un screen de l'erreur et de la commande, merci")


for filename in os.listdir('cogs/'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    "[Owner only] - Permet de load un cogs"
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('<:PacifiqueCreation38:677599361202520065>')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    "[Owner only] - Permet de reload un cogs"
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('<:PacifiqueCreation38:677599361202520065>')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    "[Owner only] - Permet d'unload un cogs"
    bot.unload_extension(f'cogs.{extension}')
    await ctx.message.add_reaction('<:PacifiqueCreation38:677599361202520065>')

@bot.command()
@commands.is_owner()
async def restart(ctx):
    "[Owner only] - Permet de redémarer la shard."
    await ctx.message.add_reaction('<:PacifiqueCreation38:677599361202520065>')
    await ctx.send("Redémarrage ... Attendez jusqu'à 5 secondes")
    restart_program()

@bot.command()
@commands.is_owner()
async def logout(ctx):
    "[Owner only] - Permet d'arrêter la shard."
    await ctx.send("Shard arrêtée.")
    await ctx.bot.logout()



bot.run(f"{config.token}", bot=True, reconnect=True)
