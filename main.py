from pyrogram import Client
from docker-compose import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

bot = Client(
    "QR CODE BOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        "root": "bot/plugins"
    },
    parse_mode="html"
)
bot.run()
