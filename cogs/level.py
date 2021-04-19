import discord
import config
import random
import json
import asyncio
from math import floor
from discord.ext import commands
'''import sqlite3'''


bot = commands.Bot(command_prefix = f"{config.prefix}") #config du bot


class Level(commands.Cog):
    """Les commandes de level."""
    def __init__(self, bot):
        self.bot = bot


    @bot.event
    async def on_message(message):
        print('Message !')
        if message.author.bot:
            return

        '''if not os.path.exists(users.json):
            with open('users.json', 'w') as json_file:
                users = json.load(json_file)'''

        with open('users.json', 'r') as json_file:
            users = json.load(json_file)
            if not users:
                await user_insert(users, message.author)
                with open("users.json", "w") as f:
                    json.dump(users, f)
                await message.channel.send("You are now in the list you can level up (write some message to lvl up)")
            try:
                print (users[str(message.author.id)])
            except:
                await user_insert(users, message.author)
                with open("users.json", "w") as f:
                    json.dump(users, f)
                await message.channel.send("You are now in the list you can level up (write some message to lvl up)")

            if time.time() - users[str(message.author.id)]["last_message"] > 5:
                number = random.randint(1, 5)
                await add_experience(users, message.author, number)
                await add_money(users, message.author)
                await level_up(users, message.author, message.channel)
                with open("users.json", 'w') as f:
                    json.dump(users, f)
        await bot.process_commands(message)

    async def user_insert(users, user):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]["experience"] = 0
            users[user.id]["level"] = 1
            users[user.id]["last_message"] = time.time()
            users[user.id]["money"] = 0

    async def add_experience(users, user, number):
        experience = floor(9.5 + number + (users[str(user.id)]['level'] - 2))
        users[str(user.id)]["experience"] += experience
        users[str(user.id)]["last_message"] = time.time()

    async def add_money(users, user):
        money = floor((9.5 + users[str(user.id)]['level'] + 50.75 + (users[str(user.id)]['level'] - 2) / 4 * 2 * ((users[str(user.id)]['level']) % 4) + 1 + (users[str(user.id)]['level'] - 6) / 4 * 2) / 18)
        users[str(user.id)]["money"] += money

    async def level_up(users, user, channel):
        experience = users[str(user.id)]["experience"]
        current_level = users[str(user.id)]["level"]
        next_level = int(experience ** (1 / 4))

        if current_level < next_level:
            await channel.send(f":tada: {user.mention}, tu as atteint le niveau {next_level} !")
            users[str(user.id)]["level"] = next_level



'''    @bot.event
    async def on_message(self, message):
        guild = message.guild
        user = message.author
        if message.author.bot == False:
            if bot.user.mentioned_in(message) and message.content != "@everyone" and message.content != "@here":
                channel = message.channel
                await channel.send(f'Mon prefix est "{config.prefix}" faites "{config.prefix}help" pour obtenir de l\'aide!')


                conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
                c = conn.cursor()
                c.execute("SELECT user_id FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, guild.id))
                test = c.fetchone()
                try:
                    test = test[0]
                except:
                    await self.update_data(message.author)
                    await self.add_experience(message.author, xp = random.randint(1, 5))
                    await self.level_up(message.author, message.channel, message)


                if str(test) == str(user.id):
                    await self.add_experience(message.author, xp = random.randint(1, 5))
                    await self.level_up(message.author, message.channel, message)
                else:
                    pass
                conn.close()
        else:
            pass          

        await bot.process_commands(message)

    async def update_data(self, user):
        conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
        c = conn.cursor()
        c.execute("""INSERT INTO level(guild_id, user_id, xp, level) VALUES(?, ?, ?, ?)""", (user.guild.id, user.id, 5, 1))
        conn.commit()

    async def add_experience(self, user, xp):
        conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
        c = conn.cursor()
        c.execute("SELECT xp FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, user.guild.id))
        test = c.fetchone()
        test = test[0]
        a = False
        for role in user.roles:
            if role.id == 688309169601642538:
                a = True
                xp * 2
                break
        
        if a == False:
            pass

        xp += test
        c.execute("""UPDATE level SET xp = ? WHERE user_id = ? AND guild_id = ?""", (xp, user.id, user.guild.id))
        conn.commit()
        conn.close()

    async def level_up(self, user, channel, message): 
        guild = message.guild
        conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
        c = conn.cursor()

        c.execute("SELECT level FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, user.guild.id))
        lvl = c.fetchone()

        c.execute("SELECT xp FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, user.guild.id))
        xp = c.fetchone()

        xp = xp[0]

        #b = [x for elem in lvl for x in elem] 
        lvl = lvl[0]
        print(lvl)

        lvl_end = int((lvl*400) ** 1.025)

        if xp >= lvl_end:
            lvl += 1
            await channel.send(f'{user.mention} est passé levels {lvl} !')
            c.execute("""UPDATE level SET level = ? WHERE user_id = ? AND guild_id = ?""", (lvl, user.id, user.guild.id))
            if lvl >= 5:
                role = discord.utils.get(guild.roles, id = 697452046323810365)
                await user.add_roles(role)
            elif lvl >= 20:
                role = discord.utils.get(guild.roles, id = 678906180856446977)
                await user.add_roles(role)
            else:
                pass
        else:
            pass

        conn.commit()
        conn.close()


    @bot.command()
    async def rank(self, ctx, user: discord.User):
        """Affiche son niveau au sein du serveur"""
        guild = ctx.message.guild
        conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
        c = conn.cursor()

        c.execute("SELECT xp FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, guild.id))
        a = c.fetchone()
        a = a[0]

        c.execute("SELECT level FROM level WHERE user_id = ? AND guild_id = ? ", (user.id, ctx.guild.id))
        b = c.fetchone()
        b = b[0]

        embed = discord.Embed(title=f"Voici le rank de {user}", colour=discord.Color.blue())
        embed.add_field(name=f"**Level : **", value=f"> {b}", inline = False)
        embed.add_field(name=f"**Xp d'activité** :", value=f"> {a}", inline = False)
        embed.set_thumbnail(url = user.avatar_url)
        await ctx.send(embed = embed)

        conn.close()


    @rank.error
    async def rank_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            #user1 = str(ctx.message.author.id)
            user = ctx.message.author.id
            user2 = ctx.message.author


            conn = sqlite3.connect('/home/pacifiquec/bot1/warn.db')
            c = conn.cursor()

            c.execute("SELECT xp FROM level WHERE user_id = ? AND guild_id = ? ", (user, ctx.guild.id))
            a = c.fetchone()
            a = a[0]

            c.execute("SELECT level FROM level WHERE user_id = ? AND guild_id = ? ", (user, ctx.guild.id))
            b = c.fetchone()
            b = b[0]

            embed = discord.Embed(title=f"Voici le rank de {user2}", colour=discord.Color.blue())
            embed.add_field(name=f"**Level : **", value=f"> {b}", inline = False)
            embed.add_field(name=f"**Xp d'activité** :", value=f"> {a}", inline = False)
            embed.set_thumbnail(url = user2.avatar_url)
            await ctx.send(embed = embed)
            conn.close()

        elif isinstance(error, commands.BadArgument):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Désolé... {ctx.author.mention}. Le ou les arguments que tu m'a donnés sont mauvais ...")
            await ctx.send("``rank {user}``")
        else:
            pass'''
            
        
def setup(bot):
    bot.add_cog(Level(bot))
