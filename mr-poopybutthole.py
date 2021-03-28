import argparse
import logging
import os
import sys

from discord.ext import commands
from dotenv import load_dotenv

from mr_poopybutthole.oohwee import Oohwee
from mr_poopybutthole.command import Command
from mr_poopybutthole.listener import Listener
from mr_poopybutthole.snowflake import Snowflake


def get_logger():
    """
    Create the logger for the Mr-Poopybutthole Discord bot.
    """
    log = logging.getLogger()
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter("%(message)s"))
    stdout_handler.setLevel(logging.INFO)

    log.addHandler(stdout_handler)
    log.setLevel(logging.INFO)


def get_args():
    """
    Gets command-line arguments for the Mr-Poopybutthole Discord bot.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Enable development mode.")

    return parser.parse_args()


def oohwee():
    """
    Main routine. Creates a logger, instanciates the bot, and
    adds/enables all cogs that makes up Mr. PoopyButthole.
    """
    get_logger()
    load_dotenv()
    args = get_args()

    if args.dev:
        os.environ["DEVMODE"] = "True"
        token = os.getenv("DEV_DISCORD_TOKEN")
    else:
        os.environ["DEVMODE"] = "False"
        token = os.getenv("MAIN_CHANNEL")

    bot = commands.Bot(command_prefix="!")
    bot.remove_command("help")
    bot.add_cog(Oohwee(bot))
    bot.add_cog(Command(bot))
    bot.add_cog(Listener(bot))
    bot.add_cog(Snowflake(bot))
    bot.run(token)


# TODO: toggle load_dotenv() only for running outside of k8s

if __name__ == "__main__":
    oohwee()
