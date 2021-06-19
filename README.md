# mr-poopybutthole

A hilariously useless Discord bot.

More specifically, this is a dumb Discord bot I use on my personal Discord server. It's mostly filled with dumb pictures and inside jokes.

## features

This is a very troll-tastic bot, but it actually has some decent features:

- Modular Discord Cog design, allowing for easy addition/removal of features and for easier debugging
- Core `Oohwee` class - base commands
  - Base Discord listeners, such as `on_ready` and `on_member_join`
  - The `!help` command system
  - Help commands are defined programatically by a YAML config file
  - Pulls in all commands and listners programatically from their own config files
  - Allows for basic help through `!help` and more info on specific commands, such as `!help commmands`
- `Command` class - all meme commands
  - Allows commands such as `!oohwee` and `!fu` to post a memes and a message to the server by any server member
  - All simple commands can be pulled in programatically by a YAML config file
  - Commands can support a single image to be posted, or can also post a random image from a specified list
  - Commands are executed by listening to `on_command_error` for proper triggering and clean execution
- `Listener` class - all meme autoresponders
  - Allows for memes to be posted when members post certain matches to the channel, such as `ooh`, `wee`, `adonis`, and `good bot`
  - Listeners are defined completely by YAML file as well
  - Listeners can have one or more matches and a message to display
  - Listeners also support posting a specified image or posting a random image from a specified list
  - Listeners will not trigger on any commands or vice-versa
- `Snowflake` class - Super Snowflake Mode!
  - Kicks the bot into super troll mode for special server members
  - All snowflakes, custom messages, and links to videos are defined in YAML
  - Status can be displayed by either `!snowflake`, `!snowflake status`, or `!snowflakes`
  - Can be enabled/disabled by `!snowflake on` and `!snowflake off`, respectively
  - When on, all snowflakes will get a custom response for _every_ non-command message they post
  - Snowflakes will also have their nicknames customized by the bot, and will not be able to change it back
  - Snowflakes can retreat to their safe space with `!snowflake safespace` or by typing a safe phrase
  - Snowflakes in their safe space won't get the autorepsonder or have their nickname changed, just some annoying emoji instead
  - Snowflakes can only turn off Snowflake Mode if they first retreat to their safe space with `!snowflake safespace`
  - Snowflakes can choose to rejoin the fun with `!snowflake brave`
  - Snowflakes (not all members) can also use the power `!snowflake force` to override everyone and re-enable Snowflake Mode

## contributing

If you're just here to add a meme to the bot, check out [this file](CONTRIBUTING.md).

## usage

This bot is configured to run locally in a Docker container for Python 3.8.

### requirements

- Python 3.6 or later installed locally (for f-string support)
- Docker
- Make

### installation

- Copy `template.env` to `.env` and fill in your Discord token and main channel ID, optionally adding your dev token and ID as well.
- Run `make start` to build the docker container and run the bot
- Run `make restart` to restart the bot (e.g. for updating)
- Run `make stop` to stop the bot
- Run `make` to see more options for running the bot

## development

To set up a development environment, you can use the different commands build in the `Makefile` to do the following:

Make Aliases:

- `make` or `make help` - display all make options
- `make start` - build container and run bot
- `make restart` - stop, build, and start containerized bot

Docker Options:

- `make build` - build the bot's image
- `make run` - run the containerized bot
- `make stop` - stop containerized bot
- `make log` - tap into container logs and output to `mr-poopybutthole.log`

Development Options:

- `make env` - prepare your local Python environment
- `make local` - run the bot on your system locally
- `make dev` - run the bot locally in development mode
- `make test` - run `pytest` tests and check test coverage
- `make lint` - use the `black` linter to reformat code

For more details on how the bot works, check the [makefile](Makefile) to see what each command does.

## version 1.0 achievements

- Modify the `commands` and `listeners` lists to be imported by YAML files for easier cataloging
- Split `oohwee.py` into the core `Oohwee`, `Listener`, `Command`, and `Snowflake` classes
- Remove code complexity and redundancy
- Super Snowflake Mode: also update user nicknames as well as respond to everything the snowflakes say
- Make a much better `!help` command that is more concise and supports other help commands such as `!help commands` or `!help snowflake`
- Make the `!snowflakes` command look better as well, just like the help command
- Better commands for announcing when Mr. Poopybutthole is loaded, as well as sending messages when players join
- Add support for randomized files to `Command` and `Listener` classes

## future plans

### short term plans

- Add new slash command support for `!help`, `!snowflake`, and future commands
  - Available through <https://pypi.org/project/discord-py-slash-command/>
- Allow commands and listeners to respond directly to the user instead of "someone"
- Add Eagleworld API support for built-in games and other fun stuff

### long term plans

- Voice channel support for posting sound memes
- Either encapsulate in Kubernetes or use docker-compose for quicker reloading of the application
- Complete test coverage of module
- CI/CD pipeline support through Jenkins or another tool
