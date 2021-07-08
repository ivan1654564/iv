import discord
from discord.ext import commands
import random
intents = discord.Intents.all()

bot =commands.Bot(command_prefix ="[ " , intents = intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(862376491022286848)
    await channel.send (f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(862376533003599882)
    await channel.send  (f"{member} leave!")

@bot.command()
async def ping (ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")

    
#picture in pc
@bot.command()
async def picture (ctx):
    random_pic = random.choice(jdata["pic"])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

#picture online
@bot.command()
async def online_pic (ctx):
    random_pic = random.choice(jdata["online_pic"])
    await ctx.send(random_pic)
    
bot.run("ODYyMzQxOTEyNzgyNTY5NDcy.YOW8fQ.7Q9yEpm3JTcP8hlRgUDg6hIaoWA") 

