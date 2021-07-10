import discord
from discord import message
from discord.ext import commands
import json

from discord.ext.commands.core import command
from core.classes import Cog_Extension
import datetime
import pytz

dt_mtn = datetime.datetime.now()

with open("setting.json","r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension): 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
        await channel.send (f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["Leave_channel"]))
        await channel.send  (f"{member} leave!")

    @commands.Cog.listener()
    async def on_message (self, msg):
        if msg.content == "apple":
            await msg.channel.send("hi")

    @commands.command()
    async def em(self, ctx):
        embed = discord.Embed(title="iv", url="https://home.gamer.com.tw/creationDetail.php?sn=4458961"
        , description="my name is iv" , color=0x192cb8 , timestamp = dt_mtn.astimezone(pytz.timezone("Hongkong")) )
        embed.set_author(name="ivan" , url="https://www.youtube.com/watch?v=d0yvxh1PJ9Y&ab_channel=Hololive%E7%AE%B1%E6%8E%A8%E8%99%8E-%E7%87%92%E8%82%89%E8%A6%81%E5%90%83%E7%83%A4%E7%89%9B%E8%82%89"
        , icon_url="https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1623560976616.jpg")
        embed.set_thumbnail(url="https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1623560976616.jpg")       
        embed.add_field(name="1", value="11", inline=True)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=True)
        embed.set_footer(text="made by ivan")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean (self, ctx, num :int):
            await ctx.channel.purge(limit= num+1)
    
    


def setup(bot):
    bot.add_cog(Event(bot))