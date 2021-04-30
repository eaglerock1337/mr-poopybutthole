import discord
import os
import logging
import random
import re
import yaml

from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

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
        self.commands = yaml.load(open(COMMANDS_FILE), Loader=yaml.Loader)

    async def _send_command(self, ctx, command):
        """
        Sends a standard command response consisting of a text `response`. Also supports
        posting a file specified by `filename` or posting a random file listed in
        `filenames`. Retrieves the information from the command list and posts the
        specified information to the channel.
        """
        cmd = self.commands[command]
        await ctx.channel.send(cmd["response"])

        if "filename" in cmd:
            with open(os.path.join(RESOURCES_DIR, cmd["filename"]), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        if "filenames" in cmd:
            with open(
                os.path.join(RESOURCES_DIR, random.choice(cmd["filenames"])),
                "rb",
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        self.logger.info(
            f"Member {ctx.message.author.name} sent !{command} "
            + f"to the {ctx.channel.name} channel!"
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        This function handles all commands defined in the commands YAML file and
        stored in self.commands in the Command class. It does this by hijacking
        all `CommandNotFound` errors the bot receives by listening for all
        `on_command_error()` Discord events as follows:

        First, check that the error is a CommandNotFound type. Second, use the
        `re.findall()` command to grab the command from the error text, which will
        look something like this:

        `discord.ext.commands.errors.CommandNotFound: Command "oohwee" is not found`

        Second, use the `re.findall()` regex function to parse the first result in
        the error text that's inside quotes, which will be the command name.

        Finally, check the command against the imported command list, and
        invoke the `send_command()` function if found. Otherwise, raise the error
        normally and avoid swallowing unnecesary errors.
        """
        if isinstance(error, CommandNotFound):
            # Grab command name from the error output
            command = re.findall(r'"(.*?)"', str(error))[0]
            if command in self.commands:
                await self._send_command(ctx, command)
                return
        raise error
