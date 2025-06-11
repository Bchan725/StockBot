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
    print('실행 됨.')

@bot.command()
async def hello(ctx):
    await ctx.send("ㅎㅇ")

@bot.command()
async def test(ctx):
    msg = await ctx.send("1초 생각 좀")
    # 1초 대기
    await asyncio.sleep(1)
    # 메시지 수정
    await msg.edit(content="ㅎㅇ")

bot.run(os.getenv("TOKEN"))