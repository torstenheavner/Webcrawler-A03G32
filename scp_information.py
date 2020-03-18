from importlib import *
from random import randint

from discord.ext import commands

import useful_stuff as us


class SCP_INFORMATION(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.link = "http://www.scp-wiki.net/scp-"
        self.color = "CYAN"
        self.name = "SCP_INFORMATION"

    def cog_unload(self):
        us.nprint(self.color, self.name, "OFFLINE")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if "scp" in message.content:
            scp_amount = 0
            split_message = message.content.split("scp")
            for number in range(len(split_message)):
                if number > 0:
                    includes_scp = False
                    if split_message[number][0] == " " and us.can_be_int(split_message[number].split(" ")[1]):
                        scp_number = int(split_message[number].split(" ")[1])
                        includes_scp = True
                    elif split_message[number][0] == "-" and us.can_be_int(split_message[number].split("-")[1]):
                        scp_number = int(split_message[number].split("-")[1])
                        includes_scp = True

                    if includes_scp:
                        scp_amount += 1
                        scp_number = scp_number if scp_number > 99 else ("0%s" % scp_number if scp_number > 9 else ("00%s" % scp_number))
                        embed = us.make_embed()
                        scp_link = self.link + str(scp_number)
                        embed.title = "__**SCP-%s**__" % scp_number
                        embed.description = scp_link
                        await message.channel.send(embed=embed)
            if scp_amount > 0:
                us.cprint(self.color, self.name, message, "%s SCP(S) RECOGNIZED" % scp_amount)

    @commands.command(brief="GET THE LINK TO AN SCP")
    async def GET_SCP_LINK(self, ctx, number=-1):
        if number == -1:
            number = randint(0, 5999)
        number = number if number > 99 else ("0%s" % number if number > 9 else "00%s" % number)
        link = self.link + str(number)
        embed = us.make_embed()
        embed.title = "__**SCP-%s**__" % number
        embed.description = link
        await ctx.send(embed=embed)
        us.cprint(self.color, self.name, ctx, "SCP-%s INFORMATION RETRIEVED" % number)


def setup(bot):
    us.nprint("CYAN", "SCP_INFORMATION", "ONLINE")
    bot.add_cog(SCP_INFORMATION(bot))
    reload(us)
