from discord.ext import commands

# channel dans lequel les logs apparaissent
log_id = 1071224767094456384


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # détecte les messages édités
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot == True or before.guild.id != 1071106499683811439:
            return
        elif before.content == after.content:
            return
        await self.bot.get_channel(log_id).send(
            f"Message de {before.author} édité dans {before.channel} :\n**Message original : **{before.content}\n**Message édité : **{after.content}")

    #détecte les messages supprimés
    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if ctx.author.bot == True or ctx.guild.id != 1071106499683811439:
            return
        await self.bot.get_channel(log_id).send(f"Message de {ctx.author} supprimé dans {ctx.channel} : \n{ctx.content}")
