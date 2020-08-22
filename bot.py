from bs4 import BeautifulSoup
import discord
import random
import requests
import warnings
import wget

TOKEN = 'NzQ2NTgwMjI3ODEwOTE4NDQx.X0CZBQ.uauebJ4ESH7uV_sjaaIskXqWDE8'

client = discord.Client()

@client.event #Message print to console saying that the bot is ready.
async def on_ready():
    print("I am ready!!!")

@client.event #Join message!
async def DeezNuts(member):
    await member.create_dm()
    await member.dm_channel.send("Haha Deez Nuts! " + member.name + ": Welcome to the Cracked GAMING!!")

@client.event
async def on_reaction_add(reaction, user):
    

@client.event #!joke command
async def on_message(message):
    if message.author == client.user:
        return

    jokes = ['Haha DEEZ NUTS!', "Joe Mama!","Blindmun", "Blindma", "" ]
    
    if message.content.startswith('!joke'):
        response = random.choice(jokes)
        await message.channel.send(response)

@client.event #!twitch streams command
async def on_message(message):
    if message.author == client.user:
        return
    all_streams = ['https://www.twitch.tv/mr_phantastic', "https://twitch.tv/littlet2525" ,"https://www.twitch.tv/megafood3", "https://www.twitch.tv/youngmullababyyy9", "https://www.twitch.tv/smoke6ix", "https://www.twitch.tv/sebuttian", "https://www.twitch.tv/abvval"]
    if message.content.startswith('!twitches'):
        for stream in all_streams:
            await message.channel.send(stream)

#@client.event #!battle command
#async def on_message(message):
    #if message.author == client.user:
        #return

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()
