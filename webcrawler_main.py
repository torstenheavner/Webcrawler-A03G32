import sys
from useful_stuff import *

from discord.ext import commands


sys.path.append("T:/all")
bot = commands.Bot(command_prefix="!")


cogs = getData()["cogs"]
clear()
for extension in cogs:
    bot.load_extension(extension[0])
    # nprint(extension[1], extension[0].upper(), "ONLINE")
    nprint("GREEN", "MAIN", "%s INITIALIZED" % extension[0].upper())


@bot.event
async def on_connect():
    nprint("GREEN", "MAIN", "CONNECTED")

@bot.event
async def on_disconnect():
    nprint("GREEN", "MAIN", "DISCONNECTED")

@bot.event
async def on_ready():
    nprint("GREEN", "MAIN", "ONLINE")
    nprint("GREEN", "MAIN", "ALL PROCESSES INITIALIZED SUCCESFULLY")


@bot.command(brief="CHECK PROCESS STATUS")
async def PING(ctx):
    await ctx.send("WEBCRAWLER_A03G32 ONLINE")
    cprint("GREEN", "MAIN", ctx, "STATUS CHECKED")


@bot.command(brief="RE-INITIALIZE PROCESSES")
async def RELOAD(ctx):
    cprint("GREEN", "MAIN", ctx, "PROCESSES RE-INITIALIZED")
    log = []
    _cogs = getData()["cogs"]
    # if cog == "all":
    for _extension in _cogs:
        try:
            bot.reload_extension(_extension[0])
            # nprint(_extension[1], _extension[0].upper(), "OFFLINE")
            # nprint(_extension[1], _extension[0].upper(), "ONLINE")
            nprint("GREEN", "MAIN", "%s REINITIALIZED" % _extension[0].upper())
            log.append("\"**%s**\" RE-INITIALIZED" % _extension[0].upper())
        except:
            bot.load_extension(_extension[0])
            # nprint(_extension[1], _extension[0].upper(), "ONLINE")
            nprint("GREEN", "MAIN", "%s INITIALIZED" % _extension[0])
            log.append("\"**%s**\" INITIALIZED" % _extension[0].upper())
    nprint("GREEN", "MAIN", "ALL PROCESSES RUNNING")

    await ctx.send("\n".join(log))
    # else:
    #     try:
    #         bot.reload_extension(cog)
    #         await ctx.send("\"**%s**\" RE-INITIALIZED" % cog.upper())
    #         cprint("GREEN", "MAIN", ctx.author, "\"%s\" RE-INITIALIZED" % cog.upper())
    #     except:
    #         bot.load_extension(cog)
    #         await ctx.send("\"**%s**\" INITIALIZED" % cog.upper())
    #         cprint("GREEN", "MAIN", ctx.author, "\"%s\" INITIALIZED" % cog.upper())


with open("T:/all/webcrawler_a03g32_credentials.txt", "r") as token:
    bot.run(token.read())
