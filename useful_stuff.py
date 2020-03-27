import json
import os
from datetime import *

from termcolor import colored
import discord


def clear(): return os.system("cls")


def getData():
    with open("data.json", "r") as dataFile:
        return json.loads(dataFile.read())


def setData(_in):
    with open("data.json", "w") as dataFile:
        dataFile.write(json.dumps(_in, indent=2))


def make_embed():
    return discord.Embed(title="PLACEHOLDER_TITLE", description="PLACEHOLDER_DESCRIPTION", color=0x7289DA)


def getTime():
    return datetime.now()


def can_be_int(string):
    try:
        int(string)
        return True
    except:
        return False


def nprint(_color, _cog, _in):
    print("[%s] [WEBCRAWLER_A03G32] [%s] %s %s" % (getTime(), colored(_cog, _color.lower()), "." * (17 - len(_cog)), _in))


def cprint(_color, _cog, ctx, _in, member=False):
    if member:
        nprint(_color, _cog, "[%s] %s [%s] %s %s" % (ctx.guild.name.upper(), "." * (25 - len(ctx.guild.name)), ctx.name.upper(), "." * (20 - len(ctx.name)), _in))
    else:
        nprint(_color, _cog, "[%s] %s [%s] %s %s" % (ctx.guild.name.upper(), "." * (25 - len(ctx.guild.name)), ctx.author.name.upper(), "." * (20 - len(ctx.author.name)), _in))
