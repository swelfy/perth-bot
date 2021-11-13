import discord
import os

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])
