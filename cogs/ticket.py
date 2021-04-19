import discord
import config
from discord.ext import commands
import json
import time

bot = commands.Bot(command_prefix = f"{config.prefix}") #config du bot


class Ticket(commands.Cog):
    """Les commandes de ticket."""
    def __init__(self, bot):
        self.bot = bot

        
    @bot.command()
    async def creation(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        test = discord.utils.get(guild.roles, id = 678902263493820418)
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        test: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue {user.mention} dans l'interface de votre demande de création et développement de votre serveur Discord ! \nNous vous demandons de faire la description de votre demande ci-dessous pour que le ticket ne sert pas à rien, un {test.mention} serveur prendra en charge votre demande le plus vite possible **")

    @bot.command()
    async def partenariat(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue Dans le système de Partenariat ! Si vous remplissez les conditions publicitaire nous pouvons continuer, présentez nous votre support de Partenariat {user.mention}, un membre du personnel s'occupera de votre demande.**")

    @bot.command()
    async def evolution(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        test = discord.utils.get(guild.roles, id = 678902263493820418)
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        test: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue dans l'interface de description de votre demande d'amélioration de votre serveur {user.mention} \nUn {test.mention} vous répondra sous peux .**")
        
    @bot.command()
    async def devbot(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        test = discord.utils.get(guild.roles, id = 685575296799604752)
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        test: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue {user.mention} dans l'interface de votre demande de création et développement de votre propre BOT Discord + hébergement (condition àrespecter) ! \nNous vous demandons de faire la description de votre demande ci-dessous pour que le ticket ne sert pas à rien, un {test.mention} prendra en charge votre demande le plus vite possible !**")

    @bot.command()
    async def logodiscord(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        test = discord.utils.get(guild.roles, id = 686934415179644951)
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        test: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue {user.mention} dans l'interface de votre demande de création et développement de vos graphismes pour votre serveur Discord ! Nous vous demandons de faire la description de votre demande ci-dessous pour que le ticket ne sert pas à rien, un {test.mention} prendra en charge votre demande le plus vite possible !**")

    @bot.command()
    async def montage_vidéo(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        test = discord.utils.get(guild.roles, id = 699908850601558037)
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        test: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue dans l'interface de demande de conception de montages & vidéos pour une présentation de votre serveur Discord sous format vidéo, décrivez la description de votre demande {user.mention} un {test.mention} s'occupera de votre demande dès que possible.**")

    @bot.command()
    async def recrutement(self, ctx, user: discord.Member = None):
        user = ctx.author
        guild = user.guild
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        }

        channel = await guild.create_text_channel(f"{user.name}-ticket", overwrites = overwrites)
        await channel.send(f"**Bienvenue cher candidat dans le système global de recrutement {user.mention} merci d'avoir pris le ticket !**\n**__Si vous souhaitez devenir Modérateur du Discord :__ vous serez en relations avec la fédération PacifiqueCreation nous vous poserons quelques questions et nous vous mettrons sous épreuves avant le test vocal, vous devez avant tous respecter les conditions dans recrutement modération.**\n**__Si vous souhaitez devenir Concepteur serveur du Discord :__ Nous allons vous mettre à l'épreuve, vous devez,** *__Créer un serveur de test avec tout ce que vous savez faire dessus.__*\n**__Si vous souhaitez devenir Concepteur de BOT Discord :__ Nous allons vous mettre à l'épreuve, vous devez,** *__Créer un BOT Discord avec toutes les fonctions et commandes que vous pouvez faire dedans en suivant aussi nos services.__*\n**__Si vous souhaitez devenir Concepteur Graphisme;__  Nous allons vous mettre à l'épreuve vous devez,** *__Créer un Graphisme concernant le serveur Discord, (PacifiqueCreation) par vous même, vous avez carte blanche, en suivant aussi nos services__*\n\n__Remarque : Prendre un graphisme sur un moteur de recherche ou prendre des idées sur un moteur de recherche ou autre nous montre que vous êtes pas expérimenté et que vous n'avez pas d'imagination pour créer des œuvres.\n**__Si vous souhaitez devenir Collaborateur du Projet :__  vous respectez les critères de collaboration ? alors nous pouvons continuer, présentez-nous votre serveur discord et un personnel du serveur s'occupera de votre demande de collaboration**\n**__Si vous souhaitez devenir Concepteur de création et développement de vidéo pour des présentation de serveur sous format vidéo ;__ vous devez nous montrer une vidéo avec montage que vous avez créer vous même**\n*__Remarque :__ Dans tout les domaines de conceptions nous vous métrons à l'épreuve pour le domaine de recrutement de concepteur*")

    #take 

    @bot.command()
    @commands.has_role(792734218434117643)
    async def take(self, ctx, user: discord.Member, channell : discord.TextChannel):
        test = ctx.author.mention
        guild = ctx.message.guild
        await channell.send(f"Bonne nouvelle {user.mention}, il y a {test} qui a pris ta demande !")
        await channell.edit(name = f"{user.name}-en-cours")
        

        with open('/home/pacifiquec/bot1/demande.json', 'r') as f:
            numéro = json.load(f)

        if not 'demande' in numéro:
            numéro = {}
            numéro['demande'] = 1
        else:
            numéro['demande'] += 1

        with open('/home/pacifiquec/bot1/demande.json', 'w') as f:
            json.dump(numéro, f, indent=4)
        

        with open('/home/pacifiquec/bot1/demande.json', 'r')as f:
            numéro = json.load(f)

        a = 0
        a = numéro['demande']


        demande = discord.utils.get(guild.channels, id = 679302357330165770)
        log = discord.utils.get(guild.channels, id = 694617389660110982)
        embed = discord.Embed(title=f"La demmande de {user.name} a été prise", colour=discord.Color.orange())
        embed.add_field(name=f"**Client** :", value=f"> **{user.name}**", inline = False)
        embed.add_field(name=f"**Identifiant** :", value=f"> **{user.id}**", inline = False)
        embed.add_field(name=f"**Concepteur** :", value=f"> **{test}**", inline = False)
        embed.add_field(name=f"**Numéro de demande** :", value=f"> **N°{a}**", inline = False)
        embed.set_footer(text=f"{time.asctime()}")
        embed.set_thumbnail(url = user.avatar_url)

        await demande.send(embed = embed)
        await log.send(embed = embed)

    @bot.command()
    @commands.has_role(792734218434117643)
    async def end(self, ctx, user: discord.Member, channell : discord.TextChannel):
        test = ctx.message.author.mention
        guild = ctx.message.guild
        await channell.send(f"Merci d'avoir utilisé nos service, {user.mention}, votre commande est terminée !")
        await channell.send(f"Pensez aussi à remercier le concepteur qui a réalisé votre demmande dans <#679378795765039114> \nMerci ^^")
        await channell.edit(name = f"{user.name}-finit")

        demande = discord.utils.get(guild.channels, id = 679302357330165770)
        log = discord.utils.get(guild.channels, id = 694617389660110982)
        embed = discord.Embed(title=f"La demmande de {user.name} est finit", colour=discord.Color.green())
        embed.add_field(name=f"**Client** :", value=f"> **{user.name}**", inline = False)
        embed.add_field(name=f"**Identifiant** :", value=f"> **{user.id}**", inline = False)
        embed.add_field(name=f"**Concepteur** :", value=f"> **{test}**", inline = False)
        embed.set_footer(text=f"{time.strftime('%d %A %b')} à {time.strftime('%X')}")
        embed.set_thumbnail(url = user.avatar_url)
        await demande.send(embed = embed)
        with open('/home/pacifiquec/bot1/demande.json', 'r')as f:
            numéro = json.load(f)

        a = 0
        a = numéro['demande']
        guild = ctx.message.guild

        vocal = discord.utils.get(guild.channels, id = 698830925231947806)   
        await vocal.edit(name = f"Demande finit : {a}")
        await log.send(embed = embed)
        

    @bot.command()
    @commands.has_role(792734218434117643)
    async def close(self, ctx, user: discord.Member, channell : discord.TextChannel):
        guild = ctx.message.guild
        #await channell.delete()
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        user: discord.PermissionOverwrite(read_messages=False, send_messages=False)
                        }
        await channell.edit(name = f"{user.name}-finit", overwrites = overwrites)
        await channell.send("**DEMANDE FINIT**")
        await channell.send("Pour supprimer ce salon, faite la commande ``^^p.del_ticket``")
        log = discord.utils.get(guild.channels, id = 694617389660110982)
        await log.send(f"La commande de {user} a été finis")

    @bot.command()
    @commands.has_role(792734218434117643)
    async def del_ticket(self, ctx, user: discord.Member, channel: discord.TextChannel):
        await channel.delete()
        guild = ctx.message.guild
        log = discord.utils.get(guild.channels, id = 694617389660110982)
        await log.send(f"Le ticket de {user} a été supprimé")

    #error

    @take.error
    async def take_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention} tu n'as pas les permissions nécessaires pour effectuer cette commande" ,delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque quelques arguments que tu ne m'as pas donnés ..." ,delete_after=10.0)
            await ctx.send("``take <@user> {channel}``" ,delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donnés sont mauvais ..." ,delete_after=10.0)
            await ctx.send("``take <@user> {channel}``" ,delete_after=10.0)
        else:
            await ctx.send(error)

    @close.error
    async def close_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention} tu n'as pas les permissions nécessaire pour effectuer cette commande " ,delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque quelques arguments que tu ne m'as pas donnés ..." ,delete_after=10.0)
            await ctx.send("``close <@user> {channel}``" ,delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donnés sont mauvais ..." ,delete_after=10.0)
            await ctx.send("``close <@user> {channel}``" ,delete_after=10.0)
        else:
            pass

    @end.error
    async def end_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'as pas les permissions nécessaires pour effectuer cette commande" ,delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne m'as pas donnés ..." ,delete_after=10.0)
            await ctx.send("``close <@user> {channel}``" ,delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'as donnés sont mauvais ..." ,delete_after=10.0)
            await ctx.send("``close <@user> {channel}``" ,delete_after=10.0)
        else:
            pass

    @del_ticket.error
    async def del_ticket_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'as pas les permissions nécessaire pour effectuer cette commande" ,delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque quelques arguments que tu ne m'as pas donnés ..." ,delete_after=10.0)
            await ctx.send("``del_ticket <@user> {channel}``" ,delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'as donnés sont mauvais ..." ,delete_after=10.0)
            await ctx.send("``del_ticket <@user> {channel}``" ,delete_after=10.0)
        else:
            pass
      
        
        
def setup(bot):
    bot.add_cog(Ticket(bot))
