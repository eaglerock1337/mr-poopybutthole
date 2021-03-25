import discord
import os
import logging
import yaml

from discord.ext import commands

from .constants import COMMANDS_FILE, RESOURCES_DIR


class Command(commands.Cog):
    """
    The command class for the Mr. Poopybutthole Discord bot.

    Hands all meme commands that follow the basic format:
    - Uses one specific command to be triggered (e.g. '!fu')
    - Returns a statement and an optional image to the channel
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.commands = yaml.load(open(COMMANDS_FILE), Loader=yaml.FullLoader)

    async def send_command(self, message, command):
        """
        Sends a standard command response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name.
        Takes the message info, and response with the given message and filename.
        """
        cmd = self.commands[command]
        await message.channel.send(cmd["response"])
        if "filename" in cmd:
            with open(os.path.join(RESOURCES_DIR, cmd["filename"]), "rb") as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
        self.logger.info(
            f"Member {message.author.name} sent !{command} "
            + f"to the {message.channel.name} channel!"
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Main routine for generic meme commands for Mr. Poopybutthole. Verifies
        the command is in fact a command, grabs the text immediately after the !,
        and checks the command set for a match, sending the meme if matched.
        """
        if message.author == self.bot.user:
            return

        if not message.content.startswith("!"):
            return

        command = message.content[1:].split(" ")[0]
        if command in self.commands:
            await self.send_command(message, command)
