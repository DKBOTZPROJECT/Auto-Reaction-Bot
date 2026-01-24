import random
import asyncio
from pyrogram import Client as DKBOTZ, filters
from pyrogram.types import *
from pyrogram.errors import *
from Config import *

@DKBOTZ.on_message(filters.group | filters.channel)
async def send_reaction(client, message):
    try:
        await message.react(random.choice(EMOJI))
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await message.react(random.choice(EMOJI))
    except Exception as e:
        print(f"Error: {e}")
