import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asynco
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_ready():
    print("Thankyou For Using Video Bot")
	await client.change_presence(game=discord.Game(name="prefix ?")
	
@client.event
async def on_message(message):
    if message.content.startswith('?hello'):
	    msg = 'Hello' (0.author.mention) Hows your day?'.format(message)
		await client.send_message(message.channel ,msg)
		
$ heroku addons:create rails-autoscale:trial
		
client.run(os.getenv('rafsan'))
