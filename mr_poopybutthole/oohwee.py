# oohwee.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CHRIS_ID = 533873187780558848
GAY_FILES = ["gay1.jpg", "gay2.jpg", "gay3.jpg", "gay4.jpg", "gay5.jpg", "gay6.jpg"]

client = discord.Client()


@client.event
async def on_ready():
    print(f"Oooh, Wee! {client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Oooh, Wee! {member.name} has joined the server!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == CHRIS_ID:
        chris = "Ooh, wee! Nice comment there, cheesecake!"
        await message.channel.send(chris)

    if message.content.lower().startswith("!ole"):
        response = "Ooh, wee!"
        await message.channel.send(response)
        with open(os.path.join("resources", "ole.jpg"), "rb") as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
        return

    if message.content.lower().startswith("!gay"):
        response = "Ooh, wee! Here's how gay that shot was!"
        await message.channel.send(response)
        with open(os.path.join("resources", random.choice(GAY_FILES)), "rb") as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
        return

    matches = ["balls", "duke", "nukem", "steel"]

    if any(c in message.content.lower() for c in matches):
        response = "Ooh, wee! I've got balls of steel!"
        await message.channel.send(response)
        with open(os.path.join("resources", "nukem.png"), "rb") as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
        return

    if "balls" in message.content.lower():
        response = "Ooh, wee! I hear Rob doesn't miss!"
        await message.channel.send(response)
        return

    if "rob" in message.content.lower():
        response = "Ooh, wee! I hear Rob doesn't miss!"
        await message.channel.send(response)
        return

    if "peter" in message.content.lower():
        response = "Ooh, wee!"
        await message.channel.send(response)
        with open(os.path.join("resources", "peter.jpg"), "rb") as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
        return

    matches = ["ooh", "wee"]

    if any(c in message.content.lower() for c in matches):
        response = "O" + "o" * random.randint(2, 15) + "h, Wee!"
        await message.channel.send(response)


client.run(TOKEN)
