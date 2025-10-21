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
# async def load_cogs():
#     cogs_path = "./src/stock_bot/cogs" 

#     for filename in os.listdir(cogs_path):
#         if filename.endswith('.py') and not filename.startswith('__'):
#             await bot.load_extension(f'cogs.{filename[:-3]}')
#             print(f'{filename[:-3]} Cog loaded.')

async def load_cogs():
    # Path to the cogs folder
    cogs_path = "./src/stock_bot/cogs" 
    
    # Check if the directory exists
    if not os.path.isdir(cogs_path):
        print(f"Error: Cogs directory not found at '{cogs_path}'")
        return

    for filename in os.listdir(cogs_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            # This is the full Python path to the module
            extension_path = f"src.stock_bot.cogs.{filename[:-3]}"
            try:
                # Attempt to load the extension
                await bot.load_extension(extension_path)
                print(f"✅ Cog loaded: {filename[:-3]}")
            except Exception as e:
                # If any error occurs, print it and continue
                print(f"❌ Failed to load cog '{filename[:-3]}': {e}")

async def main():
    await load_cogs()
    token = os.getenv("TOKEN")

    await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())