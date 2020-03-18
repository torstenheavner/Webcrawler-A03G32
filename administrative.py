from importlib import *

from discord.ext import commands

import useful_stuff as us


class ADMINISTRATIVE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = "RED"
        self.name = "ADMINISTRATIVE"

    def cog_unload(self):
        us.nprint(self.color, self.name, "OFFLINE")

    @commands.command(brief="CHANGE THE SERVER WELCOME MESSAGE")
    async def CHANGE_WELCOME_MESSAGE(self, ctx, message):
        data = us.getData()
        try:
            original_welcome = data["server_welcomes"][str(ctx.guild.id)]
        except:
            original_welcome = "NONE"
        data["server_welcomes"][str(ctx.guild.id)] = message
        new_welcome = message
        us.cprint(self.color, self.name, ctx, "WELCOME MESSAGE CHANGED FROM \"%s\" TO \"%s\"" % (original_welcome, new_welcome))
        await ctx.send("WELCOME MESSAGE CHANGED FROM **\"%s\"** TO **\"%s\"**" % (original_welcome, new_welcome))
        us.setData(data)

    @commands.command(brief="CHANGE THE SERVER LEAVE MESSAGE")
    async def CHANGE_LEAVE_MESSAGE(self, ctx, message):
        data = us.getData()
        try:
            original_leave = data["server_goodbyes"][str(ctx.guild.id)]
        except:
            original_leave = "NONE"
        data["server_goodbyes"][str(ctx.guild.id)] = message
        new_goodbye = message
        us.cprint(self.color, self.name, ctx, "GOODBYE MESSAGE CHANGED FROM \"%s\" TO \"%s\"" % (original_leave, new_goodbye))
        await ctx.send("GOODBYE MESSAGE CHANGED FROM **\"%s\"** TO **\"%s\"**" % (original_leave, new_goodbye))
        us.setData(data)

    @commands.command(brief="GET THE SERVER WELCOME MESSAGE")
    async def GET_WELCOME_MESSAGE(self, ctx):
        data = us.getData()
        try:
            welcome = data["server_welcomes"][str(ctx.guild.id)]
        except:
            welcome = "NONE"
        await ctx.send("__**WELCOME MESSAGE:**__\n%s" % welcome)
        us.cprint(self.color, self.name, ctx, "WELCOME MESSAGE RETRIEVED")


def setup(bot):
    us.nprint("RED", "ADMINISTRATIVE", "ONLINE")
    bot.add_cog(ADMINISTRATIVE(bot))
    reload(us)
