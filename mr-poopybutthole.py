import logging
import os
import sys

from discord.ext import commands
from dotenv import load_dotenv
from mr_poopybutthole import Oohwee


def get_logger():
    """
    Create the logger for the mr-poopybutthole Discord bot.
    """
    log = logging.getLogger()
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter("%(message)s"))
    stdout_handler.setLevel(logging.INFO)

    log.addHandler(stdout_handler)
    log.setLevel(logging.INFO)


def oohwee():
    """
    Main routine. Creates a logger and instanciates the Oohwee class.
    """
    get_logger()
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = commands.Bot(command_prefix="!")
    bot.add_cog(Oohwee(bot))
    bot.run(TOKEN)

# TODO: argparse function for taking in runtime arguments
# TODO: toggle load_dotenv() only for running outside of k8s

if __name__ == "__main__":
    oohwee()