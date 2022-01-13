import discord
import os

client = discord.Client()
client.run(os.environ["DISCORD_TOKEN"])

const exampleEmbed = new Discord.RichEmbed()
    .setColor('#0099ff')
    .setTitle('Add Jerseyetr')
    .setAuthor('Midnight Bot', 'image.png', 'https://xxxxxxxx.com')
    .setDescription('')
    .addField('How to Gain Access to the Server', '1. Go to the Rules Section and read the rules \n2. Add XXXX on Steam. Link above \n3. Download and install our mods. Check the #information Channel for info')
    .addBlankField()
    .addField('Mods download:', 'https://xxxxxxxxx', true)
    .addField('how to install mods', 'https://xxxxxxx', true)
    .addField('Vote for our Server', 'https://xxxxx', true)
    .setImage('')
    .setTimestamp()

channel.send(exampleEmbed);
