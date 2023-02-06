from discord.ext import commands


class CommandesOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.guild.id == 1048273748320600084

    @commands.command()
    async def plabou(self, ctx):
        print("https://cdn.discordapp.com/attachments/452761605558501386/1068240041006088202/image.png")
        await ctx.send("https://cdn.discordapp.com/attachments/452761605558501386/1068240041006088202/image.png")

    @commands.command()
    async def heeelp(self, ctx):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/452761605558501386/1068241176320295033/text-1674758925520.png")
