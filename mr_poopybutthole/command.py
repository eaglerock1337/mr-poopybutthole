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

    @commands.command()
    async def ole(self, ctx):
        await self.send_command(ctx, "ole")

    @commands.command()
    async def shakira(self, ctx):
        await self.send_command(ctx, "shakira")

    @commands.command()
    async def oof(self, ctx):
        await self.send_command(ctx, "oof")

    @commands.command()
    async def wtf(self, ctx):
        await self.send_command(ctx, "wtf")

    @commands.command()
    async def nice(self, ctx):
        await self.send_command(ctx, "nice")

    @commands.command()
    async def damage(self, ctx):
        await self.send_command(ctx, "damage")

    @commands.command()
    async def xp(self, ctx):
        await self.send_command(ctx, "xp")

    @commands.command()
    async def dialedin(self, ctx):
        await self.send_command(ctx, "dialedin")

    @commands.command()
    async def opinion(self, ctx):
        await self.send_command(ctx, "opinion")

    @commands.command()
    async def dumb(self, ctx):
        await self.send_command(ctx, "dumb")

    @commands.command()
    async def stfu(self, ctx):
        await self.send_command(ctx, "stfu")

    @commands.command()
    async def waiting(self, ctx):
        await self.send_command(ctx, "waiting")

    @commands.command()
    async def sleep(self, ctx):
        await self.send_command(ctx, "sleep")

    @commands.command()
    async def scotch(self, ctx):
        await self.send_command(ctx, "scotch")

    @commands.command()
    async def waldo(self, ctx):
        await self.send_command(ctx, "waldo")

    @commands.command()
    async def yourmom(self, ctx):
        await self.send_command(ctx, "yourmom")

    @commands.command()
    async def notgood(self, ctx):
        await self.send_command(ctx, "notgood")

    @commands.command()
    async def more(self, ctx):
        await self.send_command(ctx, "more")

    @commands.command()
    async def welp(self, ctx):
        await self.send_command(ctx, "welp")

    @commands.command()
    async def igotthis(self, ctx):
        await self.send_command(ctx, "igotthis")

    @commands.command()
    async def neener(self, ctx):
        await self.send_command(ctx, "neener")

    @commands.command()
    async def ettu(self, ctx):
        await self.send_command(ctx, "ettu")

    @commands.command()
    async def latifi(self, ctx):
        await self.send_command(ctx, "latifi")

    @commands.command()
    async def ihateyou(self, ctx):
        await self.send_command(ctx, "ihateyou")

    @commands.command()
    async def sorry(self, ctx):
        await self.send_command(ctx, "sorry")

    @commands.command()
    async def fu(self, ctx):
        await self.send_command(ctx, "fu")

    @commands.command()
    async def fu2(self, ctx):
        await self.send_command(ctx, "fu2")

    @commands.command()
    async def torvalds(self, ctx):
        await self.send_command(ctx, "torvalds")

    @commands.command()
    async def triggered(self, ctx):
        await self.send_command(ctx, "triggered")

    @commands.command()
    async def fuckmas(self, ctx):
        await self.send_command(ctx, "fuckmas")

    @commands.command()
    async def ight(self, ctx):
        await self.send_command(ctx, "ight")

    @commands.command()
    async def ffs(self, ctx):
        await self.send_command(ctx, "ffs")

    @commands.command()
    async def nope(self, ctx):
        await self.send_command(ctx, "nope")

    @commands.command()
    async def letsgo(self, ctx):
        await self.send_command(ctx, "letsgo")

    @commands.command()
    async def halp(self, ctx):
        await self.send_command(ctx, "halp")

    @commands.command()
    async def orly(self, ctx):
        await self.send_command(ctx, "orly")

    @commands.command()
    async def yarly(self, ctx):
        await self.send_command(ctx, "yarly")

    @commands.command()
    async def nowai(self, ctx):
        await self.send_command(ctx, "nowai")

    @commands.command()
    async def owls(self, ctx):
        await self.send_command(ctx, "owls")

    @commands.command()
    async def idgaf(self, ctx):
        await self.send_command(ctx, "idgaf")

    @commands.command()
    async def engineer(self, ctx):
        await self.send_command(ctx, "engineer")

    @commands.command()
    async def win(self, ctx):
        await self.send_command(ctx, "win")

    @commands.command()
    async def hattip(self, ctx):
        await self.send_command(ctx, "hattip")

    @commands.command()
    async def bobross(self, ctx):
        await self.send_command(ctx, "bobross")

    @commands.command()
    async def butts(self, ctx):
        await self.send_command(ctx, "butts")

    @commands.command()
    async def ace(self, ctx):
        await self.send_command(ctx, "ace")

    @commands.command()
    async def wam(self, ctx):
        await self.send_command(ctx, "wam")
