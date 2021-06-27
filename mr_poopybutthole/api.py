import discord
import logging
import requests

from discord.ext import commands

from .constants import EAGLEWORLD_API_URL, ICON_URL, REPO_URL, FOOTER_TEXT

class EagleworldApi(commands.Cog):
    """
    The Eagleworld API class for the Mr. Poopybutthole Discord bot.

    Hands the commands that interface with the Eagleworld API.
    """

    def __init__(self, bot):
        self.logger = logging.getLogger(__name__)
        self.bot = bot

    @commands.command()
    async def fortune(self, ctx, arg="plain"):
        """
        The fortune command, which works with the Eagleworld API to provide the
        user with a fortune. Will request a fortune from the API and send it to
        the channel with a Discord Embed. Supports multiple display options:

        - plain - Return the basic `fortune` command
        - cow - Return the fortune piped through `cowsay`
        - tux - Return the fortune piped through `tuxsay`
        """
        options = ''
        if arg == 'cow':
            options = '?option=cowsay'
        elif arg == 'tux':
            options = '?option=tuxsay'

        fortune = requests.get(f'{EAGLEWORLD_API_URL}/fortune{options}')
        if fortune.status_code == 200:
            response = fortune.json()['fortune']
        else:
            response = f"Got response code {fortune.response} trying to get fortune: {fortune}"

        embed = discord.Embed(
            title=f"Here's your fortune:",
            url=REPO_URL,
            description=f"```{response}```",
        )
        embed.set_author(
            name=f"Oooowee, {ctx.author.name}!", icon_url=ctx.author.avatar_url
        )
        embed.set_thumbnail(url=ICON_URL)
        embed.set_footer(icon_url=ICON_URL, text=FOOTER_TEXT)

        await ctx.channel.send(embed=embed)
        self.logger.info(
            f"Member {ctx.message.author.name} sent !fortune {arg} "
            + f"to the {ctx.channel.name} channel!"
        )