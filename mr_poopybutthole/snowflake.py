import discord
import os
import logging
import yaml

from discord.ext import commands
from time import sleep

from .constants import (
    FOOTER_TEXT,
    ICON_URL,
    IMAGE_URL_HEADER,
    RESOURCES_DIR,
    REPO_URL,
    SNOWFLAKE_EMOJI,
    SNOWFLAKES_FILE,
)


class Snowflake(commands.Cog):
    """
    The Snowflake class for the Mr. Poopybutthole Discord bot.

    Hands the commands and autoresponder for Snowflake Mode.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot

        snowflake_data = yaml.load(open(SNOWFLAKES_FILE), Loader=yaml.Loader)
        self.commands = snowflake_data["commands"]
        self.thelist = snowflake_data["snowflakes"]
        self.safephrase = snowflake_data["safephrase"].lower()

        self.snowflake_list = {}
        for snowflake in self.thelist.keys():
            self.snowflake_list[snowflake] = True
        self.snowflake_mode = False

    async def _set_snowflake_name(self, snowflake, member, reset=False):
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

    async def _set_snowflake_names(self, guild, reset=False):
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
                await self._set_snowflake_name(self.thelist[snowflake], member, reset)

    async def _send_snowflake_embed(self, ctx, command):
        """
        Generates the embed message for Snowflake Mode. Parses the 
        """
        if self.snowflake_mode:
            color = discord.Color.red()
            status = "Enabled"
        else:
            color = discord.Color.green()
            status = "Disabled"

        if command == "safespace":
            description = self.thelist[ctx.author.id]["disable"]
        else:
            description = self.commands[command]["response"]

        image = os.path.join(IMAGE_URL_HEADER, self.commands[command]["filename"])

        embed = discord.Embed(
            title=f"Snowflake Mode - {status}",
            url=REPO_URL,
            description=description,
            color=color,
        )
        embed.set_author(
            name=f"Oooowee, {ctx.author.name}!", icon_url=ctx.author.avatar_url
        )
        embed.set_thumbnail(url=ICON_URL)
        embed.set_image(url=image)
        embed.set_footer(icon_url=ICON_URL, text=FOOTER_TEXT)

        enabled_text = disabled_text = ""
        for snowflake in self.thelist.keys():
            snowflake_text = f"{self.thelist[snowflake]['name']}: <@{snowflake}>\n"
            if self.snowflake_list[snowflake]:
                enabled_text += snowflake_text
            else:
                disabled_text += snowflake_text

        enabled_text = "None" if enabled_text == "" else enabled_text
        disabled_text = "None" if disabled_text == "" else disabled_text

        embed.add_field(name="Current Status:", value=status, inline=False)
        embed.add_field(
            name="Danger Zone Snowflakes:", value=enabled_text, inline=False
        )
        embed.add_field(
            name="Safe Space Snowflakes:", value=disabled_text, inline=False
        )
        embed.add_field(
            name="Current Safe Phrase:", value=f"`{self.safephrase}`", inline=False
        )
        embed.add_field(
            name="For help:",
            value="Type `!help snowflake` for more info on Snowflake Mode! Ooooooh, wee!",
            inline=False,
        )

        await ctx.channel.send(embed=embed)
        self.logger.info(f"Sent Snowflake Mode status embed to {ctx.channel.name}!")

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        The main listener routine that Snowflake Mode uses to respond to users.
        The routine will check if Snowflake Mode is enabled, and send a message
        if the user hasn't retreated to their safe space, as well as change their
        nickname. If they type the safe phrase message, the user will retreat to their
        safe space by disabling Snowflake Mode for them and resetting their nickname. 
        """
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

        if self.snowflake_mode:
            if message.author.id in self.thelist:
                snowflake = self.thelist[message.author.id]
                sleep(1)

                if self.snowflake_list[message.author.id]:
                    if self.safephrase in message.content.lower():
                        self.snowflake_list[message.author.id] = False

                        await message.channel.send(snowflake["disable"])
                        with open(
                            os.path.join(RESOURCES_DIR, "safespace.gif"), "rb",
                        ) as file:
                            picture = discord.File(file)
                            await message.channel.send(file=picture)

                        member = await message.guild.fetch_member(message.author.id)
                        await self._set_snowflake_name(snowflake, member, reset=True)
                        self.logger.info(
                            f"{snowflake['name']} retreated to their safe space!"
                        )

                    else:
                        response = f"{snowflake['message']}\n{snowflake['video']}"
                        await message.channel.send(response)

                        member = await message.guild.fetch_member(message.author.id)
                        await self._set_snowflake_name(snowflake, member)
                        self.logger.info(
                            f"Bugged {snowflake['name']} in {message.channel.name}!"
                        )
                else:
                    for char in SNOWFLAKE_EMOJI:
                        await message.add_reaction(char)
                    self.logger.info(
                        f"Add reactions to {snowflake['name']} in {message.channel.name}!"
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
                self._set_snowflake_name(after.id, after)

    @commands.command()
    async def snowflake(self, ctx, arg="status"):
        """
        The main !snowflake command, that has five options:

        `status` (default) - get a status on Snowflake Mode (same as `!snowflakes`)

        `on` - enable Snowflake Mode for all users that have not retreated to
        their safe space, and change their nicknames.

        `off` - disable Snowflake Mode for all users and reset all nicknames.

        `safespace` - disable Snowflake Mode for a specific user and retreat to their safe space.

        `force` - enable Snowflake Mode for all users, even those that have explicitly
        retreated to their safe space. Can only be invoked by snowflakes!
        """
        arg = arg.lower()

        # Command conditionals
        if arg == "on":
            self.snowflake_mode = True
            await self._set_snowflake_names(ctx.message.guild)
            self.logger.info(
                f"{ctx.author.name} enabled Snowflake Mode in {ctx.channel.name}!"
            )

        elif arg == "off":
            if ctx.author.id in self.thelist and self.snowflake_list[ctx.author.id]:
                response = (
                    f"You can't turn off Snowflake Mode, {ctx.author.name}! "
                    + "You should try retreating to your safe space first! Ooh, wee!"
                )
                await ctx.channel.send(response)
                self.logger.info(
                    f"Snowflake {ctx.author.name} tried to turn off Snowflake Mode "
                    + f"in {ctx.channel.name} but isn't in their safe space!"
                )
                return

            self.snowflake_mode = False
            await self._set_snowflake_names(ctx.message.guild, reset=True)
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

            await self._set_snowflake_names(ctx.message.guild)
            self.logger.info(
                f"Snowflake {ctx.author.name} forced Snowflake Mode in {ctx.channel.name}!"
            )

        elif arg == "safespace":
            self.snowflake_list[ctx.author.id] = False
            self.logger.info(f"{ctx.author.name} retreated to their safe space!")

        elif arg == "brave":
            self.snowflake_list[ctx.author.id] = True
            self.logger.info(
                f"Brave snowflake {ctx.author.name} emerged from their safe space!"
            )

        elif arg == "status":
            self.logger.info(
                f"{ctx.author.name} requested Snowflake Mode status in {ctx.channel.name}!"
            )

        # Display conditionals
        if arg in self.commands:
            await self._send_snowflake_embed(ctx, arg)

        else:
            response = f"Hey {ctx.author.name}, try to get the command right next time! Oooooh, wee!"
            await ctx.channel.send(response)
            self.logger.info(
                f"{ctx.author.name} doesn't know how to use the snowflake command!"
            )

    @commands.command()
    async def snowflakes(self, ctx):
        """
        The !snowflakes command, which will print out some status info on Snowflake Mode,
        such as whether it is enabled, and what users have retreated to their safe space.
        """
        await self._send_snowflake_embed(ctx, "status")
