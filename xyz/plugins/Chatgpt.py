from telethon import events
from .. import bot
from .. import openai_key
import asyncio
import openai

openai.api_key= openai_key

@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def ccchatgpt(event):
  if event.sender_id == int(6129038868):
    await event.reply("hello anisha")
  else:
    await event.reply("hello user")
    