#    _____              ______       _   
#   |_   _|             | ___ \     | |  
#     | | ___  _ __ ___ | |_/ / ___ | |_ 
#     | |/ _ \| '_ ` _ \| ___ \/ _ \| __|
#     | | (_) | | | | | | |_/ / (_) | |_ 
#     \_/\___/|_| |_| |_\____/ \___/ \__|
#                                                                         

#V1.2 - Last updated 08/10/2021
#Tom Kennedy 2021

#Github repository: https://github.com/Skyrub-dev/TomBot

import os
import random
import json
from discord.errors import HTTPException, InvalidArgument
from discord.player import FFmpegPCMAudio
import asyncio
import time
import traceback
import sys
import youtube_dl

import discord
from discord.ext.commands import Bot
from discord.enums import Status
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

#can remove if cloning or adapted to your own directory
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
    print("------------------------------------------------------------------------------------------")
    print("TomBot - V1.2 (10/21)")
    print("Public repo - https://github.com/Skyrub-dev/Discord_Bot_Public")
    print("Any issues or bugs with the bot? contact me here - Discord: Skryub#1376")
    print("----------------------------------- Beginning of debug ------------------------------------")
    print("Debug begun at:")
    print(time.strftime('%d/%m/%Y %H:%M:%S\n'))

    print(
    f'[ OK ] established {bot.user}s connection to Discord services!\n'
    f'[ OK ] Connected to the following guild: {guild.name} (id: {guild.id})'
    )
    
    print(introascii)

'''
///
Misc commands
///
'''

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title = "Hi!", description = f"Thank you for adding me to {guild.name}. Use !help to discover what I have to offer!")
            await channel.send(embed=embed)

@bot.command(name = "ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command(name = "invite")
async def invite(ctx):
    embed = discord.Embed(Title = "Wanna invite the bot to another server?", description = "https://discord.com/api/oauth2/authorize?client_id=796535397647646741&permissions=8&scope=bot")
    await ctx.send(embed = embed)

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

@bot.command(name="twitter")
async def twitter(ctx: commands.Context):
    await ctx.send("Follow Python's official Twitter here! https://twitter.com/ThePSF")

'''
///
Help command menu
///
'''

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = "Help menu",
        colour = discord.Colour.blue()
    )

    embed.add_field(name='!twitter', value='Follow Python twitter', inline=False)
    embed.add_field(name='!ping', value='Get your ping', inline=False)
    embed.add_field(name='!download - *enter_youtube_url*', value='Want to download a song from youtube without having to use those dodgy sites, use this!', inline=False)
    embed.add_field(name="!invite", value = "Want to invite the bot to another server? grab an invite here!", inline=False)

    embed.add_field(name = 'Voice commands', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = '!yorushika', value='Plays a cool song from Yorushika', inline=False)
    embed.add_field(name = 'More soon!', value='more commands will be added over time', inline=False)

    embed.add_field(name = 'TomCoin', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = "!TomCoin", value = "Use this to learn more about TomCoin!", inline=False)
    embed.add_field(name = "!balance", value = "Fetch your TomCoin balance with this command", inline=False)
    embed.add_field(name = "!rates", value = "View the current TomCoin rates", inline=False)
    embed.add_field(name = "!slots", value = "Get three numbers correct in a row for a chance to earn TomCoin!", inline=False)
    embed.add_field(name = "!daily", value = "Recieve 100 TomCoin per 24 hours!", inline=False)


    embed.set_footer(text = "Hint: use !ping to check your ping!")

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

@bot.command(pass_context=True, name = "Tomcoin")
async def Tomcoin(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "TomCoin info menu")

    embed.add_field(name = "What is TomCoin?", value = "TomCoin is a virtual currency you can earn just for being active and posting in the server", inline=False)
    embed.add_field(name = "How do I earn TomCoin?", value = "Simply posting any message on the server will put you up for a 1/50 chance to earn a random amount of TomCoin between 1 to 100, the bot will post if you earn any", inline=False)
    embed.add_field(name = "How do I check how much TomCoin I own?", value = "To check, simply enter '!balance' to display the amount of TomCoin you currently own", inline=False)
    embed.add_field(name = "How often will TomCoin rates change?", value = "Depending on how TomCoin will be used and evolve will determine how the rates will be changed - use !rates to view current chance and pool of TomCoin up for grabs", inline=False)
    embed.set_footer(text = "Get earning!")

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

@bot.command(pass_context=True, name = "rates")
async def rates(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "Current TomCoin rates as of: 16/06/2021")

    embed.add_field(name = "Current chance per message of earning TomCoin:", value = "1/50")
    embed.add_field(name = "Current pool of TomCoin to earn:", value = "1 - 100")
    embed.add_field(name = "Additional note:", value = "These values will most likely be nerfed and/or buffed over time")
    embed.set_footer(text = "Good luck!")

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

'''
///
Voice commands
///
'''

@bot.command(name="yorushika")
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
        voice = get(bot.voice_clients, guild=ctx.guild)
        source = FFmpegPCMAudio('yorushika.mp3')
        player = voice.play(source)
        await asyncio.sleep(306)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("You're not in a voice channel!")

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

'''
///
Economy system
///
'''

@bot.command()
async def balance(ctx):
    await chung_account(ctx.author)

    users = await chung_data()
    user = ctx.author

    wallet_amt = users[str(user.id)]["Wallet"]

    embed = discord.Embed(title = f"{ctx.author.name}'s TomCoin")
    embed.add_field(name = "TomCoin balance", value = wallet_amt)
    embed.set_footer(text = "Want more TomCoin? use !spin")
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

'''
///
DEBUGGING
///
'''

@bot.command(name = "100debugcoin")
async def debugcoin(ctx):
    users = await chung_data()
    user = ctx.author
    await ctx.send("Given 100 TomCoin")
    users[str(user.id)]["Wallet"] = 100
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)

@bot.command(name = "1000debugcoin")
async def debugcoin(ctx):
    users = await chung_data()
    user = ctx.author
    await ctx.send("Given 1000 TomCoin")
    users[str(user.id)]["Wallet"] = 1000
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)

'''
///
'''
         
#Will reset when the bot is restarted
@bot.command(name = "daily")
@commands.cooldown(rate=1, per=86400)
async def daily(ctx):
    users = await chung_data()
    user = ctx.author
    dailyreward = 100
    await ctx.send("Claimed daily reward of 100 TomCoin! Come back in another 24 hours for more")
    users[str(user.id)]["Wallet"] += dailyreward
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)

@bot.command(pass_context = True)
async def reset(ctx):
    
    users = await chung_data()
    user = ctx.author
    
    await ctx.send("Are you sure you want to reset your Tomcoin? this process is irreversible!!")
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
    wallet_amt = users[str(user.id)]["Wallet"]

    if random.random() <= 1/50: #original value 1/50
        earnings = random.randrange(100)
        earned = discord.Embed(title = f"Congrats!, {message.author}, you've been awarded: {earnings} TomCoin!")
        await message.channel.send(embed = earned)

        users[str(user.id)]["Wallet"] += earnings

        with open("chungbank.json", "w") as f:
            json.dump(users, f)

    await bot.process_commands(message)
    
    role = discord.utils.get(message.guild.roles, name = "TomCoin Master")
    
    if wallet_amt >= 1000:
        if role in user.roles:
            return
        else:
            await user.add_roles(role)
            await message.channel.send("You've earned: 'TomCoin master' by earning 1000 TomCoin in total!")
       
    await bot.process_commands(message)

@bot.command(name="slots")
@commands.cooldown(rate=1, per=30)
async def slots(ctx):
    slots = [1, 2 ,3]
    
    one = random.choice(slots)
    two = random.choice(slots)
    third = random.choice(slots)

    embed = discord.Embed(title = "Your slot results!")
    
    embed.add_field(name = "Current pot winnings:", value = "100 Tomcoin")

    users = await chung_data()
    user = ctx.author
    pot = 100

    await ctx.channel.send("Your results are:")
    embed.add_field(name = "Result: 1:", value = (str(one)), inline = False)
    embed.add_field(name = "Result: 2:", value = (str(two)), inline = False)
    embed.add_field(name = "Result: 3:", value = (str(third)), inline = False)

    await asyncio.sleep(1)
    await ctx.send(embed = embed)

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
        
'''
///
Error handlers
///
'''

@slots.error
async def bot_error(ctx: commands.Context, error):
    toofast = discord.Embed(title = "Hold it!")
    if isinstance(error, commands.CommandOnCooldown):
        toofast.add_field(name = "You're using this command too frequently!", value = f"Try again in: {round(error.retry_after)} seconds")
        await ctx.send(embed = toofast, delete_after= 15)

@daily.error
async def daily_error(ctx: commands.Context, error):
    toofast = discord.Embed(title = "Hold it!")
    if isinstance(error, commands.CommandOnCooldown):
        toofast.add_field(name = "You're using this command too frequently!", value = f"Try again in 24 hours!: ({round(error.retry_after)} seconds)")
        await ctx.send(embed = toofast, delete_after= 15)      



@bot.command(name = "serverid")
async def serverinfo(ctx):
    guild = discord.utils.get(bot.guilds, name = GUILD)
    await ctx.send(f"This server is, {guild.name} (ID: {guild.id})")

'''
///
Test features - Youtube audio downloader
///
'''
@bot.command(name = 'download')
@commands.cooldown(rate=1, per=30)
async def download(ctx, url: str):
    
    await ctx.send("Downloading...")

    ytdl_format = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',

        }],
    }

    with youtube_dl.YoutubeDL(ytdl_format) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "download.mp3")
    await ctx.send("Downloaded! here's your file: (File may take a couple of seconds to post)")
   #If cloning will need to dynamically adapt this depending on where you want audio files to save
    await ctx.send(file=discord.File(r'C:\Users\Tom\Desktop\Holidays_Python\discord_bot\download.mp3'))
    os.remove("download.mp3")
    '''// for purpose of debug //'''
    print(" ")
    print("Download complete and posted on Discord!")
    print(" ")

@download.error
async def download_error(ctx: commands.Context, error):
    toofast = discord.Embed(title = "Hold it!")
    if isinstance(error, commands.CommandOnCooldown):
        toofast.add_field(name = "You're using this command too frequently!", value = f"Try again in: {round(error.retry_after)} seconds")
        await ctx.send(embed = toofast, delete_after= 15)
    elif isinstance(error, commands.UserInputError):
        await ctx.send("Missing Argument")

bot.run(TOKEN)
