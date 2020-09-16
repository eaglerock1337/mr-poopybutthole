import discord
import os
import logging
import random

from discord.ext import commands
from dotenv import load_dotenv


CHRIS_ID = 533873187780558848
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

        if "rob" in message.content.lower():
            response = "Ooh, wee! I hear Rob doesn't miss!"
            await message.channel.send(response)
            return

        if "peter" in message.content.lower():
            response = "Ooh, wee!"
            await message.channel.send(response)
            with open(os.path.join("mr_poopybutthole", "resources", "peter.jpg"), "rb") as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["balls", "duke", "nukem", "steel"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I've got balls of steel!"
            await message.channel.send(response)
            with open(os.path.join("mr_poopybutthole", "resources", "nukem.png"), "rb") as file:
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
            with open(os.path.join("mr_poopybutthole", "resources", filename), "rb") as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I'm pretty sure that's something an adonia superwoman would do!"
            await message.channel.send(response)
            with open(os.path.join("mr_poopybutthole", "resources", "adonia.jpg"), "rb") as file:
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
        with open(os.path.join("mr_poopybutthole", "resources", "ole.jpg"), "rb") as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return

    @commands.command()
    async def gay(self, ctx):
        response = "Ooh, wee! Here's how gay that shot was!"
        await ctx.channel.send(response)
        with open(os.path.join("mr_poopybutthole", "resources", random.choice(GAY_FILES)), "rb") as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
        return