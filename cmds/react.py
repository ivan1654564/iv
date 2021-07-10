import discord
from discord.ext import commands
import random
import json

from core.classes import Cog_Extension

with open("setting.json","r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    #picture in pc
    @commands.command()
    async def picture (self,ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    #picture online
    @commands.command()
    async def online_pic (self,ctx):
        random_pic = random.choice(jdata["online_pic"])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))