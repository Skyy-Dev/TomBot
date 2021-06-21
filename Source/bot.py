#Tom Kennedy 2021

#Github repository: https://github.com/Skyrub-dev/Discord_bot

#IMPORTANT: This bot runs of a .env file to protect the security of the actual bot, you must insert the details of your own bot and server in the file provided in order for the bot to work properly

import os
import random
import json
from discord.player import FFmpegPCMAudio
import asyncio
import time
import traceback
import sys

import discord
from discord.ext.commands import Bot
from discord.enums import Status
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

os.chdir=("C:\\Users\\Tom\\Desktop\\Holidays_Python\\discord_bot")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!")

act = discord.Game("With Python!")
embed = discord.Embed()
bot.remove_command('help')
players = {}

introascii = '''
   _____                            _           _ _ 
  / ____|                          | |         | | |
 | |     ___  _ __  _ __   ___  ___| |_ ___  __| | |
 | |    / _ \| '_ \| '_ \ / _ \/ __| __/ _ \/ _` | |
 | |___| (_) | | | | | | |  __/ (__| ||  __/ (_| |_|
  \_____\___/|_| |_|_| |_|\___|\___|\__\___|\__,_(_)
  '''

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name = GUILD)
    await bot.change_presence(status=discord.Status.online, activity=act)
    print("----------------------------------- Beginning of debug ------------------------------------")
    print("Debug begun at:")
    print(time.strftime('%d/%m/%Y %H:%M:%S\n'))

    print(
    f'established {bot.user}s connection to Discord services!\n'
    f'Connected to the following guild: {guild.name} (id: {guild.id}'
    )
    
    print(introascii)

@bot.command(name = "ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

@bot.command(name="quote")
async def quotes(ctx: commands.Context):
    with open("./quotes.json", "r") as file:
        data = json.load(file)
        quotes = data['quote']

        response = random.choice(quotes)
        await ctx.send(response)

@bot.command(name="twitter")
async def twitter(ctx: commands.Context):
    await ctx.send("Follow Python's official Twitter here! https://twitter.com/ThePSF")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = "Help",
        colour = discord.Colour.blue()
    )

    embed.add_field(name='!quote', value='Inspirational quotes from the Pope', inline=False)
    embed.add_field(name='!twitter', value='Follow Pythons Twitter!', inline=False)
    embed.add_field(name='!ping', value='Get your ping', inline=False)
    
    embed.add_field(name = 'Voice commands', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = '!yorushika', value='Plays a cool song from Yorushika', inline=False)
    embed.add_field(name = 'More soon!', value='more commands may be added over time', inline=False)

    embed.add_field(name = 'TomCoin', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = "!tomcoin", value = "Use this to learn more about TomCoin!", inline=False)
    embed.add_field(name = "!balance", value = "Fetch your TomCoin balance with this command", inline=False)
    embed.add_field(name = "!rates", value = "View the current TomCoin rates", inline=False)

    await ctx.send(f"Here's your request!, {author}", embed=embed)

@bot.command(pass_context=True, name = "tomcoin")
async def tomcoin(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "TomCoin info menu")

    embed.add_field(name = "What is TomCoin?", value = "TomCoin is a brand new (very real) EPIC cryptocurrency you can earn just for being active and posting in the server", inline=False)
    embed.add_field(name = "How do I earn TomCoin?", value = "Simply posting any message on the server will put you up for a 1/50 chance to earn a random amount of TomCoin between 1 to 100, the bot will post if you earn any", inline=False)
    embed.add_field(name = "How do I check how much TomCoin I own?", value = "To check, simply enter '!balance' to display the amount of TomCoin you currently own", inline=False)
    embed.add_field(name = "What can I do with TomCoin?", value = "Currently, nothing, probably something in the future though", inline=False)
    embed.add_field(name = "How often will TomCoin rates change?", value = "Depending on how TomCoin will be used and evolve will determine how the rates will be changed - use !rates to view current chance and pool of ChungCoin up for grabs", inline=False)

    await ctx.send(f"Here's your request! {author}", embed=embed)

@bot.command(pass_context=True, name = "rates")
async def rates(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "Current TomCoin rates as of: 16/06/2021")

    embed.add_field(name = "Current chance per message of earning TomCoin:", value = "1/50")
    embed.add_field(name = "Current pool of TomCoin to earn:", value = "1 - 100")
    embed.add_field(name = "Additional note:", value = "These values will most likely be changed over time")

    await ctx.send(f"Here's your request! {author}", embed=embed)

#voice features

@bot.command(name="yorushika")
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
        voice = get(bot.voice_clients, guild=ctx.guild)
        source = FFmpegPCMAudio('yorushika.mp3')
        player = voice.play(source)
        #amount of time before disconnect code executes and bot leaves channel
        await asyncio.sleep(306)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("You're not in a voice channel!")

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

#economy system
@bot.command()
async def balance(ctx):
    await chung_account(ctx.author)

    users = await chung_data()
    user = ctx.author

    wallet_amt = users[str(user.id)]["Wallet"]

    embed = discord.Embed(title = f"{ctx.author.name}'s TomCoin")
    embed.add_field(name = "TomCoin balance", value = wallet_amt)
    await ctx.send(embed = embed)

async def chung_account(user):
    
    users = await chung_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
    
    with open("chungbank.json","w") as f:
        json.dump(users,f)
    return True

async def chung_data():
    with open("chungbank.json","r") as f:
        users = json.load(f)
    return users

async def more_chung(user):
    users = await chung_data()

    coin = random.randrange(100)
    users[str(user.id)]["Wallet"] += coin

#command only able to be executed by my account (Skyrub#1376)
@bot.command(name="owner")
@commands.is_owner()
async def owner(ctx: commands.Context):
    await ctx.send("This is only avaiable to the owner!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    
    users = await chung_data()
    user = message.author

    #works in an if statement however none of the other commands work
    if random.random() <= 1/50: #original value 1/50
        earnings = random.randrange(100)
        await message.channel.send(f"You've been given: {earnings} TomCoin!")
        users[str(user.id)]["Wallet"] += earnings

        with open("chungbank.json", "w") as f:
            json.dump(users, f)
        
    await bot.process_commands(message)
        #might try embed this later on

bot.run(TOKEN)
