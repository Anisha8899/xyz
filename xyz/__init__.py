from telethon import TelegramClient
import logging
import time


openai_key="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"
api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="5871452691:AAHJjLocKmAa0MxdUif7c8PyoK-mgoHfLLA"

bot=TelegramClient("a",api_id,api_hash).start(bot_token=bot_token)