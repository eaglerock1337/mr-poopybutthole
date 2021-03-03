# mr-poopybutthole

A hilariously useless Discord bot.

More specifically, this is a dumb Discord bot I use on my personal Discord server. It's mostly filled with dumb pictures and inside jokes.

## usage

I am going to encapsulate this into a Kubernetes manifest to make for easier deployment, but in the meantime, I am running this in Docker as follows:

Note that running this first requires adding the Discord bot token to `mr-poopybutthole/mr_poopybutthole/.env`.

`$ docker build --tag mr-poopybutthole:<version>`

`$ docker run -d --rm --name mr-poopybutthole mr-poopybutthole:<version>`

## running locally

To run outside of Docker, you can take advantage of Pipenv to run as follows:

`$ pipenv install` (add `--dev` for dev tools such as `pytest` and `black`)

`$ pipenv shell`

`$ python mr-poopybutthole.py`

## path to version 1.0

- Modify the `commands` and `listeners` lists to be imported by YAML files for easier cataloging
- Separate `oohwee.py` into multiple classes for `listeners`, `commands`, `snowflake`, and the `help` class
- Either encapsulate in Kubernetes or use docker-compose for quicker reloading of the application
