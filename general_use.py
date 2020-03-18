from importlib import *
from random import *

from discord.ext import commands

import useful_stuff as us


class GENERAL_USE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = "MAGENTA"
        self.name = "GENERAL_USE"

    def cog_unload(self):
        us.nprint(self.color, self.name, "OFFLINE")

    @commands.command(brief="ROLL A DIE")
    async def ROLL(self, ctx):
        await ctx.send(randint(0, 6))
        us.cprint(self.color, self.name, ctx, "RANDOM  NUMBER ROLLED")


def setup(bot):
    us.nprint("MAGENTA", "GENERAL_USE", "ONLINE")
    bot.add_cog(GENERAL_USE(bot))
    reload(us)
