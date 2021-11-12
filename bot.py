import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi


client.run("ODkxNTE5MDM1ODgyMjA5MzYw.YU_hzQ.gZE8dEHzk9IwnPOZhmxJPq2xe74")