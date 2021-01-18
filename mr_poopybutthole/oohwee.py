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
    ```!ole       !gay       !shakira   !oof       !wtf
!nice      !damage    !xp        !dialedin  !opinion
!dumb      !stfu      !waiting   !sleep     !scotch
!waldo     !notgood   !more      !welp      !igotthis
!neener    !ettu      !latifi    !ihateyou  !sorry
!fu        !fu2       !torvalds  !triggered```""",
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

COMMANDS = {
    "ole": {
        "response": "Ooh, wee! Time for a fiesta!",
        "filename": "ole.jpg",
    },
    "shakira": {
        "response": "Ooh, wee! I hear her hips don't lie!",
        "filename": "shakira.mp4",
    },
    "oof": {
        "response": "Ooh, wee! That was oof-worthy!",
        "filename": "oof.gif",
    },
    "wtf": {
        "response": "Ooh, wee! What the fuck?",
        "filename": "wtf.gif",
    },
    "nice": {
        "response": "Ooh, wee! That was pretty nice!",
        "filename": "nice.gif",
    },
    "damage": {
        "response": "OOH, WEE! THAT'S A LOT OF DAMAGE!",
        "filename": "damage.png",
    },
    "xp": {
        "response": "Ooh, wee, Scott! That was...\nONE MEEELLION XP! That's a lot of frickin' XP!",
        "filename": "drevil.gif",
    },
    "dialedin": {
        "response": "Ooh, wee! Looks like SOMEBODY is dialed in!",
        "filename": "dialedin.jpg",
    },
    "opinion": {
        "response": "Ooh, wee! Here's what you can do with your opinion!",
        "filename": "opinion.png",
    },
    "dumb": {
        "response": "Ooh, wee! Looks like had a great suggestion! Let's think about that one!",
        "filename": "dumb.png",
    },
    "stfu": {
        "response": "Ooh, wee! Someone is running their mouth and really need to give it a break!",
        "filename": "stfu.jpg",
    },
    "waiting": {
        "response": "Ooh, wee! Someone's taking their sweet-ass time today!",
        "filename": "waiting.gif",
    },
    "sleep": {
        "response": "Ooh, wee! Looks like somebody needs their beauty sleep!",
        "filename": "sleep.png",
    },
    "scotch": {
        "response": "Ooh, wee! I love scotch! Scotchy-scotch-scotch!",
        "filename": "scotch.jpg",
    },
    "waldo": {
        "response": "Ooh, wee! I found that motherfucker!",
        "filename": "waldo.jpg",
    },
    "yourmom": {
        "response": "Ooh, wee! That's not what YOUR MOM said last night!",
        "filename": "yourmom.png",
    },
    "notgood": {
        "response": "Ooh, wee! That last shot was notta so good!",
        "filename": "notgood.jpg",
    },
    "more": {
        "response": "Ooh, wee! Sounds like the shots just aren't gonna stop!",
        "filename": "more.jpg",
    },
    "welp": {
        "response": "Ooh, wee! Sounds like the match isn't going someone's way!",
        "filename": "welp.jpg",
    },
    "igotthis": {
        "response": "Ooh, wee! SOMEONE needs to chill the fuck out!",
        "filename": "igotthis.jpg",
    },
    "neener": {
        "response": "Neener neener foo foo! I iz cute so stfu! Ooh, wee!",
        "filename": "neener.jpg",
    },
    "ettu": {
        "response": "Ooh, wee! Et tu? Cogitavi in ​​qua sumus, amici! Bitch.",
        "filename": "ettu.jpg",
    },
    "latifi": {
        "response": "Ooh, wee! Looks like Latifi over there is playing the long game!",
        "filename": "latifi.jpg",
    },
    "ihateyou": {
        "response": "Ooh, wee! Someone's pissed somebody off, tonight!",
        "filename": "ihateyou.jpg",
    },
    "sorry": {
        "response": "Ooh, wee! Let me guess: you didn't mean to shoot him, did you?",
        "filename": "sorry.png",
    },
    "fu": {
        "response": "Ooh, wee! Someone needs a three-finger salute!",
        "filename": "fu.jpg",
    },
    "fu2": {
        "response": "Ooh, wee! Someone else needs a three-finger salute, too!",
        "filename": "fu2.jpg",
    },
    "torvalds": {
        "response": "Ooh, wee! Even Linus Torvalds hates you!",
        "filename": "torvalds.jpg",
    },
    "triggered": {
        "response": "Ooh, wee! Someone better retreat to their safe space right away!",
        "filename": "triggered.gif",
    },
}

LISTENERS = {
    "nukem": {
        "matches": ["balls", "duke", "nukem", "steel"],
        "response": "Ooh, wee! I've got balls of steel!",
        "filename": "nukem.png",
    },
    "spicyboi": {
        "matches": ["spicy", "boi", "boy"],
        "response": "Ooh, wee! That there's a spicy, spicy boi!",
        "filename": "spicyboi.jpg",
    },
    "peloton": {
        "matches": ["peloton", "pelaton"],
        "response": "Ooh, wee! Nobody's laughing at that Peloton ad anymore, are they?",
        "filename": "peloton.jpg",
    },
    "twisted": {
        "matches": ["m16", "twisted", "sister", "guitar"],
        "response": "OOH, WEE! I CARRIED AN M16 AND YOU...\nYOU CARRY THAT, THAT...GUITAR!!!",
        "filename": "m16.jpg",
    },
    "fucks": {
        "matches": ["guys", "shut", "fuck"],
        "response": "Ooh, wee! Someone needs to shut their fucks!",
        "filename": "fucks.jpg",
    },
    "ram": {
        "matches": ["chrome", "google", "ram"],
        "response": "Ooh, wee! Someone must really hate their RAM!",
        "filename": "chrome.jpg",
    },
    "help": {
        "matches": ["help", "halp", "pls", "plz"],
        "response": "Ooh, wee! If you want some help from me, you should probably try the `help` command!",
    },
}


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

    @commands.command()
    async def send_command(self, ctx, command):
        """
        Sends a standard command response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name.
        Takes the message info, and response with the given message and filename.
        """
        cmd = COMMANDS[command]
        await ctx.channel.send(cmd["response"])
        if "filename" in cmd:
            with open(
                os.path.join("mr_poopybutthole", "resources", cmd["filename"]), "rb"
            ) as file:
                picture = discord.File(file)
                await ctx.channel.send(file=picture)

    @commands.Cog.listener()
    async def send_message(self, message, listener):
        """
        Sends a standard message response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name, and
        retrieves the matches, response, and tests if it should send based on the matches.
        Returns true if the match was successful, false otherwise.
        """
        lst = LISTENERS[listener]
        if any(c in message.content.lower() for c in lst["matches"]) and not message.content.startswith("!"):
            await message.channel.send(lst["response"])
            if "filename" in lst:
                with open(
                    os.path.join("mr_poopybutthole", "resources", lst["filename"]), "rb"
                ) as file:
                    picture = discord.File(file)
                    await message.channel.send(file=picture)
            return True
        else:
            return False

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
                        with open(
                            os.path.join("mr_poopybutthole", "resources", "safespace.gif"), "rb"
                        ) as file:
                            picture = discord.File(file)
                            await message.channel.send(file=picture)
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

        if await self.send_message(message, "nukem"):
            return

        if await self.send_message(message, "spicyboi"):
            return

        if await self.send_message(message, "peloton"):
            return

        if await self.send_message(message, "twisted"):
            return

        if await self.send_message(message, "fucks"):
            return

        if await self.send_message(message, "ram"):
            return

        if await self.send_message(message, "help"):
            return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, Wee!"
            await message.channel.send(response)

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
