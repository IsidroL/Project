# Import class libaries for interaction with discord

import discord
import os
import random

from ec2_metadata import ec2_metadata

from dotenv import load_dotenv

print(ec2_metadata.region)
print(ec2_metadata.instance_id)
print(ec2_metadata.public_ipv4)

load_dotenv()

client = discord.Client()
token = str(os.getenv('TOKEN'))

@client.event
async def on_ready():
    
    print("Logged in as bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return
    if channel == "random":
        if user_message.lower() == "good morning" or user_message.lower() == "hey":
            await message.channel.send(f"morning {username} Your EC2 Data: {ec2_metadata.region}")
            return
        
        elif user_message.lower() == "goodnight":
            await message.channel.send(f"night {username} Your EC2 Data: {ec2_metadata.region}")

client.run(token)
