import discord
import os
import logging
import random
import yaml

from discord.ext import commands

from .constants import LISTENERS_FILE, RESOURCES_DIR


class Listener(commands.Cog):
    """
    The listener class for the Mr. Poopybutthole Discord bot.

    Hands all listener commands and autoresponses from the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.listeners = yaml.load(open(LISTENERS_FILE), Loader=yaml.FullLoader)

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
                with open(os.path.join(RESOURCES_DIR, lst["filename"]), "rb") as file:
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
        """
        Main listener routine for Mr. Poopybutthole. Will follow all special-case
        listening rules, as well as parse the list of all listeners in the yaml
        file, sending a message to Discord if matched. 
        """
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

        for listener in self.listeners.keys():
            if await self.send_message(message, listener):
                return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, wee!"
            await message.channel.send(response)
            self.logger.info(
                f"Sent default oohwee listener to {message.channel.name} "
                + f"channel due to {message.author.name}!"
            )
