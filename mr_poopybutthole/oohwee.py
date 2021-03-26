import discord
import os
import logging
import numpy
import yaml

from datetime import datetime
from discord.ext import commands

from .constants import (
    COMMANDS_FILE,
    FOOTER_TEXT,
    HELP_FILE,
    HELP_IMAGE_URL,
    ICON_URL,
    LISTENERS_FILE,
    MAIN_CHANNEL,
    REPO_URL,
    RESOURCES_DIR,
    VERSION,
)


class Oohwee(commands.Cog):
    """
    The primary class for the Mr. Poopybutthole Discord bot.

    Hands the base commands that make up the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.help = yaml.load(open(HELP_FILE), Loader=yaml.FullLoader)
        self.command_output = self._gen_command_output(COMMANDS_FILE, columns=2)
        self.listener_output = self._gen_listener_output(LISTENERS_FILE)

    def _get_command_arrays(self, file, columns):
        """
        Load the command list from the provided file and return as a list with
        `column` lists of evenly sorted columns for easy column printing. Also
        returns the total number of commands for printing in the embed.
        """
        commands = sorted(yaml.load(open(file), Loader=yaml.FullLoader))
        total = len(commands)
        split = numpy.array_split(commands, columns)
        lists = []
        for nparray in split:
            lists.append(nparray.tolist())
        for col in range(1, columns):
            lists[col].append("")
        return lists, total

    def _gen_command_output(self, file, columns=2):
        """
        Generate the `!help command` output string that contains all commands
        the bot supports. Calls the `_get_command_arrays()` class function to
        organize the commands in `file` into an array, then formats the block
        of commands as a string to include in the embed for the help command.
        """
        cmds, total = self._get_command_arrays(file, columns)
        cols = len(cmds)
        rows = len(cmds[0])

        output = "```\n"
        for row in range(rows):
            for col in range(cols):
                output += "" if cmds[col][row] == "" else f"!{cmds[col][row]:12}"
            output += "\n"
        output += f"```\nTotal Commands: **{total}**\n"
        return output

    def _gen_listener_output(self, file):
        """
        Generate the `!help listeners` output string that contains all the listeners
        the bot supports and their respective triggers. Obtains a sorted list of
        listeners from `file` and renders the list, one listener per line, with all
        the matchers listed.
        """
        listeners = yaml.load(open(file), Loader=yaml.FullLoader)
        sorted_listeners = sorted(listeners)

        output = "\n\n"
        for lst in sorted_listeners:
            output += f"**`{lst:8}`** -"
            for match in range(len(listeners[lst]["matches"])):
                output += "" if match == 0 else ","
                output += f" *'{listeners[lst]['matches'][match]}'*"
            output += "\n"
        output += f"\nTotal Listeners: **{len(sorted_listeners)}**\n"
        return output

    def _generate_embed(self, command, author):
        """
        Generate a help message for the `!help` command. Will format the message based on the
        command given and the data in the help YAML file, then return the embed to the
        calling function.
        """
        try:
            fields = self.help[command]["fields"]
        except KeyError:
            fields = {}

        title = self.help[command]["title"]
        use_image = self.help[command]["image"]
        description = self.help[command]["description"]

        if command == "commands":
            description += self.command_output
        elif command == "listeners":
            description += self.listener_output

        embed = discord.Embed(
            title=title,
            url=REPO_URL,
            description=description,
            color=discord.Color.blue(),
        )
        embed.set_author(name=f"Oooowee, {author.name}!", icon_url=author.avatar_url)
        embed.set_thumbnail(url=ICON_URL)
        embed.set_footer(icon_url=ICON_URL, text=FOOTER_TEXT)

        if use_image:
            embed.set_image(url=HELP_IMAGE_URL)

        for field in fields:
            embed.add_field(
                name=f"`{fields[field]['name']}`",
                value=fields[field]["value"],
                inline=False,
            )

        return embed

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Mr. Poopybutthole's introduction when the bot goes online. Sends a message to
        the main channel as specified in the `constants.py` file.
        """
        channel = await self.bot.fetch_channel(MAIN_CHANNEL)
        await channel.send(f"Ooh, wee! Mr. Poopybutthole v{VERSION} is online!")
        self.logger.info(f"Oooh, wee! {self.bot.user.name} has connected to Discord!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        A greeter message from Mr. Poopybutthole when someone joins the server. Sends a
        DM to the user as well as a message to the main channel specified in the
        `constants.py` file.
        """
        channel = await self.bot.fetch_channel(MAIN_CHANNEL)
        await channel.send(f"Ooh, wee! {member.name} has joined the Discord!!")
        await member.create_dm()
        await member.dm_channel.send(
            f"Oooh, wee! Welcome to the server, {member.name}! I'm Mr. Poopybutthole!\n"
            + "Type `!help` to learn more about me, and have fun! Oooooooh, wee!"
        )

    @commands.command()
    async def help(self, ctx, arg="main"):
        """
        The help message for Mr. Poopybutthole. supports the main command, as well as
        all subcommands, such as `!help commands`. Formats the message using a Discord
        embed and posts the message to the channel.
        """
        if arg not in self.help:
            response = f"Hey {ctx.author.name}, try to get the command right next time! Oooooh, wee!"
            await ctx.channel.send(response)

            self.logger.info(
                f"{ctx.author.name} doesn't know how to use the help command!"
            )
            return

        embed = self._generate_embed(arg, ctx.author)
        await ctx.channel.send(embed=embed)
