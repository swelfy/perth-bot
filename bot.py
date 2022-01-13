import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Welcome to the Discord server for Perth Crypto Crew", description="No spam - moderators will not tolerate spam\nNo advertising or affiliate links without ADMIN permission\nBe respectful at all times, kindness is required\nNo doxxing\nPlease use the right channels\nNo discussion of illegal practices\nReport any malicious behaviours to the moderators\nNo pump and dumps", color=0xeb0057)
    await ctx.send(embed=embed)

bot.run(os.environ["DISCORD_TOKEN"])
