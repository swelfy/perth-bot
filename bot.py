import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def foo(ctx, arg):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    await ctx.send(embed)

bot.run(os.environ["DISCORD_TOKEN"])
