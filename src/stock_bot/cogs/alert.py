from . import * 

class Alert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="국장")
    async def 국장(self, ctx):
        await ctx.send('국장')
    
async def setup(bot):
    await bot.add_cog(Alert(bot))
