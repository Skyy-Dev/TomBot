# Discord_Bot_Public
A simple Discord bot written in Python using Discord.py module! Includes basic economy system and simple voice commands.
Created by Tom Kennedy: Skyrub#1376

# Features
- Basic economy system
- Text commands
- Voice commands

IMPORTANT: An .env file is required to run this version of the bot in order to protect its security, and make things a bit more neater
---------------------------------------------------------------------------------------------------------------------------------------------------
//SETUP//
- Firstly, make sure you have the latest version of Python installed: if not you can install it here - https://www.python.org/
# Dependencies / modules required to install
- To run the bot locally, the following dependencies are required:
- Discord.py
```
pip install discord.py
```
- dotenv
```
pip install python-dotenv
```
- ffmpeg
```
pip install ffmpeg
```

# .env
- Firstly, make sure you have the env extension installed in Python by opening your terminal and entering:
```
pip install python-dotenv
```

- Download the repo (Should be called 'Source')
- Once in the folder right click anywhere in the folder
- Create a new text file call it whatever you want, for the sake of this example let's call it '.env'
- Paste the following code (remember to change the token and guild to your own):
```
# .env

#Find your Discord bot token at: https://discord.com/developers/applications
#Enter the name of your guild in 'DISCORD_GUILD'

DISCORD_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
DISCORD_GUILD="XXXXXXXX XXXXX XXXXX"
```
- Save the file, make sure you set it to 'All files' and add the extension '.env' at the end of the file name

And you're done!

How to start the bot
---------------------------------------------------------------------------------------------------------------------------------------------------
- Go to your Python terminal
- Enter this command to redirect to the location of the file, in my case:
```
cd C:\Users\Tom\Documents\Source
```
- Enter:
```
python bot.py
```
- Or just:
```
bot.py
```
- A connected message will appear on the terminal once you've connected

And that's it, enjoy!
---------------------------------------------------------------------------------------------------------------------------------------------------
