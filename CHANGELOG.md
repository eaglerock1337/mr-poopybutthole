# changelog for mr-poopybutthole

## 0.9.0 - 3/25/2021

### 0.9.0 - Added

- Constants file for better clarity and modularity
- Data directory for YAML files
- More commands and listeners!
- Two new snowflakes!
- Added [instructions](CONTRIBUTE.md) on how to add memes to the bot!

### 0.9.0 - Changed

- Drastic reduction of duplicate code
- Listeners and commands now can be fully managed by YAML files
- Snowflake Mode is now managed my YAML file as well!
- Updated `README` with new workflow and instructions

### 0.9.0 - Fixed

- Version of bot is now specified in one place
- Makefile no longer requires updating for each version
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

### 0.1.0 - Changed

N/A

### 0.1.0 - Fixed

N/A
