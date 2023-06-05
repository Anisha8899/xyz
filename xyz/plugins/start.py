from .. import bot,openai_key
from telethon import events 
import asyncio
import openai

openai.my_api_key="opena_key"

@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):
 await event.reply("HELLO THIS IS START COMMAND")
 

@bot.on(events.NewMessage(incoming=True,pattern="/get"))
async def start(event):
  a=await event.reply("HELLO THIS IS GET COMMAND")
  await asyncio.sleep(2)
  await a.edit("this is edited message")
  
  
@bot.on(events.NewMessage(incoming=True,pattern="/eval"))
async def start(event):
  await event.reply("HELLO THIS IS EVAL COMMAND")
  