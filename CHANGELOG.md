# changelog for mr-poopybutthole

## 1.2.1 - 2/1/23

The Not Quite as Annoying Edition

### 1.2.1 - added

- Nine more commands, up to 105 in total! Ooh, wee!
- One new listener!
- Ten new images!

### 1.2.1 - changed

- Removed listeners that triggered too much
- 

## 1.2.0 - 8/9/22

The People's Edition™️

### 1.2.0 - added

- Eight more commands! That makes 96 altogether! Ooh, wee!
- Two more listeners! Ooh, wee!
- Ten new images! Ooh, wee!
- Added ARM support
- Added Kubernetes support
- Added BSD 3-clause license

### 1.2.0 - changed

- Listeners now need to hit a whole word, not just any part of the string
- Added some extra matches to listeners to preserve old behavior
- Removed some listeners that were triggering too much
- Revamped build system to support amd64 and arm64 architectures

### 1.2.0 - fixed

- Docker optimizations:
  - Staged Docker image to remove build artifacts from image
  - Minimized files copied to the image from the repo
  - Reduced Docker image size from 390MB to 230MB
- Fixed Makefile issues with some untested commands
- Fixed some dumb typos

## 1.1.0 - 6/27/21

Fortune Edition

### 1.1.0 - Added

- Added the new `!fortune` command for requesting fortunes from the Eagleworld API
- Added support for multiple display options
- Added `api` class for all interaction with the Eagleworld API for future expansion

## 1.0.7 - 6/19/21

Mission from God Edition

### 1.0.7 - added

- Two new commands!
- One new listener!
- Four new images!
- Me giving the finger!

### 1.0.7 - fixed

- Minor code updates to keep things neat
- The `ok` listener will not trigger as much anymore, since Chris kept complaining

### 1.0.7 - changed

- Chris won't be able to completely get away from the ok gif!
- Improved `Makefile` and `make` functionality

## 1.0.6 - 4/29/21

Extreme Maturity Edition

### 1.0.6 - added

- Six new commands!
- One new listener!
- Twelve new images!
- Added very much missing `!poop` command!

### 1.0.6 - fixed

- Fixed missing documentation for `_send_snowflake_embed()`
- Actually bothered to lint my code

## 1.0.5 - 4/17/21

Big Meme Pack - Nicholas Cage Edition!

### 1.0.5 - added

- Add 25 new images!
- Twelve new commmands!
- Five new listeners!
- Infinitely more Nicholas Cage!
- Your mom is so fat, she deserves more insults! Ooh, wee!

## 1.0.4 - 4/11/21

### 1.0.4 - added

- Six more commands! Ooh, wee!
- One more listener! Ooh, wee!
- Added 22 new images! Ooh, wee!

### 1.0.4 - changed

- Renamed `data` directory to `config` since it makes more sense
- Adjusted some meme text to make it a bit nicer

### 1.0.4 - fixed

- Switched to `yaml.Loader` instead of `yaml.FullLoader` for best practice
- Fixed some commands and listeners that weren't working because I can't spell

## 1.0.3 - 3/28/2021

### 1.0.3 - added

- Over 25 new images and many new memes!
- More pictures of some favorite Snowflakes, especially myself!
- 14 new commands and listeners!

## 1.0.2 - 3/28/2021

### 1.0.2 - added

- Development mode supported for local iterative testing in separate Discord channels
- Development mode supports separate Discord tokens and notification channels
- Snowflake mode now sends emoji to Snowflakes in their Safe Space
- `!snowflake brave` allows Snowflakes to rejoin the action

### 1.0.2 - changed

- The main notification channel is now configurable by the `.env` file
- Memes in embeds no longer need the full GitHub URL in the YAML file
- Meme URLs will pull from your local testing branch in dev mode, `main` otherwise

## 1.0.0 - 3/26/2021

We made it to 1.0! Oooooooh, wee!

### 1.0.0 - added

- Random image support added to `Listener` and `Command` YAML files
- Added log output support to Docker through `make logs`
- Added command and listener totals to help commands
- Added `!snowflake` and `!snowflake status` as aliases to `!snowflakes`
- Added `!snowflake safespace` as a way to snowflakes to retreat to their safe space
- `Makefile` now supports local testing, viewing logs, linting, and testing
- `constants.py` now includes necessary media/constants for displaying all embeds

### 1.0.0 - changed

- Improved `!help commands` and `!help listeners` commands:
  - Programatic formatting of list under `description` instead of using unreliable Discord embed fields
  - No more images attached to keep commands smaller and wider
  - Totals of commands or listeners printed as well
  - Much better formatting overall
- Help commands now show the name and avatar of the person calling the command instead of Mr. Poopybutthole
- Snowflakes can no longer use `!snowflake off` unless they are already in their safe space
- Safe phrases are now changeable in the config files, not hardcoded

### 1.0.0 - fixed

- Final hardcoded command has been moved to YAML!
- `!help commands` and `!help listeners` no longer render text each time they are called, increasing performance
- [CONTRIBUTING.md](CONTRIBUTING.md) file now has up-to-date instructions on adding bot commands/listeners

## 0.9.5 - 3/25/2021

### 0.9.5 - added

- Super Snowflake Mode - Snowflake Mode now updates user nicknames as well as bothers them
- Users will no longer be able to change their server nicknames while Snowflake Mode is enabled
- Snowflake Mode can now only be forced on by fellow snowflakes
- Even more memes!

### 0.9.5 - changed

- The new `!help` command system is here!
- `!help main` or just `!help` provides a concise, nicely formatted help page
- `!help commands` provides the command list
- `!help listeners` provides the listeners and their matches
- `!help snowflake` provides the deets on Snowflake mode
- Function documentation is now more complete and uses proper formating for functions and keywords

### 0.9.5 - fixed

- Commands in the YAML file used to throw errors, but now are now sent through missing command events, making the command routine much, much cleaner as well as more efficient
- Logging is now more complete and will log on most bot events

## 0.9.0 - 3/25/2021

### 0.9.0 - added

- Constants file for better clarity and modularity
- Data directory for YAML files
- More commands and listeners!
- Two new snowflakes!
- Added [instructions](CONTRIBUTING.md) on how to add memes to the bot!

### 0.9.0 - changed

- Drastic reduction of duplicate code
- Listeners and commands now can be fully managed by YAML files
- Snowflake Mode is now managed my YAML file as well!
- Updated `README` with new workflow and instructions

### 0.9.0 - fixed

- Version of bot is now specified in one place in `constants.py`
- Makefile no longer requires updating for each version
- `__version__` is now accessible inside the module itself
- Unnecessary decorators removed from base functions
- Some unreferenced memes have been fixed

## 0.8.0 - 3/24/2021

### 0.8.0 - added

- YAML file support now in place for listeners and commands

### 0.8.0 - changed

- Listeners now part of its own file/class
- Commands now part of its own file/class
- Splitting of cogs now complete

### 0.8.0 - fixed

- Logging of basic commands/listeners fixed
- No license was specified, now ships with GPL 3.0 license

## 0.5.0 - 3/23/2021

### 0.5.0 - added

- Added almost 30 commands and listeners!
- Proper Makefile for building and testing

### 0.5.0 - changed

- Started transition to multiple cogs
- Snowflake Mode is now its own cog
- YAML files are now maintaine in parallel with the inline data structs for listeners and commands

### 0.5.0 - fixed

- Completed transition from poetry to pipenv
- Module import no longer requires futzing with `__init__.py`

## 0.3.0 - 1/3/2021

### 0.3.0 - added

- Generic functions for commands and listeners
- Many more hilarious memes
- Added changelog

### 0.3.0 - changed

- All standard commands and listeners are migrated to the generic functions
- Oohwee class reduced in size and complexity

### 0.3.0 - fixed

- Adding basic memes is now simplified

## 0.2.0 - 10/10/2020

### 0.2.0 - added

- Snowflake mode - much better control over annoying autoreponders
- Many more memes added
- Much more structured help message system

### 0.2.0 - changed

- Original autoreponders for certain discord members moved to snowflake mode

### 0.2.0 - fixed

- The whining of certain snowflakes

## 0.1.0 - 8/22/2020

### 0.1.0 - added

- Initial structure of bot
- Commands and autoreponders created
- Ability to post text and images
- Some easter eggs added for certain Discord members
