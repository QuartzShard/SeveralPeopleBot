## Initialization
import discord
from discord.ext import commands, tasks

## General utility commands
class typing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ## Type!
    @commands.Cog.listener()
    async def on_message(self, ctx):
        await ctx.channel.trigger_typing()

## Allow use of cog class by main bot instance
def setup(bot):
    bot.add_cog(typing(bot))