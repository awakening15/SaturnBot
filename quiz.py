from discord.ext import commands
import random


async def setup(bot):
    await bot.add_cog(Quiz(bot, on_command=0))


class Quiz(commands.Cog):
    def __init__(self, bot, on_command):
        self.bot = bot
        self.on_command = on_command

    @commands.command()
    async def q(self, ctx, categorie="nintendo"):
        if self.on_command == 1:
            return
        self.on_command = 1
        # création des catégories
        liste_categorie = ["nintendo", "zelda", "castlevania"]

        # si la catégorie renseignée n'existe pas, mettre nintendo par défaut
        if categorie not in liste_categorie:
            categorie = "nintendo"
            await ctx.send("Cette catégorie n'existe pas, question aléatoire par defaut :")

        # récupère l'emplacement de la catégorie dans la liste
        index = liste_categorie.index(categorie)

        # liste des questions pour chaque catégorie
        questions_zelda = [

            {
                "questions": "En quelle année est sorti The Legend of Zelda?",
                "reponses": "1986"
            },
            {
                "questions": "En quelle année est sorti Zelda II?",
                "reponses": "1987"
            },
            {
                "questions": "En quelle année est sorti A Link to the Past?",
                "reponses": "1991"
            },
            {
                "questions": "En quelle année est sorti Link's Awakening?",
                "reponses": "1993"
            },
            {
                "questions": "En quelle année est sorti Ocarina of Time?",
                "reponses": "1998"

            },
            {
                "questions": "En quelle année est sorti Majora's Mask?",
                "reponses": "2000"
            },
            {
                "questions": "En quelle année est sorti Oracle of Ages?",
                "reponses": "2001"
            },
            {
                "questions": "En quelle année est sorti Oracle of Seasons?",
                "reponses": "2001"
            },
            {
                "questions": "En quelle année est sorti The Wind Waker?",
                "reponses": "2002"
            },
            {
                "questions": "En quelle année est sorti The Minish Cap?",
                "reponses": "2004"
            },
            {
                "questions": "En quelle année est sorti Twilight Princess?",
                "reponses": "2006"
            },
            {
                "questions": "En quelle année est sorti Phantom Hourglass?",
                "reponses": "2007"
            },
            {
                "questions": "En quelle année est sorti Spirit Tracks?",
                "reponses": "2009"
            },
            {
                "questions": "En quelle année est sorti Skyward Sword?",
                "reponses": "2011"
            },
            {
                "questions": "En quelle année est sorti A Link Between Worlds?",
                "reponses": "2013"
            },
            {
                "questions": "En quelle année est sorti Breath of the Wild?",
                "reponses": "2017"
            },
            {
                "questions": "Comment s'appelle l'oracle des saisons?",
                "reponses": "Din"
            }
        ]
        questions_castlevania = [
            {
                "questions": "En quelle année est sorti Harmony of Dissonance?",
                "reponses": "2002"
            }
        ]
        questions_nintendo = questions_zelda + questions_castlevania
        liste_questions = [questions_nintendo, questions_zelda, questions_castlevania]

        # prendre une question au hasard dans la catégorie choisie
        nombre_questions = len(liste_questions[index])
        numero = random.randint(0, nombre_questions-1)
        bonne_reponse = liste_questions[index][numero]["reponses"]

        # check le chan et la réponse
        def check(message):
            return message.channel == ctx.message.channel and message.content.lower() == bonne_reponse.lower()

        try:
            # pose la question
            await ctx.send(liste_questions[index][numero]["questions"])

            # attends la bonne réponse pendant t secondes
            reponse = await self.bot.wait_for("message", timeout=20, check=check)

            # valide la réponse
            await ctx.send(f"{reponse.author.mention} a trouvé la bonne réponse : " + bonne_reponse)

        except:
            # donne la bonne réponse en cas d'échec
            await ctx.send("Personne n'a trouvé, la bonne réponse était " + bonne_reponse)

        self.on_command=0
