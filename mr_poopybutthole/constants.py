import os

from datetime import datetime

# Constants for Mr. Poopybutthole module

VERSION = "1.0.0"

REPO_URL = "https://github.com/eaglerock1337/mr-poopybutthole"
ICON_URL = "https://cdn.discordapp.com/app-icons/741883337156853781/41a1b01e5828ecadd517a57f62c07018.png"
HELP_IMAGE_URL = "https://raw.githubusercontent.com/eaglerock1337/mr-poopybutthole/main/mr_poopybutthole/resources/oohwee.gif"
FOOTER_TEXT = f"Mr. Poopybutthole v{VERSION} © {datetime.now().year} EagleRock"

MAIN_CHANNEL = 362982581068890113

MODULE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MODULE_DIR, "data")
RESOURCES_DIR = os.path.join(MODULE_DIR, "resources")

COMMANDS_FILE = os.path.join(DATA_DIR, "commands.yaml")
HELP_FILE = os.path.join(DATA_DIR, "help.yaml")
LISTENERS_FILE = os.path.join(DATA_DIR, "listeners.yaml")
SNOWFLAKES_FILE = os.path.join(DATA_DIR, "snowflakes.yaml")
