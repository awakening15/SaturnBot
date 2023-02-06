import discord
import random
from discord.ext import commands

server_id = 1071106499683811439
bonjour_id = 1071106499683811441
au_revoir_id = 1071139737873686718


class Bonjour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot == True or member.guild.id != server_id:
            return
        personnage = ["Mario",
                      "Luigi",
                      "Wario",
                      "Bowser",
                      "Harmonie et Luma",
                      "Yoshi",
                      "Link",
                      "Zelda",
                      "Ganondorf",
                      "Donkey Kong",
                      "Diddy Kong",
                      "Fox",
                      "Falco",
                      "Ness",
                      "Lucas",
                      "Samus Sombre",
                      "Kirby",
                      "Meta Knight",
                      "Roi Dadidou",
                      "Pikachu",
                      "Pichu",
                      "Rondoudou",
                      "Amphinobi",
                      "Felinferno",
                      "Link Enfant",
                      "Link Cartoon",
                      "Sheik",
                      "Captain Falcon",
                      "Peach",
                      "Daisy",
                      "Ice Climbers",
                      "Dr. Mario",
                      "Marth",
                      "Lucina",
                      "Roy",
                      "Chrom",
                      "Daraen",
                      "Ike",
                      "Byleth",
                      "Corrin",
                      "Cloud",
                      "Sephiroth",
                      "Snake",
                      "Sonic",
                      "Pit",
                      "Pit Maléfique",
                      "Dresseur de Pokemon",
                      "Entraineuse Wii Fit",
                      "Olimar",
                      "Palutena",
                      "Mewtwo",
                      "Plante Piranha",
                      "Joker",
                      "Banjo et Kazooie",
                      "Kazuya",
                      "Terry",
                      "Minmin",
                      "Sora",
                      "Steve",
                      "Hero",
                      "Mr. Game and Watch",
                      "Samus sans Armure",
                      "Wolf",
                      "Lucario",
                      "Rob",
                      "Villageois",
                      "Megaman",
                      "Little Mac",
                      "Pac-Man",
                      "Shulk",
                      "Bowser Jr.",
                      "Duo Duck Hunt",
                      "Ryu",
                      "Ken",
                      "Bayonetta",
                      "Inkling",
                      "Ridley",
                      "Simon",
                      "Richter",
                      "Marie",
                      "King K. Rool",
                      "Pyra/Mythra"]
        channel = member.guild.get_channel(bonjour_id)
        true_member_count = len([m for m in member.guild.members if not m.bot])
        thumbnail = "https://cdn.discordapp.com/attachments/452761605558501386/1071394682917097502/description-image.png"
        image = "https://cdn.discordapp.com/attachments/452761605558501386/1071397048764596294/6269a3aa2119c8.png"
        message_bienvenue = discord.Embed(title="Bienvenue sur Nintendo Palace", color=0xf56cf0,
                                          description="*Tu aimes Nintendo?*\n\n**Vérifie** et prends connaissance de nos <#1071111830287696004> avant de discuter sur le serveur!\n\n**Prends** tes <#1071110380752994394> pour pouvoir partager tes jeux préférés avec les autres membres!\n\n**Amuse** toi avec nous!"
                                          )
        message_bienvenue.set_thumbnail(
            url=thumbnail)
        message_bienvenue.set_image(
            url=image)
        message_bienvenue.set_footer(text=random.choice(personnage) + " te remercie ❤️")
        await channel.send(
            f"{member.mention} nous a rejoint dans le super monde de Nintendo et nous sommes maintenant **{true_member_count}**! <:Bro_HighFive:1071214208949157888>",
            embed=message_bienvenue)

        @commands.Cog.listener()
        async def on_member_remove(self, member):
            if member.bot == True or member.guild.id != server_id:
                return
            channel = member.guild.get_channel(au_revoir_id)
            await channel.send(f"{member.mention} a perdu sa dernière vie...")
