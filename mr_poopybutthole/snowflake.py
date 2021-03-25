import discord
import os
import logging
import yaml

from discord.ext import commands
from time import sleep

from .constants import RESOURCES_DIR, SNOWFLAKES_FILE


class Snowflake(commands.Cog):
    """
    The Snowflake class for the Mr. Poopybutthole Discord bot.

    Hands the commands and autoresponder for Snowflake Mode.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.thelist = yaml.load(open(SNOWFLAKES_FILE), Loader=yaml.FullLoader)
        self.snowflake_list = {} 
        for snowflake in self.thelist.keys():
            self.snowflake_list[snowflake] = True
        self.snowflake_mode = False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

        if self.snowflake_mode:
            if message.author.id in self.thelist.keys():
                snowflake = self.thelist[message.author.id]
                if self.snowflake_list[message.author.id]:
                    sleep(1)
                    if "i made a doody" in message.content.lower():
                        self.snowflake_list[message.author.id] = False
                        await message.channel.send(snowflake["disable"])
                        with open(
                            os.path.join(RESOURCES_DIR, "safespace.gif"), "rb",
                        ) as file:
                            picture = discord.File(file)
                            await message.channel.send(file=picture)
                        return
                    else:
                        response = f"{snowflake['message']}\n{snowflake['video']}"
                        await message.channel.send(response)

    @commands.command()
    async def snowflake(self, ctx, arg="on"):
        if arg == "on":
            self.snowflake_mode = True
            response = "Ooh, wee! We're gonna get some people pissed off, tonight!"
            await ctx.channel.send(response)
            with open(os.path.join(RESOURCES_DIR, "snowflake.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        elif arg == "off":
            self.snowflake_mode = False
            response = "Ooh, wee! Looks like *all* the snowflakes need a break!"
            await ctx.channel.send(response)
            with open(os.path.join(RESOURCES_DIR, "privilege.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        elif arg == "force":
            self.snowflake_mode = True
            for snowflake in self.snowflake_list.keys():
                self.snowflake_list[snowflake] = True
            response = "Ooh, wee! Time for all your safe spaces to burn down!"
            await ctx.channel.send(response)
            with open(os.path.join(RESOURCES_DIR, "safespace.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

    @commands.command()
    async def snowflakes(self, ctx):
        response = "Ooh, wee! Let's see how the snowflakes are doing!"
        await ctx.channel.send(response)
        with open(os.path.join(RESOURCES_DIR, "snowflakes.jpg"), "rb") as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

        snowflake_mode = "enabled" if self.snowflake_mode else "disabled"
        response = (
            f"It looks like snowflake mode is currently {snowflake_mode}! Ooh, wee!\n"
        )

        if self.snowflake_mode:
            enabled_snowflakes = []
            disabled_snowflakes = []
            for snowflake in self.thelist.keys():
                if self.snowflake_list[snowflake]:
                    enabled_snowflakes.append(snowflake)
                else:
                    disabled_snowflakes.append(snowflake)

            if len(enabled_snowflakes) > 0:
                response += "\nThe following snowflakes better watch out:\n"
                for snowflake in enabled_snowflakes:
                    response += f"{self.thelist[snowflake]['name']}: <@{snowflake}>\n"

            if len(disabled_snowflakes) > 0:
                response += "\nThese snowflakes had to retreat to their safe space:\n"
                for snowflake in disabled_snowflakes:
                    response += f"{self.thelist[snowflake]['name']}: <@{snowflake}>\n"

            response += (
                "\nRemember snowflakes, just type `i made a doody` if the victimization "
                + "is too much and you need to go to your safe space! Ooooooh, wee!"
            )

        await ctx.channel.send(response)
