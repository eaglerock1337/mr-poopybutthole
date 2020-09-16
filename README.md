# mr-poopybutthole

A hilariously useless Discord bot.

## usage

I am going to encapsulate this into a Kubernetes manifest to make for easier deployment, but in the meantime, I am running this in Docker as follows:

Note that running this first requires adding the Discord bot token to `mr-poopybutthole/.env`.

`$ docker build --tag mr-poopybutthole:<version>`

`$ docker run -d -name mr-poopybutthole mr-poopybutthole:<version>`

## running locally

To run outside of Docker, you can take advantage of Pipenv to run as follows:

`$ pipenv install` (add `--dev` for dev tools)

`$ pipenv shell`

`$ python mr-poopybutthole.py`