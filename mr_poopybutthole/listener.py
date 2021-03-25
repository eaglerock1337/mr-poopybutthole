import discord
import os
import logging
import random
import yaml

from discord.ext import commands


LISTENERS_FILE = os.path.join(os.path.dirname(__file__), "listeners.yaml")


class Listener(commands.Cog):
    """
    The listener class for the Mr. Poopybutthole Discord bot.

    Hands all listener commands and autoresponses from the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.listeners = yaml.load(open(LISTENERS_FILE), Loader=yaml.FullLoader)
        self.listset = set(self.listeners)

    @commands.Cog.listener()
    async def send_message(self, message, listener):
        """
        Sends a standard message response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name, and
        retrieves the matches, response, and tests if it should send based on the matches.
        Returns true if the match was successful, false otherwise.
        """
        lst = self.listeners[listener]
        if any(c in message.content.lower() for c in lst["matches"]):
            await message.channel.send(lst["response"])
            if "filename" in lst:
                with open(
                    os.path.join("mr_poopybutthole", "resources", lst["filename"]), "rb"
                ) as file:
                    picture = discord.File(file)
                    await message.channel.send(file=picture)
            self.logger.info(
                f"Sent {listener} listener to {message.channel.name} "
                + f"channel due to {message.author.name}!"
            )
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

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

        # This should probably become a command later on, but leave it for now
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

        for listener in self.listset:
            if await self.send_message(message, listener):
                return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, wee!"
            await message.channel.send(response)
