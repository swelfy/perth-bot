import discord
from discord.ext import commands
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])

bot.run(os.environ["DISCORD_TOKEN"])
