""""
Created by Zaneaussie 2021 - https://github.com/Zaneaussie
Description:  OOA Discord bot
Version: 1.0
"""

import os
import json
import platform
import sys
import discord

GUILD = 'Order of Australia'

welcome_channel_id = 712257564091351095


if not os.path.isfile("config.json"):
    sys.exit("'config file not found")
else:
    with open("config.json") as file:
        config = json.load(file)


client = discord.Client()

try:

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(f"Bot logged into Discord server as {client.user.name}")
        print(f'Guild: {guild.name}')
        print(f"Discord.py API version: {discord.__version__}")
        print(f"Python version: {platform.python_version()}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("-------------------")
        print('Connected awaiting commands from users...')
    



    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(f'Hi {member.name}, welcome to {guild.name}!')
        await welcome_channel_id.send(f'Hi {member.name}, welcome to {guild.name}! Feel free to take a look around and come say Hi!')

except Exception:
    print('The error was:', Exception)



client.run(config["token"])
