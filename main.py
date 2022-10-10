import discord
import os




TOKEN = 'MTAyOTA1MjQyMDM5Njk2MTgxMw.GyxnR6.bpNF0cZ3pCkAW8MbIUgGpoXo0UNXmlTpby5evg'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*help'):
        await message.channel.send('**HEY I CAN GIVE YOU ANY REPO OR SOURCE CODE YOU WANT by typing " *get repo {the repositry name} **')

    if message.content.startswith('*get repo grabber'):
        await message.channel.send('**:white_check_mark: command successfull**                                                                                                                                                                                                                                                            https://github.com/Anonymous1094795585/FORBIDDEN_BOYZ_GRABBER')


    if message.content.startswith('*get repo ai'):
        await message.channel.send('**:white_check_mark: command successfull**                                                                                                                                                                                                                                                            https://github.com/Anonymous1094795585/TECHSA-AUTOMATED-ASSISTANT-')


    if message.content.startswith('*get code'):
        await message.channel.send('**:x: command failed sorry you arent authorized for viewing source codes**')

client.run(TOKEN)