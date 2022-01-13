import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Welcome to the Discord server for Perth Crypto Crew", color=0xeb0057)
    embed.add_field(value="No spam - moderators will not tolerate spam", inline=False)
    embed.add_field(value="No advertising or affiliate links without ADMIN permission", inline=False)
    embed.add_field(value="Be respectful at all times, kindness is required", inline=False)
    embed.add_field(value="No doxxing", inline=False)
    embed.add_field(value="Please use the right channels", inline=False)
    embed.add_field(value="No discussion of illegal practices", inline=False)
    embed.add_field(value="Report any malicious behaviours to the moderators", inline=False)
    embed.add_field(nvalue="No pump and dumps", inline=False)
await ctx.send(embed=embed)

bot.run(os.environ["DISCORD_TOKEN"])

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])
