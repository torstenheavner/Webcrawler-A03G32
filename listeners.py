from random import *

from discord.ext import commands

import useful_stuff as us
from importlib import *


class LISTENERS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = "YELLOW"
        self.name = "LISTENERS"

    def cog_unload(self):
        us.nprint(self.color, self.name, "OFFLINE")

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        system_channel = ctx.guild.system_channel
        if system_channel is not None:
            data = us.getData()
            try:
                message = data["server_welcomes"][str(ctx.guild.id)].replace("[USER]", ctx.mention)
            except:
                message = "%s JOINED" % ctx.mention
            await system_channel.send(message)
            us.cprint(self.color, self.name, ctx, "USER JOINED SERVER", True)

    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        system_channel = ctx.guild.system_channel
        if system_channel is not None:
            data = us.getData()
            try:
                message = data["server_goodbyes"][str(ctx.guild.id)].replace("[USER]", ctx.mention)
            except:
                message = "%s LEFT" % ctx.mention
            await system_channel.send(message)
            us.cprint(self.color, self.name, ctx, "USER LEFT SERVER", True)

    # @commands.Cog.listener()
    # async def on_message(self, ctx):
    #     cprint(self.color, self.name, ctx, "MESSAGE RECIEVED")


def setup(bot):
    us.nprint("YELLOW", "LISTENERS", "ONLINE")
    bot.add_cog(LISTENERS(bot))
    reload(us)