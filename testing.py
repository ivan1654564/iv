import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json, asyncio, datetime

with open("setting.json","r", encoding="utf8") as jfile:
    jdata = json.load(jfile)
with open("setting.json", "w", encoding="utf8") as jfile:
    jdata["bot_on"] =1
    print (jdata["bot_on"])
    json.dump(jdata, jfile, indent = 4)



#目標 
# 利用command bot_on 跟bot_off 來控制bot的開闢

#流程 
#設立command bot_on 跟bot_off 
# bot_on --> int("bot_on") =0
# bot_on --> int("bot_on") !=0
#更改 while的判斷句 (增加多一個判斷) (達成所有判斷才跑流程)
# while xxx and int("bot_on") ==0



