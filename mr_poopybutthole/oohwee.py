import os
import logging
import random

from discord.ext import commands
from dotenv import load_dotenv

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
        await member.dm_channel.send(f"Oooh, Wee! {member.name} has joined the server!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return