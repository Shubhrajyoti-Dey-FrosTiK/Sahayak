from enum import Flag
import time
import discord
import os
from discord import client
from discord.ext import commands
from discord.message import Message
import asyncio
from discord.permissions import Permissions

from selenium.webdriver.remote import command
from Sahayak import sahayak

bot = commands.Bot(command_prefix ='-')

global flag 
flag = {}

@bot.command()
async def hi(ctx) :
    await ctx.send("Welcome to Sahayak!\n You can search through vacant vaccine centres near you\nType in the following format\n\n-get_info #< Age Group >#< State_Name >#< District_Name>#< Vaccine_Type >#< Vaccine_Dose >#< Time >\n\n < Age_Group > should be \n   1 for Age Group 18+\n   2 for Age Group 45+\n\n< State_Name > should be the name of your state \n\n  < District_Name > should be the name of the city\n  < Vaccine_Type > should be\n   1 for COVISHIELD\n   2 for COVAXIN \n \n  < Time > represents the time interval after which you want to be notified in HOURS. (It must be an integer value)\n\nNOTE : You can turn off the notifications by the command -end")


async def op(ctx,msg,UserID,time) :
  global flag
  while flag[UserID] == 1 :
    RS = await asyncio.create_task(sahayak(msg)) 
    print(len(RS))
    for i in range(0,len(RS)) :
      await ctx.send(RS[i])
    await ctx.send("https://www.cowin.gov.in/home")
    await asyncio.sleep(time)
    if flag == 0 :
      break

@bot.command()
async def end(ctx) :
  try :
    global flag
    flag[ctx.author.id] = 0
    print(ctx.author.id)
    
    print("End Triggered")
  except :
    pass


@bot.command() 
async def get_info(ctx,*args) :
  global flag
  flag[ctx.author.id] = 1
  msg = "M"
  for i in range(0,len(args)) :
    msg=msg+args[i]+" "
  UserID = ctx.author.id

  M = msg.split("#")
  print(flag)

  o = asyncio.create_task(op(ctx,msg,UserID,(int(M[6].replace(" ","")))*60*60))

bot.run(YOUR_TOKEN)