import discord
import os
import logging
import random

from discord.ext import commands
from dotenv import load_dotenv


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
    "bitch": {
        "matches": ["bitch", "please"],
        "response": "Bitch, please! You don't want to fuck with this! Ooh, wee!",
        "filename": "bitch.gif",
    },
    "goodbot": {
        "matches": ["good bot"],
        "response": "You like me! You really like me! Oooooooooh, wee!",
        "filename": "goodbot.jpg",
    },
    "badbot": {
        "matches": ["bad bot"],
        "response": "Ooh wee! You're a salty little fuck, aren't you?",
        "filename": "badbot.jpg",
    },
    "hmmm": {
        "matches": ["hmmm", "huh"],
        "response": "Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm?",
        "filename": "hmmm.gif",
    },
    "dinodna": {
        "matches": ["bingo", "dino", "dna"],
        "response": "BINGO! Dino DNA! Ooooooooh, wee!",
        "filename": "dinodna.gif",
    },
}


class Listener(commands.Cog):
    """
    The listener class for the Mr. Poopybutthole Discord bot.

    Hands all listener commands and autoresponses from the bot.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot

    @commands.Cog.listener()
    async def send_message(self, message, listener):
        """
        Sends a standard message response consisting of a text response and an optional picture.
        It obtains this from the above command list by using the provided command name, and
        retrieves the matches, response, and tests if it should send based on the matches.
        Returns true if the match was successful, false otherwise.
        """
        lst = LISTENERS[listener]
        if any(c in message.content.lower() for c in lst["matches"]):
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
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith("!"):
            return

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

        if await self.send_message(message, "goodbot"):
            return

        if await self.send_message(message, "badbot"):
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

        if await self.send_message(message, "bitch"):
            return

        if await self.send_message(message, "hmmm"):
            return

        if await self.send_message(message, "dinodna"):
            return

        matches = ["ooh", "wee"]

        if any(c in message.content.lower() for c in matches):
            response = "O" + "o" * random.randint(2, 15) + "h, wee!"
            await message.channel.send(response)
