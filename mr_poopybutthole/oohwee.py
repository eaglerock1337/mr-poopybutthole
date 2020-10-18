import discord
import os
import logging
import random

from discord.ext import commands
from dotenv import load_dotenv

CHRIS_ID = 533873187780558848
ROB_ID = 445052623171878912
GAY_FILES = ["gay1.jpg", "gay2.jpg", "gay3.jpg", "gay4.jpg", "gay5.jpg", "gay6.jpg"]


class Oohwee(commands.Cog):
    """
    The primary class for the Mr. Poopybutthole Discord bot.

    Hands the base commands that make up the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.chris_responder = True
        self.rob_responder = True

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"Oooh, wee! {self.bot.user.name} has connected to Discord!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Oooh, wee! {member.name} has joined the server!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.id == CHRIS_ID:
            if "i made a doody" in message.content.lower() and not self.chris_responder:
                self.chris_responder = False
                response = "Ooh, wee! I think the cheesecake needs a break!"
                await message.channel.send(response)
                return
            elif self.chris_responder:
                chris = "Ooh, wee! Nice comment there, cheesecake!"
                await message.channel.send(chris)

        if message.author.id == ROB_ID:
            if "i made a doody" in message.content.lower() and not self.rob_responder:
                self.rob_responder = False
                response = "Ooh, wee! I think Rob is looking for a break from all the awesome tunes!"
                await message.channel.send(response)
                return
            elif self.rob_responder:
                rob = (
                    "Ooh, wee! I hear you don't like this song!\n"
                    "https://www.youtube.com/watch?v=W1B_poM9l7M"
                )
                await message.channel.send(rob)

        if "rob" in message.content.lower():
            response = "Ooh, wee! I hear Rob doesn't miss!"
            await message.channel.send(response)
            return

        if "peter" in message.content.lower():
            response = "Ooh, wee!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "peter.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["balls", "duke", "nukem", "steel"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I've got balls of steel!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "nukem.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["spicy", "boi", "boy"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! That there's a spicy, spicy boi!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "spicyboi.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["peloton", "pelaton"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "Ooh, wee! Nobody's laughing at that Peloton ad anymore, are they?"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "peloton.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["garfielf", "garfield", "jon", "god", "nermal"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "Ooh, wee, Jon. You stupid fuck. How could you...Jon?\n"
                "You were my amigo, Jon. My muchaho, my compadre! Jon...\n"
                "...make me God! Being a celestial body is exhausting!\n"
                "I'm gonna eat everything!"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "garfielf.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["m16", "twisted", "sister", "guitar"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "OOH, WEE! I CARRIED AN M16 AND YOU...\n"
                "YOU CARRY THAT, THAT...GUITAR!!!"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "m16.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["damage", "flex", "seal"]

        if any(c in message.content.lower() for c in matches):
            response = "OOH, WEE! THAT'S A LOT OF DAMAGE!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "damage.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["guys", "shut", "fuck"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! Someone needs to shut their fucks!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "fucks.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        male_matches = ["adonis", "superman"]
        female_matches = ["adonia", "superwoman"]
        matches = male_matches + female_matches

        if any(c in message.content.lower() for c in matches):
            if any(c in message.content.lower() for c in male_matches):
                text = male_matches
            else:
                text = female_matches

            filename = f"{text[0]}.jpg"
            response = f"Ooh, wee! I'm pretty sure that's something an {text.pop(0)} {text.pop(0)} would do!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", filename), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I'm pretty sure that's something an adonia superwoman would do!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "adonia.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["xp", "dr", "doctor", "evil", "million", "dollars"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee, Scott! That was...\nONE MEEELLION XP! That's a lot of frickin' XP!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "drevil.gif"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, Wee!"
            await message.channel.send(response)

    @commands.command()
    async def ole(self, ctx):
        response = "Ooh, wee!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "ole.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def gay(self, ctx):
        response = "Ooh, wee! Here's how gay that shot was!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", random.choice(GAY_FILES)),
            "rb",
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def shakira(self, ctx):
        response = "Ooh, wee! I hear her hips don't lie!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "shakira.mp4"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def oof(self, ctx):
        response = "Ooh, wee! That was oof-worthy!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "oof.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def wtf(self, ctx):
        response = "Ooh, wee! What the fuck?"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "wtf.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def nice(self, ctx):
        response = "Ooh, wee! That was pretty nice!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "nice.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def opinion(self, ctx):
        response = "Ooh, wee! Here's what you can do with your opinion!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "opinion.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def waiting(self, ctx):
        response = "Ooh, wee! Someone's taking their sweet-ass time today!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "waiting.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def sleep(self, ctx):
        response = "Ooh, wee! Looks like somebody needs their beauty sleep!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "sleep.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def help(self, ctx):
        response = "Ooh, wee! Somebody clearly doesn't know how this all works!\nClearly I'm going to need to help you out here!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "help.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        helpmessage = """Ooh, wee! Here's some commands you can run:
                      !ole - For when you feel festive after shooting a Fiesta!
                      !gay - For when you feel fabulous after shooting a Rainbow!
                      !shakira - For when Rob feels the need to do a dance after a good shot!
                      !oof - There are some times that just call for an oof!
                      !wtf - For when you inevitably say this 400 times a night!
                      !nice - For when you can't even shit talk that shot because it was nice!
                      !opinion - For those unsolicited opinions you didn't ask for!
                      !waiting - For when you're waiting on the one slow person to come online!
                      !sleep - For when someone needs to go to bed and it's clearly too early!

                      I also pay attention to what you're saying on Discord and will respond
                      when you say something I was told to respond to! For example, I'll always
                      talk back when you say 'ooh' or 'wee'. Ooh, wee!

                      You might also be super lucky and have me say something to EVERYTHING
                      you say! Ooh, wee! But if you get tired of that, just make sure to say
                      'I made a doody' and I'll cut you a break! Ooh, wee!"""
        await ctx.channel.send(helpmessage)
        return
