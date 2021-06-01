import discord
import os
from dotenv import load_dotenv

client = discord.Client()

#registers events (events responds to messages)
@client.event

#Callback is a function that is called when something else happens
#TRIGGERS WHEN BOT IS READY
async def on_ready():
    print('Dark Spirit  {} has arrived'.format(client))
#0.user
#TRIGGERS IF A MESSAGE IS RECEIVED
@client.event
async def on_message(message):
    if message.author == client.user:
        return None

    if message.content.startswith('$hello'):#hello is trigger word
        await message.channel.send("https://youtu.be/mVHJ6OwTYWc")
load_dotenv()
client.run(os.getenv('TOKEN'))
#TOKEN IS the variable name from .env file

#Edited using Pycharm

#changeagain
