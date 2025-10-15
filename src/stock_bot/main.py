import os
import asyncio
import discord

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

# TEST 
@bot.command()
async def hello(ctx):
    await ctx.send("ㅎㅇ")

# Load Cogs 
async def load_cogs():
    cogs_path = "./src/stock_bot/cogs" 

    for filename in os.listdir(cogs_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename[:-3]} Cog loaded.')

async def main():
    await load_cogs()
    token = os.getenv("TOKEN")

    await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())