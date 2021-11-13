import discord

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])