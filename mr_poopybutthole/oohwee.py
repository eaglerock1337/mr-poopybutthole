# oohwee.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

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

    matches = ["ooh", "wee"]

    if any(c in message.content.lower() for c in matches):
        response = "O" + "o" * random.randint(2, 15) + "h, Wee!"
        await message.channel.send(response)


client.run(TOKEN)
