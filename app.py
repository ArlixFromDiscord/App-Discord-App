# Anything not working? Report it to Issues and I will help you
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

app = commands.Bot(command_prefix='#')

@app.event
async def on_ready():
    print ("GitHub - https://www.github.com/ArlixFromDiscord/App-Discord-Bot")
    print ("This is a test for the app")

@app.command(pass_context=True)
async def credits(ctx):
    await app.say("This is a bot that was written in the App version of discord.py and someone downloaded it so this is the only credit I bet. - If you want this bot, go to https://www.github.com/ArlixFromDiscord/App-Discord-Bot")

app.run("NDI0MjYzMjc3OTU1MjUyMjQ0.DacQcQ.DFBbTYD3MjI3uVmGdoedqyMmobg")
