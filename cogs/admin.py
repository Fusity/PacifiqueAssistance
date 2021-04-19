import discord
from discord.ext import commands
import sqlite3


################################Import config.py from parent folder################################
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import config

bot = commands.Bot(command_prefix = f"{config.prefix}") #config du bot


class Admin(commands.Cog):
    """Les commandes d'adminitration."""
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def warnings(self, ctx, user : discord.User):
        conn = sqlite3.connect('warn.db')

        c = conn.cursor()
        c.execute("SELECT message FROM warn WHERE id_users = ? AND id_server = ? ", (user.id, ctx.guild.id))
        a = c.fetchall()
        b = [x for elem in a for x in elem] 
        if len(b) > 0:
            await ctx.send(f"{user.name} a été warn ``{len(b)} fois`` pour : ```{', '.join(b)}```")
        else:
            await ctx.send(f"{user.name} a été warn ``{len(b)} fois``")
        conn.close()

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user: discord.Member, *, reason: str):
        guild = ctx.message.guild
        conn = sqlite3.connect('warn.db')

        c = conn.cursor()
        c.execute("""INSERT INTO warn(id_server, id_users, name, message) VALUES(?, ?, ?, ?)""", (guild.id, user.id, user.name, reason))
        conn.commit()
        

        embed = discord.Embed(title=f"Warn {guild.name}", colour=000000)
        embed.add_field(name="Victime :", value=f"{user.name}", inline = False)
        embed.add_field(name=f"Raison du warn :", value=f"{reason}", inline = False)
        embed.add_field(name=f"Par :", value=f"{ctx.message.author}", inline = False)
        embed.set_footer(text="Demande de {}".format(ctx.message.author))
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed,delete_after=10.0)
        try:
            await user.send(embed = embed)
        except :
            await ctx.send("Je ne peux pas envoyer d'mp a cette utilisateur")
        log = discord.utils.get(guild.channels, id = 682234253064667183)
        await log.send(embed = embed)
        conn.close()

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'as pas les permissions nécéssaire pour effectuer cette commande ",delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un ou des arguments que tu ne m'a pas donnés ...",delete_after=10.0)
            await ctx.send("``^^p.warn <@user> <raison du warn>``",delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les arguments que tu m'a donnés sont mauvais ...",delete_after=10.0)
            await ctx.send("``^^p.warn <@user> <raison du warn>``",delete_after=10.0)

    @commands.command(pass_context=True, aliases=['purge', 'clean'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, limite: int):
        """Permet d'éffacé un nombre de message donné."""
        await ctx.channel.purge(limit=limite)
        guild = ctx.message.guild
        embed = discord.Embed(title="Clear", colour=000000)
        embed.add_field(name="Nombre de messages supprimés", value=limite)
        embed.set_footer(text="Demande de {}".format(ctx.message.author))
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed = embed, delete_after=10.0)
        log = discord.utils.get(guild.channels, id = 682234253064667183)
        await log.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'as pas les permissions nécéssaire pour effectuer cette commande ", delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un ou des arguments que tu ne m'a pas donnés ...", delete_after=10.0)
            await ctx.send("``^^p.clear <nombre de message>``")
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donnés sont mauvais ...", delete_after=10.0)
            await ctx.send("``^^p.clear <nombre de message>``")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Pas de raison"):

        """Permet de bannir un utilisateur du serveur"""

        await ctx.channel.purge(limit=1)
        par = ctx.author.name
        qui = member.name
        guild = ctx.message.guild
        if member.id == ctx.author.id:
            await ctx.send("Vous ne pouvez pas vous bannir vous-même", delete_after=10.0)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title="Ban", colour=000000)
            embed.add_field(name=f"Vicime :", value=(qui), inline = False)
            embed.add_field(name=f"Raison du ban :", value=(reason), inline = False)
            embed.add_field(name=f"Par :", value=(par), inline = False)
            embed.set_footer(text="Demande de {}".format(ctx.message.author))
            embed.set_image(url="https://media.tenor.com/images/da66a96ca7f65f949a07db8ab9926297/tenor.gif")
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed, delete_after=10.0)
            await member.create_dm()
            await member.dm_channel.send(embed=embed)
            log = discord.utils.get(guild.channels, id = 682234253064667183)
            await log.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande", delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...", delete_after=10.0)
            await ctx.send("``^^p.ban <@user> <raison du warn>``", delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...", delete_after=10.0)
            await ctx.send("``^^p.ban <@user> <raison du ban>``", delete_after=10.0)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Pas de raison."):
        """Permet de kick le membre mentioné."""
        if member.id != ctx.author.id:
            await member.send(f"Vous avez été kick de {ctx.guild.name} par {ctx.author.name} pour la raison suivante: {reason}")
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kick", colour=000000)
            embed.add_field(name=f"Vicime :", value=(member.name), inline = False)
            embed.add_field(name=f"Raison du kick :", value=(reason), inline = False)
            embed.add_field(name=f"Par:", value=(ctx.author.name), inline = False)
            embed.set_footer(text="Demande de {}".format(ctx.message.author))
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed, delete_after=10.0)
            log = discord.utils.get(ctx.message.guild.channels, id = 682234253064667183)
            await log.send(embed=embed)
        else:
            await ctx.send("Vous ne pouvez pas vous kick vous-même", delete_after=10.0)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def softkick(self, ctx, member: discord.Member, *, reason="Pas de raison"):
        """Kick et renvoie une invitation du serveur au membre kick."""
        invite = await ctx.channel.create_invite(max_age = 300)
        if member.id != ctx.author.id:
            await member.send(f"Vous avez été kick de {ctx.guild.name} par {ctx.author.name} pour la raison suivante: {reason} \n Voici une invitation pour revenir sur le serveur. {invite}")
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kick", colour=000000)
            embed.add_field(name=f"Vicime :", value=(member.name), inline = False)
            embed.add_field(name=f"Raison du kick :", value=(reason), inline = False)
            embed.add_field(name=f"Par:", value=(ctx.author.name), inline = False)
            embed.set_footer(text="Demande de {}".format(ctx.message.author))
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed, delete_after=10.0)
            log = discord.utils.get(ctx.message.guild.channels, id = 682234253064667183)
            await log.send(embed=embed)
        else:
            await ctx.send("Vous ne pouvez pas vous kick vous-même", delete_after=10.0)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande", delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...", delete_after=10.0)
            await ctx.send("``^^p.kick <@user> <raison du warn>``")
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...", delete_after=10.0)
            await ctx.send("``^^p.kick <@user> <raison du warn>``", delete_after=10.0)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unban un membre bannis."""
        guild = ctx.message.guild
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                author = ctx.message.name
                embed = discord.Embed(title="Unban", colour=000000)
                embed.add_field(name=f"Utilisateur débannis :", value=f"{member_name, member_discriminator}")
                embed.add_field(name=f"Par :", value=f"{author}")
                embed.set_footer(text="Demande de {}".format(ctx.message.author))
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.send(embed=embed, delete_after=10.0)
                log = discord.utils.get(guild.channels, id = 682234253064667183)
                await log.send(embed=embed)
                return
            else:
                pass

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande ", delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...", delete_after=10.0)
            await ctx.send("``^^p.unban <@user> <raison du warn>``", delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...", delete_after=10.0)
            await ctx.send("``^^p.unban <@user> <raison du warn>``", delete_after=10.0)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, content):
        """Envoie un message par le bot dans le salon où vous éxécuter la commande"""
        await ctx.message.delete()
        await ctx.send(content)

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande ", delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...", delete_after=10.0)
            await ctx.send("``^^p.say <message>``", delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...", delete_after=10.0)
            await ctx.send("``^^p.say <message>``", delete_after=10.0)

    @bot.event
    async def on_message_delete(self, message, user: discord.User=None):
        guild = message.guild
        log = discord.utils.get(guild.channels, id=682234253064667183)
        embed = discord.Embed(title="Message supprimé", colour=discord.Color.dark_blue())
        embed.add_field(name="Un message a été supprimé par ", value=message.author, inline = False)
        embed.add_field(name="Un message a été supprimé dans ", value=message.channel, inline = False)
        embed.add_field(name="Le message était", value=message.content, inline = False)
        await log.send(embed=embed)

    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason="Pas de raison"):
        """Empèche un membre de parler dans le serveur"""
        guild = ctx.message.guild
        await ctx.channel.purge(limit=1)
        role_mute = discord.utils.get(ctx.guild.roles, id = 699182878424170546)
        par = ctx.author.name
        qui = member.name
        await member.add_roles(role_mute)
        embed = discord.Embed(title="Mute", colour=000000)
        embed.add_field(name=f"Vicime :", value=(qui), inline = False)
        embed.add_field(name=f"Raison du mute :", value=(reason), inline = False)
        embed.add_field(name=f"Par :", value=(par), inline = False)
        embed.set_footer(text="Demande de {}".format(ctx.message.author))
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed, delete_after=10.0)
        await member.send(embed=embed)
        log = discord.utils.get(guild.channels, id = 682234253064667183)
        await log.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande",delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...", delete_after=10.0)
            await ctx.send("``^^p.mute <@user> <raison du warn>``",delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...",delete_after=10.0)
            await ctx.send("``^^p.mute <@user> <raison du warn>``",delete_after=10.0)

    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member=None):
        """Redonne la permission au membre séléctionné de parler"""
        guild = ctx.message.guild
        await ctx.channel.purge(limit=1)
        role_mute = discord.utils.get(ctx.guild.roles, id = 699182878424170546)
        par = ctx.author.name
        qui = member.name
        await member.remove_roles(role_mute)
        embed = discord.Embed(title="Unmute", colour=000000)
        embed.add_field(name=f"Vicime :", value=(qui), inline = False)
        embed.add_field(name=f"Mute enlevé par :", value=(par), inline = False)
        embed.set_footer(text="Demande de {}".format(ctx.message.author))
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed,delete_after=10.0)
        await member.send(embed=embed)
        log = discord.utils.get(guild.channels, id = 682234253064667183)
        await log.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): 
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé {ctx.author.mention} tu n'a pas les permissions nécéssaire pour effectuer cette commande",delete_after=10.0)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Il manque un argument ou des arguments que tu ne ma pas donné ...",delete_after=10.0)
            await ctx.send("``^^p.unmute <@user> <raison du mute>``",delete_after=10.0)
        if isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les argument que tu m'a donné sont mauvais ...",delete_after=10.0)
            await ctx.send("``^^p.unmute <@user> <raison du mute>``",delete_after=10.0)

def setup(bot):
    bot.add_cog(Admin(bot))
