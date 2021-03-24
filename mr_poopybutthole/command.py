import discord
import os
import logging

from discord.ext import commands


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
    "fuckmas": {
        "response": "Ooh, wee! Ho, ho ho, motherfuckers!",
        "filename": "fuckmas.jpg",
    },
    "ight": {
        "response": "Time to get the fuck out of Dodge! Ooh, wee!",
        "filename": "ight.jpg",
    },
    "ffs": {
        "response": "Ooh, wee! That didn't quite go as planned!",
        "filename": "ffs.gif",
    },
    "nope": {
        "response": "Denied, bitch! Oooooooooh, wee!",
        "filename": "nope.gif",
    },
    "letsgo": {
        "response": "Ooh, wee! Someone needs to take their goddamn shot, already!",
        "filename": "letsgo.gif",
    },
    "halp": {
        "response": "Ooh, wee! Sounds like somebody is in a bit over their head!",
        "filename": "halp.jpg",
    },
    "orly": {
        "response": "Oh reeeeeeeeeeeeeeeally? Ooh, wee!",
        "filename": "orly.jpg",
    },
    "yarly": {
        "response": "Ya really, bitch. Ooh, wee!",
        "filename": "yarly.jpg",
    },
    "nowai": {
        "response": "Someone had to see the owl memes all the way through! Ooh, wee!",
        "filename": "nowai.jpg",
    },
    "owls": {
        "response": "Ooh, wee! We have a lazy asshole here who doesn't feel like typing out all the owl memes!",
        "filename": "owls.gif",
    },
    "idgaf": {
        "response": "On a scale of one to I don't give a fuck, I don't give a fuck! Ooh, wee!",
        "filename": "idgaf.gif",
    },
    "engineer": {
        "response": "Trust me, I'm an engineer! Ooh, wee!",
        "filename": "engineer.png",
    },
    "win": {
        "response": "Ooh, wee! That sure looks like a win to me!",
        "filename": "win.gif",
    },
    "hattip": {
        "response": "Ooh, wee! I tip my hat to you, sir!",
        "filename": "hattip.gif",
    },
    "bobross": {
        "response": "Ooh, wee! Looks like we're gonna have a happy little accident!",
        "filename": "bobross.jpg",
    },
    "butts": {
        "response": "Hold on to your butts! Ooh, wee!",
        "filename": "butts.gif",
    },
    "ace": {
        "response": "Sorry for the delay, Ace! Oooooooh, wee!",
        "filename": "ace.gif",
    },
}


class Command(commands.Cog):
    """
    The command class for the Mr. Poopybutthole Discord bot.

    Hands all meme commands that follow the basic format:
    - Uses one specific command to be triggered (e.g. '!fu')
    - Returns either a statement, an image, or both to the channel
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot

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
