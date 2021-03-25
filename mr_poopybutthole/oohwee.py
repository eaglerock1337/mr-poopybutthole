import discord
import os
import logging
import random

from discord.ext import commands


GAY_FILES = ["gay1.jpg", "gay2.jpg", "gay3.jpg", "gay4.jpg", "gay5.jpg", "gay6.jpg"]


HELPMESSAGES = [
    """Here's the commands you can run! Ooh, wee!
    ```!ole       !gay       !shakira   !oof       !wtf
!nice      !damage    !xp        !dialedin  !opinion
!dumb      !stfu      !waiting   !sleep     !scotch
!waldo     !notgood   !more      !welp      !igotthis
!neener    !ettu      !latifi    !ihateyou  !sorry
!fu        !fu2       !torvalds  !triggered !fuckmas
!ight      !ffs       !nope      !letsgo    !halp
!orly      !yarly     !nowai     !owls      !idgaf
!engineer  !win       !hattip    !bobross   !butts
!ace       !wam```""",
    """I also pay attention to what you're saying on Discord and will respond
when you say something I was told to respond to! For example, I'll always
talk back when you say `ooh` or `wee`. Also, if you just so happen to be an
`adonis` `superman` or an `adonia` `superwoman`, I'll make sure to comment
on that too! Ooooooooooh, wee!

`Snowflake Mode`""",
    """Finally, for all of those special snowflakes out there, we have a special
`SNOWFLAKE MODE` that will use my best microagressions and my bot privilege to
marginalize the best of you out there! Just type `!snowflake` to dial up the fun!
If you're lucky enough, you'll get a nice response from me to EVERYTHING you say!

If it's too much for you, just be sure to type `I made a doody`, and I'll make
sure you get to retreat to your safe space! You can even type `!snowflakes` to see
who can and can't take the heat! Finally, if everyone is going to ragequit because
of the trollfest, typing `!snowflake off` will make me check my privilege!
Ooooooooooooooooh, wee! Bots are fun, aren't they?""",
]


class Oohwee(commands.Cog):
    """
    The primary class for the Mr. Poopybutthole Discord bot.

    Hands the base commands that make up the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"Oooh, wee! {self.bot.user.name} has connected to Discord!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f"Oooh, wee! {member.name} has joined the server!\nType `!help` to learn more about me!"
        )

    @commands.command()
    async def help(self, ctx):
        response = (
            "Ooh, wee! Somebody clearly doesn't know how this all works!\n"
            + "Clearly I'm going to need to help you out here!"
        )
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "oohwee.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

        for helpmessage in HELPMESSAGES:
            await ctx.channel.send(helpmessage)

    @commands.command()
    async def gay(self, ctx):
        response = "Ooh, wee! Here's how gay that shot was!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", random.choice(GAY_FILES)),
            "rb",
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)
