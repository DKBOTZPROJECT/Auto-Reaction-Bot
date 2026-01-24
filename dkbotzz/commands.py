from pyrogram import Client as DKBOTZ, filters
from pyrogram.types import *
from Config import *
from dkbotz_text import *
from dkbotzz.reaction import *

# /start cmd
@DKBOTZ.on_message(filters.command("start"))
async def dkbotz_handle_start(bot, message):
    await send_reaction(bot, message)
    await message.reply_text(
        START_MESSAGE,
        reply_markup=start_buttons(),
        disable_web_page_preview=True
    )
