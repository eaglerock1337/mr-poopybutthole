import discord
import os
import logging

from discord.ext import commands
from time import sleep


CHRIS_ID = 533873187780558848
PETER_ID = 246837076987871233
ROB_ID = 445052623171878912


SNOWFLAKES = {
    CHRIS_ID: {
        "name": "Chris",
        "message": "Ooh, wee! Nice comment there, cheesecake!",
        "video": "https://www.youtube.com/watch?v=FK6Rjt4uCIw",
        "disable": "Ooh, wee! I think the cheesecake needs a break!",
    },
    PETER_ID: {
        "name": "Peter",
        "message": "Ooh, wee! Time for the elitist to get a taste of his own medicine!",
        "video": "https://www.youtube.com/watch?v=f5k3PGn6DbQ",
        "disable": "Ooh, wee! Look who can dish it out but can't take it!",
    },
    ROB_ID: {
        "name": "Rob",
        "message": "Ooh, wee! I hear you don't like this song!",
        "video": "https://www.youtube.com/watch?v=W1B_poM9l7M",
        "disable": "Ooh, wee! I think Rob is looking for a break from all the awesome tunes!",
    },
}


class Snowflake(commands.Cog):
    """
    The Snowflake class for the Mr. Poopybutthole Discord bot.

    Hands the commands and autoresponder for Snowflake Mode.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot
        self.snowflake_list = {}
        for snowflake in SNOWFLAKES.keys():
            self.snowflake_list[snowflake] = True
        self.snowflake_mode = False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

        if self.snowflake_mode:
            if message.author.id in SNOWFLAKES.keys():
                snowflake = SNOWFLAKES[message.author.id]
                if self.snowflake_list[message.author.id]:
                    sleep(1)
                    if "i made a doody" in message.content.lower():
                        self.snowflake_list[message.author.id] = False
                        await message.channel.send(snowflake["disable"])
                        with open(
                            os.path.join(
                                "mr_poopybutthole", "resources", "safespace.gif"
                            ),
                            "rb",
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
            with open(
                os.path.join("mr_poopybutthole", "resources", "snowflake.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        elif arg == "off":
            self.snowflake_mode = False
            response = "Ooh, wee! Looks like *all* the snowflakes need a break!"
            await ctx.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "privilege.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

        elif arg == "force":
            self.snowflake_mode = True
            for snowflake in self.snowflake_list.keys():
                self.snowflake_list[snowflake] = True
            response = "Ooh, wee! Time for all your safe spaces to burn down!"
            await ctx.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "safespace.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

    @commands.command()
    async def snowflakes(self, ctx):
        response = "Ooh, wee! Let's see how the snowflakes are doing!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "snowflakes.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

        snowflake_mode = "enabled" if self.snowflake_mode else "disabled"
        response = (
            f"It looks like snowflake mode is currently {snowflake_mode}! Ooh, wee!\n"
        )

        if self.snowflake_mode:
            enabled_snowflakes = []
            disabled_snowflakes = []
            for snowflake in SNOWFLAKES.keys():
                if self.snowflake_list[snowflake]:
                    enabled_snowflakes.append(snowflake)
                else:
                    disabled_snowflakes.append(snowflake)

            if len(enabled_snowflakes) > 0:
                response += "\nThe following snowflakes better watch out:\n"
                for snowflake in enabled_snowflakes:
                    response += f"{SNOWFLAKES[snowflake]['name']}: <@{snowflake}>\n"

            if len(disabled_snowflakes) > 0:
                response += "\nThese snowflakes had to retreat to their safe space:\n"
                for snowflake in disabled_snowflakes:
                    response += f"{SNOWFLAKES[snowflake]['name']}: <@{snowflake}>\n"

            response += (
                "\nRemember snowflakes, just type `i made a doody` if the victimization "
                + "is too much and you need to go to your safe space! Ooooooh, wee!"
            )

        await ctx.channel.send(response)
