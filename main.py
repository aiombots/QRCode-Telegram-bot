from pyrogram import Client
import os

bot = Client(
    "QR CODE BOT",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    plugins={
        "root": "bot/plugins"
    },
    parse_mode="html"
)
bot.run()
