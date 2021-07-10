#Tom Kennedy 2021

#Github repository: https://github.com/Skyrub-dev/Discord_bot

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
#https://stackoverflow.com/questions/63464807/how-to-save-traceback-error-information-into-a-file

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!")

#placeholder, will change, deez nuts will never die
act = discord.Game("With DEEZ NUTS")
embed = discord.Embed()
bot.remove_command('help')
players = {}

#ascii font = doom or big http://www.patorjk.com/software/taag/#p=display&f=Doom&t=Tom%20Kendy
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
    f'[ OK ] established {bot.user}s connection to Discord services!\n'
    f'[ OK ] Connected to the following guild: {guild.name} (id: {guild.id})'
    )
    
    print(introascii)

#commands
#https://vcokltfre.dev/tutorial/03-hello/
#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

@bot.command(name = "ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    #await ctx.send = discord.Embed(title = "Pong!", description = {round(bot.latency * 1000)})

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

#HELP command menu
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = "Help from the heavens",
        colour = discord.Colour.blue()
    )

    embed.add_field(name='!quote', value='Recieve a holy quote from the man himself', inline=False)
    embed.add_field(name='!twitter', value='Follow da Ady Pierce twitter', inline=False)
    embed.add_field(name='!ping', value='Get your ping', inline=False)

    embed.add_field(name = 'Voice commands', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = '!yorushika', value='Plays a cool song from Yorushika', inline=False)
    embed.add_field(name = 'More soon!', value='more commands will be added over time', inline=False)

    embed.add_field(name = 'TomCoin', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = "!TomCoin", value = "Use this to learn more about TomCoin!", inline=False)
    embed.add_field(name = "!balance", value = "Fetch your TomCoin balance with this command", inline=False)
    embed.add_field(name = "!rates", value = "View the current TomCoin rates", inline=False)
    embed.add_field(name = "!slots", value = "Get three numbers correct in a row for a chance to earn TomCoin!", inline=False)

    #embed.add_field(name = "Post!", value = "For every message you post, you'll have a 1/50 chance to earn a random amount of TomCoin!", inline=False)

    await ctx.send(f"Here's your request!, {author}", embed=embed)

@bot.command(pass_context=True, name = "TomCoin")
async def TomCoin(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "TomCoin info menu")

    embed.add_field(name = "What is TomCoin?", value = "TomCoin is a brand new (very real) EPIC cryptocurrency you can earn just for being active and posting in the server", inline=False)
    embed.add_field(name = "How do I earn TomCoin?", value = "Simply posting any message on the server will put you up for a 1/50 chance to earn a random amount of TomCoin between 1 to 100, the bot will post if you earn any", inline=False)
    embed.add_field(name = "How do I check how much TomCoin I own?", value = "To check, simply enter '!balance' to display the amount of TomCoin you currently own", inline=False)
    embed.add_field(name = "What can I do with TomCoin?", value = "Currently, nothing, probably something in the future though", inline=False)
    embed.add_field(name = "How often will TomCoin rates change?", value = "Depending on how TomCoin will be used and evolve will determine how the rates will be changed - use !rates to view current chance and pool of TomCoin up for grabs", inline=False)

    await ctx.send(f"Here's your request! {author}", embed=embed)

@bot.command(pass_context=True, name = "rates")
async def rates(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "Current TomCoin rates as of: 16/06/2021")

    embed.add_field(name = "Current chance per message of earning TomCoin:", value = "1/50")
    embed.add_field(name = "Current pool of TomCoin to earn:", value = "1 - 100")
    embed.add_field(name = "Additional note:", value = "These values will most likely be nerfed and/or buffed over time")

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
    embed.set_footer(text = "©TomCoin 2021 - Tom Kendy, Josh Hall, Tom Sargent")
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

#new
#https://stackoverflow.com/questions/51705385/discord-py-levelling-system-using-json-how-can-i-add-these-few-things-to-my-cod

async def more_chung(user):
    users = await chung_data()

    coin = random.randrange(100)
    users[str(user.id)]["Wallet"] += coin

#command only able to be executed by my account (Skyrub#1376)
@bot.command(name="owner")
@commands.is_owner()
async def owner(ctx: commands.Context):
    await ctx.send("This is only avaiable to the owner!")

@bot.command(name = "serverlist")
@commands.is_owner()
#experimental
async def serverlist(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            print(member)

@bot.command(name = "debugcoin")
async def debugcoin(ctx):
    users = await chung_data()
    user = ctx.author
    await ctx.send("This command is for the purpose of debugging TomCoin, if you stumble upon this by accident, too bad, you now have 100 TomCoin")
    users[str(user.id)]["Wallet"] = 100
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)


@bot.command(pass_context = True)
async def reset(ctx):
    
    users = await chung_data()
    user = ctx.author
    
    await ctx.send("Are you sure you want to reset your TomCoin? this process is irreversible!!")
    await ctx.send("Type 'yes' to reset, otherwise type 'no'")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["yes", "no"]
    try:
        msg = await bot.wait_for("message", timeout=15.0, check=check)
    
        if msg.content.lower() == "yes":
            await ctx.channel.send("Resetting...")
            users[str(user.id)]["Wallet"] = 0
            await ctx.channel.send("Reset!")

            with open("chungbank.json", "w") as f:
                json.dump(users, f)
        else:
            await ctx.send("Canceled!")

    except asyncio.TimeoutError:
        await ctx.send("Timed out!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    users = await chung_data()
    user = message.author

    #works in an if statement however none of the other commands work
    #await message.channel.send("this is an example message")
    if random.random() <= 1/50: #original value 1/50
        earnings = random.randrange(100)
        await message.channel.send(f"The Pope has bestowed: {earnings} TomCoin upon you! #blessed")
        users[str(user.id)]["Wallet"] += earnings

        with open("chungbank.json", "w") as f:
            json.dump(users, f)
        
    await bot.process_commands(message)
        #try embed this later on to make it look more neater

@bot.command(name="slots")
@commands.cooldown(rate=1, per=30)
async def slots(ctx):
    slots = [1, 2 ,3]
    
    one = random.choice(slots)
    two = random.choice(slots)
    third = random.choice(slots)

    embed = discord.Embed(title = "Your slot results!")
    
    embed.add_field(name = "Current pot winnings", value = "100 TomCoin")

    users = await chung_data()
    user = ctx.author
    pot = 100


    #find a way to embed
    #also find a way for the numbers to appear at once to make neater and make spam more easier to read
    await ctx.channel.send("Your results are:")
    await ctx.channel.send(str(one))
    await asyncio.sleep(1)
    await ctx.channel.send(str(two))
    await asyncio.sleep(1)
    await ctx.channel.send(str(third))
    await asyncio.sleep(1)

    if one == two == third:
        winningembed = discord.Embed(title = "Winner!")
        winningembed.add_field(name = "Congrats!", value = "You've just won 100 TomCoin!")
        users[str(user.id)]["Wallet"] += pot
        with open("chungbank.json", "w") as f:
            json.dump(users, f)
        await ctx.send(embed = winningembed)
        
    else:
        failembed = discord.Embed(title = "Unlucky!")
        failembed.add_field(name = "No win this time :(", value = "Spin again for a chance to win!")
        await ctx.send(embed = failembed)
        
#error handling - prevents spamming of the slots command
@slots.error
async def bot_error(ctx: commands.Context, error):
    toofast = discord.Embed(title = "Hold it!")
    if isinstance(error, commands.CommandOnCooldown):
        toofast.add_field(name = "You're using this command too frequently!", value = f"Try again in: {round(error.retry_after)} seconds")
        await ctx.send(embed = toofast, delete_after= 15)


@bot.command(name = "serverinfo")
async def serverinfo(ctx):
    guild = discord.utils.get(bot.guilds, name = GUILD)
    await ctx.send(f"This server is, {guild.name} (ID: {guild.id})")


bot.run(TOKEN)
