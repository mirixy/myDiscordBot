import asyncio
import json
import nextcord
import aiohttp
from nextcord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")




intents = nextcord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


if __name__ == "__main__":
    for ext in os.listdir("cogs"):
        if ext.endswith(".py"):
            bot.load_extension(f"cogs.{ext[:-3]}")
    bot.run(TOKEN)

    

