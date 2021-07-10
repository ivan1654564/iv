<<<<<<< HEAD
import discord
from discord.ext import commands
import json
import random
import os

with open("setting.json","r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot =commands.Bot(command_prefix ="[ " , intents = intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")



@bot.command()
async def   load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def   unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Un-Loaded {extension} done.")

@bot.command()
async def   reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Re-Loaded {extension} done.")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["Token"]) 

=======
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

>>>>>>> a2830125de84ba98ccf5035e202f4a530b9b5513
