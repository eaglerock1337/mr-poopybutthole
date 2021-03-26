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

    async def set_snowflake_name(self, snowflake, member, reset=False):
        """
        Set or reset the nickname of a specific snowflake. Requires the
        snowflake name, their member object (which can be obtained from
        `guild.fetch_member()`), and sets or resets based on the input.

        This will skip Peter, since Discord bots are not granted any
        permissions to change Server Owner nicknames, and will throw an
        error if they try to do so.
        """
        if snowflake["name"] == "Peter":  # prevent errors :-(
            return

        if reset:
            await member.edit(nick=member.name)
            self.logger.info(f"Reset snowflake {snowflake['name']}'s nickname!")
        else:
            await member.edit(nick=snowflake["nickname"])
            self.logger.info(
                f"Set snowflake {snowflake['name']}'s nickname to {snowflake['nickname']}!"
            )

    async def set_snowflake_names(self, guild, reset=False):
        """
        Sets or resets the nicknames for all snowflakes that have not
        retreated to their safe space. Requires the guild object passed in
        either from `ctx.message.guild` or `message.guild` from the listener
        or command.

        The command will iterate through the snowflake list, setting or
        resetting each snowflake name based on the optional keyword arg.
        """
        for snowflake in self.thelist.keys():
            if self.snowflake_list[snowflake]:
                member = await guild.fetch_member(snowflake)
                await self.set_snowflake_name(self.thelist[snowflake], member, reset)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        The main listener routine that Snowflake Mode uses to respond to users.
        The routine will check if Snowflake Mode is enabled, and send a message
        if the user hasn't retreated to their safe space, as well as change their
        nickname. If they type the `i made a doody` safe space message, it will
        disable their Snowflake Mode and reset their nickname. 
        """
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

        if self.snowflake_mode:
            if message.author.id in self.thelist:
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
                        member = await message.guild.fetch_member(message.author.id)
                        await self.set_snowflake_name(snowflake, member, reset=True)
                        self.logger.info(
                            f"{snowflake.name} retreated to their safe space!"
                        )
                    else:
                        response = f"{snowflake['message']}\n{snowflake['video']}"
                        await message.channel.send(response)
                        member = await message.guild.fetch_member(message.author.id)
                        await self.set_snowflake_name(snowflake, member)
                        self.logger.info(
                            f"Bugged {snowflake.name} in {message.channel.name}!"
                        )

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """
        Listen for members trying to update their nickname. Prevent all snowflakes from
        updating their nickname unless Snowflake Mode is disabled or they have retreated
        to their safe space.

        Does not work for Peter, as bots cannot update nicknames for Server Owners.
        """
        if before.nickname == after.nickname:
            return

        if self.snowflake_mode and after.id in self.thelist:
            # Does not work with Server Owners, unfortunately
            if self.thelist[after.id]["name"] == "Peter":
                return

            if self.snowflake_list[after.id]:
                self.set_snowflake_name(after.id, after)

    @commands.command()
    async def snowflake(self, ctx, arg="on"):
        """
        The main !snowflake command, that has three options:

        `on` (default) - enable Snowflake Mode for all users that have not retreated to
        their safe space, and change their nicknames.

        `off` - disable Snowflake Mode for all users and reset all nicknames.

        `force` - enable Snowflake Mode for all users, even those that have explicitly
        retreated to their safe space. Can only be invoked by snowflakes!
        """
        if arg == "on":
            self.snowflake_mode = True
            response = "Ooh, wee! We're gonna get some people pissed off, tonight!"
            await ctx.channel.send(response)
            await self.set_snowflake_names(ctx.message.guild)
            with open(os.path.join(RESOURCES_DIR, "snowflake.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)
            self.logger.info(
                f"{ctx.author.name} enabled Snowflake Mode in {ctx.channel.name}!"
            )

        elif arg == "off":
            self.snowflake_mode = False
            response = "Ooh, wee! Looks like *all* the snowflakes need a break!"
            await ctx.channel.send(response)
            await self.set_snowflake_names(ctx.message.guild, reset=True)
            with open(os.path.join(RESOURCES_DIR, "privilege.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)
            self.logger.info(
                f"{ctx.author.name} disabled Snowflake Mode in {ctx.channel.name}!"
            )

        elif arg == "force":
            if ctx.author.id not in self.thelist:
                response = (
                    "Only fellow snowflakes can force Snowflake Mode on! Ooh, wee!"
                )
                await ctx.channel.send(response)
                self.logger.info(
                    f"{ctx.author.name} tried to force on Snowflake Mode in {ctx.channel.name}!"
                )
                return

            self.snowflake_mode = True
            for snowflake in self.snowflake_list.keys():
                self.snowflake_list[snowflake] = True

            response = "Ooh, wee! Time for all your safe spaces to burn down!"
            await ctx.channel.send(response)
            await self.set_snowflake_names(ctx.message.guild)
            with open(os.path.join(RESOURCES_DIR, "safespace.jpg"), "rb") as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)
            self.logger.info(
                f"{ctx.author.name} disabled Snowflake Mode in {ctx.channel.name}!"
            )

    @commands.command()
    async def snowflakes(self, ctx):
        """
        The !snowflakes command, which will print out some status info on Snowflake Mode,
        such as whether it is enabled, and what users have retreated to their safe space.
        """
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
