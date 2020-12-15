import discord
import os
import logging
import random

from discord.ext import commands
from dotenv import load_dotenv

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

GAY_FILES = ["gay1.jpg", "gay2.jpg", "gay3.jpg", "gay4.jpg", "gay5.jpg", "gay6.jpg"]

HELPMESSAGES = [
    """Here's the commands you can run! Ooh, wee!
    `!ole` - For when you feel festive after shooting a Fiesta!
    `!gay` - For when you feel fabulous after shooting a Rainbow!
    `!shakira` - For when Rob feels the need to do a dance after a good shot!
    `!oof` - There are some times that just call for an oof!
    `!wtf` - For when you inevitably say this 400 times a night!
    `!nice` - For when you can't even shit talk that shot because it was nice!
    `!damage` - Some shots do a lot of damage, and deserve it to be known!
    `!xp` - Some rounds generate a ton of XP! This is for those times!
    `!dialedin` - For when someone just can't help but be dialed in!
    `!opinion` - For those unsolicited opinions you didn't ask for!
    `!dumb` - For those times someone has a idea and you need to tell them how you feel!
    `!stfu` - Sometimes people just don't get the hint!
    `!waiting` - For when you're waiting on the one slow person to come online!
    `!sleep` - For when someone needs to go to bed and it's clearly too early!
    `!scotch` - Who doesn't love scotch? Besides non-scotch drinkers, that is?
    `!waldo` - For when Chris gets a high-dea and this becomes a meme!
    `!notgood` - For when the game just isn't so good!
    `!more` - For when the shots just seem to keep coming!
    `!welp` - For those times that someone gets a brutal adonis shot on you!

I also pay attention to what you're saying on Discord and will respond
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
        self.snowflake_list = {}
        for snowflake in SNOWFLAKES.keys():
            self.snowflake_list[snowflake] = True
        self.snowflake_mode = False

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

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if self.snowflake_mode:
            if message.author.id in SNOWFLAKES.keys():
                snowflake = SNOWFLAKES[message.author.id]
                if self.snowflake_list[message.author.id]:
                    if "i made a doody" in message.content.lower():
                        self.snowflake_list[message.author.id] = False
                        await message.channel.send(snowflake["disable"])
                        return
                    else:
                        response = f"{snowflake['message']}\n{snowflake['video']}"
                        await message.channel.send(response)

        if "rob" in message.content.lower():
            response = "Ooh, wee! I hear Rob doesn't miss!"
            await message.channel.send(response)
            return

        if "peter" in message.content.lower():
            response = "Ooh, wee!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "peter.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["balls", "duke", "nukem", "steel"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I've got balls of steel!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "nukem.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["spicy", "boi", "boy"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! That there's a spicy, spicy boi!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "spicyboi.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["peloton", "pelaton"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "Ooh, wee! Nobody's laughing at that Peloton ad anymore, are they?"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "peloton.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        # This should probably become a command later on, but leave it for now
        matches = ["garfielf", "garfield", "jon", "god", "nermal"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "Ooh, wee, Jon. You stupid fuck. How could you...Jon?\n"
                "You were my amigo, Jon. My muchaho, my compadre! Jon...\n"
                "...make me God! Being a celestial body is exhausting!\n"
                "I'm gonna eat everything!"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "garfielf.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["m16", "twisted", "sister", "guitar"]

        if any(c in message.content.lower() for c in matches):
            response = (
                "OOH, WEE! I CARRIED AN M16 AND YOU...\n"
                "YOU CARRY THAT, THAT...GUITAR!!!"
            )
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "m16.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["guys", "shut", "fuck"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! Someone needs to shut their fucks!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "fucks.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["chrome", "google", "ram"]

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! Someone must really hate their RAM!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "chrome.png"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        male_matches = ["adonis", "superman"]
        female_matches = ["adonia", "superwoman"]
        matches = male_matches + female_matches

        if any(c in message.content.lower() for c in matches):
            if any(c in message.content.lower() for c in male_matches):
                text = male_matches
            else:
                text = female_matches

            filename = f"{text[0]}.jpg"
            response = f"Ooh, wee! I'm pretty sure that's something an {text.pop(0)} {text.pop(0)} would do!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", filename), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        if any(c in message.content.lower() for c in matches):
            response = "Ooh, wee! I'm pretty sure that's something an adonia superwoman would do!"
            await message.channel.send(response)
            with open(
                os.path.join("mr_poopybutthole", "resources", "adonia.jpg"), "rb"
            ) as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
            return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, Wee!"
            await message.channel.send(response)

    @commands.command()
    async def ole(self, ctx):
        response = "Ooh, wee!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "ole.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

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

    @commands.command()
    async def shakira(self, ctx):
        response = "Ooh, wee! I hear her hips don't lie!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "shakira.mp4"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def oof(self, ctx):
        response = "Ooh, wee! That was oof-worthy!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "oof.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def wtf(self, ctx):
        response = "Ooh, wee! What the fuck?"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "wtf.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def nice(self, ctx):
        response = "Ooh, wee! That was pretty nice!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "nice.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def damage(self, ctx):
        response = "OOH, WEE! THAT'S A LOT OF DAMAGE!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "damage.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def xp(self, ctx):
        response = "Ooh, wee, Scott! That was...\nONE MEEELLION XP! That's a lot of frickin' XP!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "drevil.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def dialedin(self, ctx):
        response = "Ooh, wee! Looks like SOMEBODY is dialed in!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "dialedin.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def opinion(self, ctx):
        response = "Ooh, wee! Here's what you can do with your opinion!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "opinion.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def dumb(self, ctx):
        response = (
            "Ooh, wee! Looks like had a great suggestion! Let's think about that one!"
        )
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "dumb.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def stfu(self, ctx):
        response = "Ooh, wee! Someone is running their mouth and really need to give it a break!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "stfu.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def waiting(self, ctx):
        response = "Ooh, wee! Someone's taking their sweet-ass time today!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "waiting.gif"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def sleep(self, ctx):
        response = "Ooh, wee! Looks like somebody needs their beauty sleep!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "sleep.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def scotch(self, ctx):
        response = "Ooh, wee! I love scotch! Scotchy-scotch-scotch!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "scotch.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def waldo(self, ctx):
        response = "Ooh, wee! I found that motherfucker!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "waldo.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def yourmom(self, ctx):
        response = "Ooh, wee! That's not what YOUR MOM said last night!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "yourmom.png"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def notgood(self, ctx):
        response = "Ooh, wee! That last shot was notta so good!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "notgood.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def more(self, ctx):
        response = "Ooh, wee! Sounds like the shots just aren't gonna stop!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "more.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

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

    @commands.command()
    async def welp(self, ctx):
        response = "Ooh, wee! Sounds like the match isn't going someone's way!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "welp.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)

    @commands.command()
    async def igotthis(self, ctx):
        response = "Ooh, wee! SOMEONE needs to chill the fuck out!"
        await ctx.channel.send(response)
        with open(
            os.path.join("mr_poopybutthole", "resources", "igotthis.jpg"), "rb"
        ) as file:
            picture = discord.File(file)
            await ctx.channel.send(file=picture)