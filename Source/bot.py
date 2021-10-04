#    ______               ______       _   
#    | ___ \              | ___ \     | |  
#    | |_/ /__  _ __   ___| |_/ / ___ | |_ 
#    |  __/ _ \| '_ \ / _ \ ___ \/ _ \| __|
#    | | | (_) | |_) |  __/ |_/ / (_) | |_ 
#    \_|  \___/| .__/ \___\____/ \___/ \__|
#             | |                         
#             |_|    

#V1.1 - Last updated 13th July 2021
#Tom Kennedy 2021

#Github repository: https://github.com/Skyrub-dev/Discord_bot

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
    print("------------------------------------------------------------------------------------------")
    print("Popebot - V1.1 (07/21) !DEV BUILD!")
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

#commands
#https://vcokltfre.dev/tutorial/03-hello/
#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

'''
///
Misc commands
///
'''

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title = "Greetings my children", description = f"Thank you for adding me to {guild.name}. Use !help to discover what I have to offer!")
            await channel.send(embed=embed)

@bot.command(name = "ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    #await ctx.send = discord.Embed(title = "Pong!", description = {round(bot.latency * 1000)})

@bot.command(name = "invite")
async def invite(ctx):
    embed = discord.Embed(Title = "Wanna invite the bot to another server?", description = "https://discord.com/api/oauth2/authorize?client_id=849288493511606292&permissions=8&scope=bot")
    await ctx.send(embed = embed)

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
    await ctx.send("Follow da Ady Pierce Twitter here: https://twitter.com/AdyPierce")

'''
///
Help command menu
///
'''

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = "Help from the heavens",
        colour = discord.Colour.blue()
    )
    #add embeds here
    #embed.set_author(name='Help from the heavens')
    embed.set_image(url="https://i.imgur.com/VwBN42t.jpg")
    embed.add_field(name='!quote', value='Recieve a holy quote from the man himself', inline=False)
    embed.add_field(name='!twitter', value='Follow da Ady Pierce twitter', inline=False)
    embed.add_field(name='!ping', value='Get your ping', inline=False)
    embed.add_field(name='!download - *enter_youtube_url*', value='Want to download a song from youtube without having to use those dodgy sites, use this!', inline=False)
    embed.add_field(name="!invite", value = "Want to invite the bot to another server? grab an invite here!", inline=False)

    embed.add_field(name = 'Voice commands', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = '!bigchungus', value='listen to the very legendary tale of big chungus', inline=False)
    embed.add_field(name = 'More soon!', value='more commands will be added over time', inline=False)

    embed.add_field(name = 'ChungCoin', value = '-------------------------------------------------------------------------', inline=False)
    embed.add_field(name = "!chungcoin", value = "Use this to learn more about ChungCoin!", inline=False)
    embed.add_field(name = "!balance", value = "Fetch your ChungCoin balance with this command", inline=False)
    embed.add_field(name = "!rates", value = "View the current ChungCoin rates", inline=False)
    embed.add_field(name = "!slots", value = "Get three numbers correct in a row for a chance to earn ChungCoin!", inline=False)
    embed.add_field(name = "!daily", value = "Recieve 100 ChungCoin per 24 hours!", inline=False)


    embed.set_footer(text = "Da Pope wid his brand new lambo")
    #embed.add_field(name = "Post!", value = "For every message you post, you'll have a 1/50 chance to earn a random amount of ChungCoin!", inline=False)

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

@bot.command(pass_context=True, name = "chungcoin")
async def chungcoin(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "ChungCoin info menu")

    embed.add_field(name = "What is ChungCoin?", value = "ChungCoin is a brand new (very real) EPIC cryptocurrency you can earn just for being active and posting in the server", inline=False)
    embed.add_field(name = "How do I earn ChungCoin?", value = "Simply posting any message on the server will put you up for a 1/50 chance to earn a random amount of ChungCoin between 1 to 100, the bot will post if you earn any", inline=False)
    embed.add_field(name = "How do I check how much ChungCoin I own?", value = "To check, simply enter '!balance' to display the amount of ChungCoin you currently own", inline=False)
    embed.add_field(name = "What can I do with ChungCoin?", value = "Currently, nothing, probably something in the future though", inline=False)
    embed.add_field(name = "How often will ChungCoin rates change?", value = "Depending on how ChungCoin will be used and evolve will determine how the rates will be changed - use !rates to view current chance and pool of ChungCoin up for grabs", inline=False)
    embed.set_footer(text = "©ChungCoin 2021 - Tom Kendy, Josh Hall, Tom Sargent")

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

@bot.command(pass_context=True, name = "rates")
async def rates(ctx):
    author = ctx.message.author

    embed = discord.Embed(title = "Current ChungCoin rates as of: 16/06/2021")

    embed.add_field(name = "Current chance per message of earning ChungCoin:", value = "1/50")
    embed.add_field(name = "Current pool of ChungCoin to earn:", value = "1 - 100")
    embed.add_field(name = "Additional note:", value = "These values will most likely be nerfed and/or buffed over time")
    embed.set_footer(text = "©ChungCoin 2021 - Tom Kendy, Josh Hall, Tom Sargent")

    await ctx.send(f"I have bestowed your request upon you, {author}", embed=embed)

'''
///
Voice commands
///
'''

@bot.command(name="bigchungus")
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
        voice = get(bot.voice_clients, guild=ctx.guild)
        source = FFmpegPCMAudio('music/bigchungus.mp3')
        player = voice.play(source)
        #amount of time before disconnect code executes and bot leaves channel
        await asyncio.sleep(106)
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

    embed = discord.Embed(title = f"{ctx.author.name}'s ChungCoin")
    embed.add_field(name = "ChungCoin balance", value = wallet_amt)
    embed.set_footer(text = "©ChungCoin 2021 - Tom Kendy, Josh Hall, Tom Sargent")
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

'''
///
DEBUGGING
///
'''

@bot.command(name = "100debugcoin")
#@commands.is_owner()
async def debugcoin(ctx):
    users = await chung_data()
    user = ctx.author
    await ctx.send("This command is for the purpose of debugging chungcoin, if you stumble upon this by accident, too bad, you now have 100 chungcoin")
    users[str(user.id)]["Wallet"] = 100
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)

@bot.command(name = "1000debugcoin")
#@commands.is_owner()
async def debugcoin(ctx):
    users = await chung_data()
    user = ctx.author
    await ctx.send("This command is for the purpose of debugging chungcoin, if you stumble upon this by accident, too bad, you now have 1000 chungcoin")
    users[str(user.id)]["Wallet"] = 1000
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)


@bot.command(name = "daily")
@commands.cooldown(rate=1, per=86400)
async def daily(ctx):
    users = await chung_data()
    user = ctx.author
    dailyreward = 100
    await ctx.send("Claimed daily reward of 100 ChungCoin! Come back in another 24 hours for more")
    users[str(user.id)]["Wallet"] += dailyreward
    
    with open("chungbank.json", "w") as f:
            json.dump(users, f)

@bot.command(pass_context = True)
async def reset(ctx):
    
    users = await chung_data()
    user = ctx.author
    
    await ctx.send("Are you sure you want to reset your chungcoin? this process is irreversible!!")
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


    #works in an if statement however none of the other commands work
    #await message.channel.send("this is an example message")
    if random.random() <= 1/50: #original value 1/50
        earnings = random.randrange(100)
        earned = discord.Embed(title = f"You have been #blessed, {message.author}, the Pope has bestowed: {earnings} ChungCoin! upon you!")
        await message.channel.send(embed = earned)
        #await message.channel.send(f"The Pope has bestowed: {earnings} ChungCoin upon you! #blessed")
        users[str(user.id)]["Wallet"] += earnings

        with open("chungbank.json", "w") as f:
            json.dump(users, f)

    await bot.process_commands(message)
    
     #if rolename in user.roles:
    
    #need to find a way to check if a the role has been created don't create a new one
    role = discord.utils.get(message.guild.roles, name = "ChungCoin Master")
    
    if wallet_amt >= 1000:
        if role in user.roles:
            return
        else:
            #role = discord.utils.get(message.guild.roles, name = "ChungCoin Novice")
            await user.add_roles(role)
            #rewardrole = discord.utils.get(message.guild.roles, name = "ChungCoin Novice")
            #await bot.create_role(rewardrole)
            await message.channel.send("Congrats on da new role YOU GOT 1000 CHUNGCOIN")
       
    await bot.process_commands(message)

@bot.command(name="slots")
@commands.cooldown(rate=1, per=30)
async def slots(ctx):
    slots = [1, 2 ,3]
    
    one = random.choice(slots)
    two = random.choice(slots)
    third = random.choice(slots)

    embed = discord.Embed(title = "Your slot results!")
    
    embed.add_field(name = "Current pot winnings:", value = "100 chungcoin")

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
        winningembed.add_field(name = "Congrats!", value = "You've just won 100 chungcoin!")
        users[str(user.id)]["Wallet"] += pot
        with open("chungbank.json", "w") as f:
            json.dump(users, f)
        await ctx.send(embed = winningembed)
        
    else:
        failembed = discord.Embed(title = "Unlucky!")
        failembed.add_field(name = "No win this time :(", value = "Spin again for a chance to win!")
        await ctx.send(embed = failembed)
        
#error handling - prevents spamming of the slots command
#probably a way to make this more neater and efficient
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

#embed and try get the files to download to 'song_dl_yt' for future reference to make it look a lot neater

#add error for the user not including the URL or an invalid URL

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

#Potential future ideas -
#leaderboard system??
#more music to implement?
#shop feature - give roles depending on chungcoin milestones
#Look for other bots online and see what other bots have implemented
