import discord
import os
import logging
import yaml

from datetime import datetime
from discord.ext import commands

from .constants import (
    COMMANDS_FILE,
    HELP_FILE,
    LISTENERS_FILE,
    MAIN_CHANNEL,
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
        self.commands = yaml.load(open(COMMANDS_FILE), Loader=yaml.FullLoader)
        self.listeners = yaml.load(open(LISTENERS_FILE), Loader=yaml.FullLoader)
        self.cmdlist = sorted(self.commands)
        self.listlist = sorted(self.listeners)

    def generate_embed(self, command):
        """
        Generate a help message for the `!help` command. Will format the message based on the
        command given and the data in the help YAML file, then return the embed to the
        calling function.
        """
        title = self.help["commands"][command]["title"]
        description = self.help["commands"][command]["description"]
        footer_text = f"Mr. Poopybutthole v{VERSION} (c) {datetime.now().year} EagleRock...Ooh, wee!"

        try:
            fields = self.help["commands"][command]["fields"]
        except KeyError:
            fields = False

        embed = discord.Embed(
            title=title,
            url=self.help["url"],
            description=description,
            color=discord.Color.blue(),
        )
        embed.set_author(
            name=self.help["name"], url=self.help["url"], icon_url=self.help["icon"],
        )
        embed.set_thumbnail(url=self.help["thumbnail"])
        embed.set_image(url=self.help["image"])
        embed.set_footer(text=footer_text)

        if command == "commands":
            for cmd in self.cmdlist:
                embed.add_field(name="\u200b", value=f"!{cmd}", inline=True)
        elif command == "listeners":
            for lst in self.listlist:
                matches = ""
                for match in self.listeners[lst]["matches"]:
                    matches += f"*'{match}'* "
                embed.add_field(name=f"{lst}", value=matches, inline=True)

        if fields:
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
    async def help(self, ctx, arg="legacy"):
        """
        The help message for Mr. Poopybutthole. supports the main command, as well as
        all subcommands, such as `!help commands`. Formats the message using a Discord
        embed and posts the message to the channel.
        """
        cmd = arg if arg in self.help["commands"] else "main"
        embed = self.generate_embed(cmd)
        await ctx.channel.send(embed=embed)
