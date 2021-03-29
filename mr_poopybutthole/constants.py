import os

from datetime import datetime

# Constants for Mr. Poopybutthole module

VERSION = "1.0.3"

if os.getenv("DEV_CHANNEL"):
    from git import Repo

    local_repo = Repo(path=os.getcwd())
    BRANCH = local_repo.active_branch.name
    MAIN_CHANNEL = os.getenv("DEV_CHANNEL")
    NAME = "Mr. Poopybutthole Dev"

else:
    BRANCH = "main"
    MAIN_CHANNEL = 362982581068890113  # TODO: Fix this later
    NAME = "Mr. Poopybutthole"

IMAGE_URL_HEADER = f"https://raw.githubusercontent.com/eaglerock1337/mr-poopybutthole/{BRANCH}/mr_poopybutthole/resources/"

REPO_URL = "https://github.com/eaglerock1337/mr-poopybutthole"
ICON_URL = "https://cdn.discordapp.com/app-icons/741883337156853781/41a1b01e5828ecadd517a57f62c07018.png"
HELP_IMAGE_URL = os.path.join(IMAGE_URL_HEADER, "oohwee.gif")
FOOTER_TEXT = f"{NAME} v{VERSION} © {datetime.now().year} EagleRock"

MODULE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MODULE_DIR, "data")
RESOURCES_DIR = os.path.join(MODULE_DIR, "resources")

COMMANDS_FILE = os.path.join(DATA_DIR, "commands.yaml")
HELP_FILE = os.path.join(DATA_DIR, "help.yaml")
LISTENERS_FILE = os.path.join(DATA_DIR, "listeners.yaml")
SNOWFLAKES_FILE = os.path.join(DATA_DIR, "snowflakes.yaml")
SNOWFLAKE_EMOJI = ["🇸", "🇳", "🇴", "🇼", "🇫", "🇱", "🇦", "🇰", "🇪"]
