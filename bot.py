import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

bot.run(os.environ["DISCORD_TOKEN"])
