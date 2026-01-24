from pyrogram import Client as DKBOTZ, filters
from pyrogram.types import *
from Config import *



START_MESSAGE = """<b>🔥 Welcome To The Auto Reaction Bot!</b>

✨ Add Me To Your Channel/Group And Sit Back!
💥 I Will Auto-React To Your Posts With Cool Emoji!

<b>🚀 Fast • Smart • Automatic • Non-Stop</b>
"""


def start_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆", url=f"https://t.me/{temp.ME.username}?startchannel=start")
            ],
            [
                InlineKeyboardButton("⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆", url=f"https://t.me/{temp.ME.username}?startgroup=start")
            ],
            [
                InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/{DEVELOPER_USERNAME}"),
                InlineKeyboardButton("📢 Channel", url=f"https://t.me/{CHANNEL_USERNAME}")
            ]
        ]
    )
