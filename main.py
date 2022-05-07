import os
import random
import discord
import requests 
import json 

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
  
def get_quote():
  response= requests.get("https://api.kanye.rest/")
  json_data = json.loads(response.text)
  quote = json_data["quote"] + "  -Kanye"
  return(quote)

def get_quote2():
  response= requests.get("https://www.affirmations.dev/")
  json_data = json.loads(response.text)
  quote = json_data["affirmation"] 
  return(quote)


@client.event
async def on_message(message):
  
  if message.author == client.user:
    return 
  
  if message.content == "Help":
    response = "Type in 'Kanye' to get a random quote by Kanye West or type in 'happy' to get an inspirational quote"
    await message.channel.send(response)
  elif message.content == "happy":
    response2 = get_quote2()
    await message.channel.send(response2)
  elif message.content == "Kanye":
    response3 = get_quote()
    await message.channel.send(response3)
  elif message.content == "hi":
    await message.channel.send("Hey there")
  else:
    await message.channel.send("If you have not heard from me already, enter 'Help' to begin! If you have already heard from me, enter 'Help' to get started again because you said the wrong word.")


client.run(TOKEN)

# Documentation:
# To start using this bot, simply type something in the general channel. After your response, the bot will prompt you to enter 'Help' to get started. Once you then enter 'Help', you will be prompted to choose between entering 'Kayne' or 'happy'. If you type in 'Kanye', you will get back a random Kanye quote generated from an API. If you type in 'happy', you will get back a random affirmation/inspirational quote generated from a different API. Also you can say 'hi' and the bot will respond with a 'Hey there'. If you don't enter any of these words specifically, then you'll keep getting the 'else' message telling you to enter 'Help' to get started. I've attempted to have the bot DM the users once they join but I'm not sure if that is working properly. 
