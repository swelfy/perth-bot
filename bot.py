import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    description="test result"
await ctx.send(description)

bot.run(os.environ["DISCORD_TOKEN"])
