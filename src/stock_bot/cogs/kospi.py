from discord.ext import commands

from src.stock_bot.data.kospi import get_kospi_list

class KOSPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="코스피")
    async def show_kospi_list(self, ctx):
        """KOSPI 전체 종목 리스트를 요청합니다."""

        await ctx.send(" KOSPI 종목 리스트를 가져오는 중입니다. 잠시만 기다려주세요...")

        try:
            result_message = await get_kospi_list()
        except Exception as e:
            result_message = f"오류가 발생했습니다: {e}"

        await ctx.send(result_message)
        # await ctx.send(embed=result_message)
        
    
async def setup(bot):
    await bot.add_cog(KOSPI(bot))