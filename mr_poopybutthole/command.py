import discord
import os
import logging
import yaml

from discord.ext import commands


COMMANDS_FILE = os.path.join(os.path.dirname(__file__), "commands.yaml")


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
        self.cmdset = set(self.commands)

    @commands.command()
    async def send_command(self, ctx, command):
        """
        Sends a standard command response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name.
        Takes the message info, and response with the given message and filename.
        """
        cmd = self.commands[command]
        await ctx.channel.send(cmd["response"])
        if "filename" in cmd:
            with open(
                os.path.join("mr_poopybutthole", "resources", cmd["filename"]), "rb"
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)
        self.logger.info(
            f"Member {ctx.author.name} sent !{command} "
            + f"to the {ctx.channel.name} channel!"
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if not message.content.startswith("!"):
            return

        command = message.content[1:].split(" ")[0]

        if command in self.cmdset:
            await self.send_command(message, command)
