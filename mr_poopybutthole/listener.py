import discord
import os
import logging
import random
import re
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
        self.listeners = yaml.load(open(LISTENERS_FILE), Loader=yaml.Loader)

    async def _send_message(self, message, listener):
        """
        Sends a standard message containing a text response and an optional picture.
        The routine will check `message` for all `matches` specified for the `listener`.
        If a match is found, it will respond with the `response` text and return `True`
        to the calling function, otherwise it will return `False`.

        The command optionally supports an image to be posted specified by `filename`
        for the `listener`, and also supports posting a random picture specified by a
        list under `filenames`.
        """
        lst = self.listeners[listener]
        for c in lst["matches"]:
            if re.search(r"\b" + re.escape(c) + r"\b", message.content.lower()):
                if "response" in lst:
                    await message.channel.send(lst["response"])

                if "filename" in lst:
                    with open(os.path.join(RESOURCES_DIR, lst["filename"]), "rb") as file:
                        picture = discord.File(file)
                        await message.channel.send(file=picture)

                if "filenames" in lst:
                    with open(
                        os.path.join(RESOURCES_DIR, random.choice(lst["filenames"])),
                        "rb",
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
            if await self._send_message(message, listener):
                return

        if message.content.lower() in "._.":
            await message.channel.send("ಠ_ಠ")

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, wee!"
            await message.channel.send(response)
            self.logger.info(
                f"Sent default oohwee listener to {message.channel.name} "
                + f"channel due to {message.author.name}!"
            )
