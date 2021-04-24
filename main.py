import discord
from discord.ext import commands, tasks
import random
import json
import os
import config
import sys
################## Pensez à enlever le token pour éviter que Discord gueule ###################################

bot = commands.Bot(command_prefix = f"{config.prefix}", description = f"{config.name}") #config du bot

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
async def start(ctx, secondes = 2):
    changeStatus.change_interval(seconds = secondes)

####################### Poisson d'avril à faire #######################

'''@tasks.loop(seconds = 5)
async def changeStatus():
    name_status = [f"{config.prefix}help",
        "A votre service",
        "Powered by ender_creeps and Fusity.tar.gz",
        "regarder les demandes de la PacifiqueCreation"
        ]
    type_status = [discord.ActivityType.listening,
    discord.ActivityType.playing,
    discord.ActivityType.streaming,
    discord.ActivityType.competing
    ]
    online_status = [discord.Status.do_not_disturb,
    discord.Status.invisible,
    discord.Status.offline,
    discord.Status.online,
    discord.Status.idle
    ]

    await bot.change_presence(status = random.choice(online_status), #Can be set to online, offline, do_not_disturb, idle, invisible
                            activity = discord.Activity(type=random.choice(type_status),
                            #Can be set to competing, streaming, playing, listening, watching, unknown
                            name=random.choice(name_status)))'''

#####################################################################


@tasks.loop(seconds = 5)
async def changeStatus():
    emoji = bot.get_emoji(834848666900103246)
    watlisten = [discord.ActivityType.listening, discord.ActivityType.watching]
    activity = [
        discord.Activity(type=random.choice(watlisten), name="les demandes de la PacifiqueCreation"),
        discord.Activity(type=discord.ActivityType.playing, name="votre service"),
        discord.Activity(type=discord.ActivityType.streaming, name=f"{config.prefix}help"),
        discord.Activity(type=discord.ActivityType.watching, name=" : powered by ender_creeps and Fusity.tar.gz")
    ]
    await bot.change_presence(status = discord.Status.online, activity = random.choice(activity))

@bot.event
async def on_ready():
    chnl = bot.get_channel(769878109729456140)
    await chnl.send("Je suis prêt !")
    print("La shard est bien connectée.")
    print(f'\n\nLogged as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    changeStatus.start()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(error)
        await ctx.send("<:PacifiqueCreation22:676896410184056856> Il manque un argument. - <:PacifiqueCreation22:676896410184056856>")
    elif isinstance(error, commands.MissingPermissions):
        print(error)
        await ctx.send("<:PacifiqueCreation22:676896410184056856> - Vous n'avez pas les permissions pour faire cette commande. - <:PacifiqueCreation22:676896410184056856>")
    elif isinstance(error, commands.CheckFailure):
        print(error)
        await ctx.send("<:PacifiqueCreation22:676896410184056856> - Oups... vous ne pouvez utilisez cette commande. - <:PacifiqueCreation22:676896410184056856>")
    if isinstance(error, discord.Forbidden):
        print(error)
        await ctx.send("<:PacifiqueCreation22:676896410184056856> - Oups... je n'ai pas les permissions nécessaires pour faire cette commmande! - <:PacifiqueCreation22:676896410184056856>")
    else:
        print(error)
        await ctx.send("\n" + str(error) + "\n")
        await ctx.send("Merci de contacter ender_creeps#4934 en cas de ce type de message suivi si possible d'un screen de l'erreur et de la commande, merci")


for filename in os.listdir('PacifiqueAssistance/cogs/'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') 

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    "[Owner only] - Permet de load un cogs"
    bot.load_extension(f'cogs.{extension}')
    message = await ctx.send(f"{extension} loaded !")
    await message.add_reaction('<:PacifiqueCreation38:835131679533826068>')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    "[Owner only] - Permet de reload un cogs"
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    message = await ctx.send(f"{extension} reloaded !")
    await message.add_reaction('<:PacifiqueCreation38:835131679533826068>')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    "[Owner only] - Permet d'unload un cogs"
    bot.unload_extension(f'cogs.{extension}')
    message = await ctx.send(f"{extension} unloaded !")
    await message.add_reaction('<:PacifiqueCreation38:835131679533826068>')

@bot.command()
@commands.is_owner()
async def restart(ctx):
    "[Owner only] - Permet de redémarer la shard."
    await ctx.message.add_reaction('<:PacifiqueCreation38:835220791447912458>')
    await ctx.send("Redémarrage ... Attendez jusqu'à 5 secondes")
    restart_program()

@bot.command()
@commands.is_owner()
async def logout(ctx):
    "[Owner only] - Permet d'arrêter la shard."
    await ctx.send("Shard arrêtée.")
    await ctx.bot.logout()



bot.run(f"{config.token}", bot=True, reconnect=True)
################## Pensez à enlever le token pour éviter que Discord gueule ###################################
