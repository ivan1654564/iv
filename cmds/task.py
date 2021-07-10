import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json, asyncio, datetime

with open("setting.json","r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot =commands.Bot(command_prefix ="[ " , intents = intents)

on_off = 2

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata["test_channel"]))
            while not self.bot.is_closed() and on_off == 0:
                await self.channel.send("Hi I'm running!")
                await asyncio.sleep(5) #unit is second
                pass
        self.bg_task=self.bot.loop.create_task(interval())

        async def time_task( ):
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(862341323310891018)
            while not self.bot.is_closed() :
                now_time = datetime.datetime.now().strftime("%H%M")
                with open("setting.json","r", encoding="utf8") as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata["time"] and self.count == 0:
                    self.count =1
                    await self.channel.send("Task Checking")
                    await asyncio.sleep(1)
                else: 
                    await asyncio.sleep(1)
                    pass
        
        self.bg_task=self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int) :
        self.channel= self.bot.get_channel(ch)
        await ctx.send(f"Set Channel:{self.channel.mention}")

    @commands.command()
    async def set_time (self, ctx, time):
        self.count = 0
        with open("setting.json","r", encoding="utf8") as jfile:
            jdata = json.load(jfile)

        jdata["time"] = time
        with open("setting.json","w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent = 4)
    @commands.command()
    async def on(self, ctx):
        on_off = 0
        await ctx.send("bot is online")
    
    @commands.command( )
    async def off(self, ctx):
        on_off =1
        await ctx.send("bot is offline")






def setup(bot):
    bot.add_cog(Task(bot))
