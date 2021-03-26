import os

# Constants for Mr. Poopybutthole module

VERSION = "0.9.5"

MAIN_CHANNEL = 362982581068890113

MODULE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MODULE_DIR, "data")
RESOURCES_DIR = os.path.join(MODULE_DIR, "resources")

COMMANDS_FILE = os.path.join(DATA_DIR, "commands.yaml")
HELP_FILE = os.path.join(DATA_DIR, "help.yaml")
LISTENERS_FILE = os.path.join(DATA_DIR, "listeners.yaml")
SNOWFLAKES_FILE = os.path.join(DATA_DIR, "snowflakes.yaml")
