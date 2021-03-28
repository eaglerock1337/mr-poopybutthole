# changelog for mr-poopybutthole

## 1.0.2 - 3/28/2021

### 1.0.2 - Added

- Development mode supported for local iterative testing in separate Discord channels
- Development mode supports separate Discord tokens and notification channels
- Snowflake mode now sends emoji to Snowflakes in their Safe Space
- `!snowflake brave` allows Snowflakes to rejoin the action

### 1.0.2 - Changed

- The main notification channel is now configurable by the `.env` file
- Memes in embeds no longer need the full GitHub URL in the YAML file
- Meme URLs will pull from your local testing branch in dev mode, `main` otherwise

## 1.0.0 - 3/26/2021

We made it to 1.0! Oooooooh, wee!

### 1.0.0 - Added

- Random image support added to `Listener` and `Command` YAML files
- Added log output support to Docker through `make logs`
- Added command and listener totals to help commands
- Added `!snowflake` and `!snowflake status` as aliases to `!snowflakes`
- Added `!snowflake safespace` as a way to snowflakes to retreat to their safe space
- `Makefile` now supports local testing, viewing logs, linting, and testing
- `constants.py` now includes necessary media/constants for displaying all embeds

### 1.0.0 - Changed

- Improved `!help commands` and `!help listeners` commands:
  - Programatic formatting of list under `description` instead of using unreliable Discord embed fields
  - No more images attached to keep commands smaller and wider
  - Totals of commands or listeners printed as well
  - Much better formatting overall
- Help commands now show the name and avatar of the person calling the command instead of Mr. Poopybutthole
- Snowflakes can no longer use `!snowflake off` unless they are already in their safe space
- Safe phrases are now changeable in the config files, not hardcoded

### 1.0.0 - Fixed

- Final hardcoded command has been moved to YAML!
- `!help commands` and `!help listeners` no longer render text each time they are called, increasing performance
- [CONTRIBUTING.md](CONTRIBUTING.md) file now has up-to-date instructions on adding bot commands/listeners

## 0.9.5 - 3/25/2021

### 0.9.5 - Added

- Super Snowflake Mode - Snowflake Mode now updates user nicknames as well as bothers them
- Users will no longer be able to change their server nicknames while Snowflake Mode is enabled
- Snowflake Mode can now only be forced on by fellow snowflakes
- Even more memes!

### 0.9.5 - Changed

- The new `!help` command system is here!
- `!help main` or just `!help` provides a concise, nicely formatted help page
- `!help commands` provides the command list
- `!help listeners` provides the listeners and their matches
- `!help snowflake` provides the deets on Snowflake mode
- Function documentation is now more complete and uses proper formating for functions and keywords

### 0.9.5 - Fixed

- Commands in the YAML file used to throw errors, but now are now sent through missing command events, making the command routine much, much cleaner as well as more efficient
- Logging is now more complete and will log on most bot events

## 0.9.0 - 3/25/2021

### 0.9.0 - Added

- Constants file for better clarity and modularity
- Data directory for YAML files
- More commands and listeners!
- Two new snowflakes!
- Added [instructions](CONTRIBUTING.md) on how to add memes to the bot!

### 0.9.0 - Changed

- Drastic reduction of duplicate code
- Listeners and commands now can be fully managed by YAML files
- Snowflake Mode is now managed my YAML file as well!
- Updated `README` with new workflow and instructions

### 0.9.0 - Fixed

- Version of bot is now specified in one place in `constants.py`
- Makefile no longer requires updating for each version
- `__version__` is now accessible inside the module itself
- Unnecessary decorators removed from base functions
- Some unreferenced memes have been fixed

## 0.8.0 - 3/24/2021

### 0.8.0 - Added

- YAML file support now in place for listeners and commands

### 0.8.0 - Changed

- Listeners now part of its own file/class
- Commands now part of its own file/class
- Splitting of cogs now complete

### 0.8.0 - Fixed

- Logging of basic commands/listeners fixed
- No license was specified, now ships with GPL 3.0 license

## 0.5.0 - 3/23/2021

### 0.5.0 - Added

- Added almost 30 commands and listeners!
- Proper Makefile for building and testing

### 0.5.0 - Changed

- Started transition to multiple cogs
- Snowflake Mode is now its own cog
- YAML files are now maintaine in parallel with the inline data structs for listeners and commands

### 0.5.0 - Fixed

- Completed transition from poetry to pipenv
- Module import no longer requires futzing with `__init__.py`

## 0.3.0 - 1/3/2021

### 0.3.0 - Added

- Generic functions for commands and listeners
- Many more hilarious memes
- Added changelog

### 0.3.0 - Changed

- All standard commands and listeners are migrated to the generic functions
- Oohwee class reduced in size and complexity

### 0.3.0 - Fixed

- Adding basic memes is now simplified

## 0.2.0 - 10/10/2020

### 0.2.0 - Added

- Snowflake mode - much better control over annoying autoreponders
- Many more memes added
- Much more structured help message system

### 0.2.0 - Changed

- Original autoreponders for certain discord members moved to snowflake mode

### 0.2.0 - Fixed

- The whining of certain snowflakes

## 0.1.0 - 8/22/2020

### 0.1.0 - Added

- Initial structure of bot
- Commands and autoreponders created
- Ability to post text and images
- Some easter eggs added for certain Discord members
