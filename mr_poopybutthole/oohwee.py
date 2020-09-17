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

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"Oooh, wee! {self.bot.user.name} has connected to Discord!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Oooh, Wee! {member.name} has joined the server!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.id == CHRIS_ID:
            chris = "Ooh, wee! Nice comment there, cheesecake!"
            await message.channel.send(chris)

        if message.author.id == ROB_ID:
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
