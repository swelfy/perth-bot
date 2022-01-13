import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

bot.run(os.environ["DISCORD_TOKEN"])
