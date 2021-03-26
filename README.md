# mr-poopybutthole

A hilariously useless Discord bot.

More specifically, this is a dumb Discord bot I use on my personal Discord server. It's mostly filled with dumb pictures and inside jokes.

## contributing

If you're just here to add a meme to the bot, check out [this file](CONTRIBUTING.md).

## usage

This bot is configured to run locally in a Docker container for Python 3.8.

### requirements

- Python 3.6 or later installed locally
- Docker
- Make

### installation

- Create an `.env` file in this directory, formatted as follows, replacing `{token}` (including braces) with your server's bot token from the Discord developer portal:
- `DISCORD_TOKEN={token}`
- Run `make` to build the docker container and run the bot
- Run `make stop` to stop the bot

## running locally

To run outside of Docker, you can take advantage of Pipenv to run as follows:

- `pip install pipenv`
- `pipenv install` (add `--dev` for dev tools such as `pytest` and `black`)
- `pipenv shell`
- `python mr-poopybutthole.py`

## path to version 1.0

- `DONE` - Modify the `commands` and `listeners` lists to be imported by YAML files for easier cataloging
- `DONE` - Split `oohwee.py` into the core `Oohwee`, `Listener`, `Command`, and `Snowflake` classes
- `DONE` - Remove code complexity and redundancy
- `DONE` - Super Snowflake Mode: also update user nicknames as well as respond to everything the snowflakes say
- Make a much better `!help` command that is more concise and supports other help commands such as `!help commands` or `!help snowflake`
- Make the `!snowflakes` command look better as well, just like the help command
- Better commands for announcing when Mr. Poopybutthole is loaded, as well as sending messages when players join

## future plans

- Either encapsulate in Kubernetes or use docker-compose for quicker reloading of the application
- Complete test coverage of module
- CI/CD pipeline support through Jenkins or another tool
