from pyrogram import Client as DKBOTZ
from Config import *

class Bot(DKBOTZ):
    async def start(self):
        await super().start()
        me = await self.get_me()
        temp.ME = me
        print(f"✅ Bot info: {me.id} | @{me.username}")

app = Bot(
    "dkbotz_reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=5,
    workers=999,
    plugins=dict(root="dkbotzz")
)

if __name__ == "__main__":
    app.run()
