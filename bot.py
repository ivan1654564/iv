import discord
from discord.ext import commands

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

bot.run("ODYyMzQxOTEyNzgyNTY5NDcy.YOW8fQ.WCn1ith2-7N0iHGRBDxnUY0weF4") 

