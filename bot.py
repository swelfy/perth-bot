import discord
from discord.ext import commands
import os

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])

bot.run(os.environ["DISCORD_TOKEN"])
