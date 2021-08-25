import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
Hello {}, <b>This is a QR code generator bot by @NxtStark .</b>
<b>Join:</b> https://telegram.me/HTechMedia
Made by @HTechMedia
"""
HELP_TEXT = """
- <b>You can encode and decode QRCode.</b>
- <b>Send any URL or text, this bot can convert to QRCode.</b>
- <b>You can send a QR code image and decode it.</b>
Made by @HTechMedia
"""
ABOUT_TEXT = """
- <b>Bot : QRCode-Telegram-bot</b>
- <b>Creator :</b> [NxtStark](https://telegram.me/NxtStark)
- <b>Channel :</b> [HTechMedia](https://telegram.me/HTechMedia)
- <b>Source :</b> [Click here](https://github.com/HTechMediaYT/QRCode-Telegram-bot/tree/main)
- <b>Language :</b> [Python3](https://python.org)
- <b>Library :</b> [Pyrogram](https://pyrogram.org)
- <b>Server :</b> [Heroku](https://heroku.com)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/HTechMedia')
        ]]
    )

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
