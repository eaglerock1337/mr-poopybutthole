import logging
import sys

from mr_poopybutthole import Oohwee


def get_logger():
    """
    Create the logger for the mr-poopybutthole Discord bot.
    """
    log = logging.getLogger()
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter("%(message)s"))
    stdout_handler.setLevel(logging.DEBUG)

    log.addHandler(stdout_handler)
    log.setLevel(logging.DEBUG)


def oohwee():
    """
    Main routine. Creates a logger and instantiates the Oohwee class.
    """
    get_logger()
    Oohwee()


if __name__ == "__main__":
    oohwee()