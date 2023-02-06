import discord
from discord.ext import commands


message_id = 1071946023922057298


class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # utilisable uniquement par moi
    async def cog_check(self, ctx):
        return ctx.author.id == 403647969792098305

    # envoie un message de choix de role
    @commands.command()
    async def role_embed(self, ctx):
        print(ctx.guild.emojis)
        message_role = discord.Embed(title="Choisis tes roles :",
                                     color=0xcc0000,
                                     description="<:z_madkar:1062103942856712212> : Mario\n<a:winter_2014:1059852702387028028> : Zelda\n<:ics_please_respond:1062341103992442941> : Pokémon")
        message = await ctx.send(embed=message_role)
        await message.add_reaction("<:z_madkar:1062103942856712212>")
        await message.add_reaction("<a:winter_2014:1059852702387028028>")
        await message.add_reaction("<:ics_please_respond:1062341103992442941>")
        print(message.id)

    # donne un role si ajoute une réaction
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)

        if payload.emoji.id == 1062103942856712212:
            role = discord.utils.get(guild.roles, name='Mario')
            await payload.member.add_roles(role)
        elif payload.emoji.id == 1059852702387028028:
            role = discord.utils.get(guild.roles, name='Zelda')
            await payload.member.add_roles(role)
        elif payload.emoji.id == 1062341103992442941:
            role = discord.utils.get(guild.roles, name='Pokémon')
            await payload.member.add_roles(role)

    # enlève un role si enlève une réaction
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.id == 1062103942856712212:
            role = discord.utils.get(guild.roles, name='Mario')
            await member.remove_roles(role)
        elif payload.emoji.id == 1059852702387028028:
            role = discord.utils.get(guild.roles, name='Zelda')
            await member.remove_roles(role)
        elif payload.emoji.id == 1062341103992442941:
            role = discord.utils.get(guild.roles, name='Pokémon')
            await member.remove_roles(role)
