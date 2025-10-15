from . import * 

class KOSPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="TEST")
    async def 국장(self, ctx):
        await ctx.send('TEST')
    
async def setup(bot):
    await bot.add_cog(KOSPI(bot))
