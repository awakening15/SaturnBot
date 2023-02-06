import discord
from discord.ext import commands
import bonjour
import commandes
import logs
import reaction_role
import TOKEN

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!", description="ZOOM")

general_id = 1071106499683811441
adieu_id = 1071139737873686718
server_id = 1071106499683811439


@bot.event
async def on_ready():
    print("Ready !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Kirby'))
    await bot.add_cog(commandes.CommandesOwner(bot))
    await bot.add_cog(logs.Logs(bot))
    await bot.add_cog(bonjour.Bonjour(bot))
    await bot.add_cog(reaction_role.ReactionRole(bot))
    await bot.load_extension("quiz")


# activer un fichier
@bot.command()
async def load(ctx, name=None):
    if name:
        await bot.load_extension(name)

# désactiver un fichier
@bot.command()
async def unload(ctx, name=None):
    if name:
        await bot.unload_extension(name)

# actualiser un fichier
@bot.command()
async def reload(ctx, name=None):
    if name:
        try:
            await bot.reload_extension(name)
        except:
            await bot.load_extension(name)

# renvoie le message
@bot.command()
async def test(ctx):
    print(ctx.message.content)

# édite un message du bot
@bot.command()
async def edit(ctx, *,texte):
    channel = bot.get_channel(1067033043199606795)
    message = await channel.fetch_message(1071960240347693066)
    await message.edit(content=texte)


bot.run(TOKEN.TOKEN)
