from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from NekoRobot import telethn as bot
from NekoRobot import telethn as tgbot
from NekoRobot.events import register
from NekoRobot import dispatcher


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/86d695fa788c4afe57c86.jpg"
file2 = "https://telegra.ph/file/6ad4eefabe602355b8a4d.jpg"
file3 = "https://telegra.ph/file/798c1d569950c85d0ee6f.jpg"
file4 = "https://telegra.ph/file/003c274407adc8a4d104a.jpg"
file5 = "https://telegra.ph/file/569e16c2db73d3991b40f.jpg"
""" =======================CONSTANTS====================== """

@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Click Here",data="information")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"♡ Hey {betsy}, I'm Chloe\n♡ Click The Button Below To Get Your Info", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    NEKO = "YOUR DETAILS BY Ⲥⲏʟⲟⲉ \n\n"
    NEKO += f"FIRST NAME : {PRO.first_name} \n"
    NEKO += f"LAST NAME : {PRO.last_name}\n"
    NEKO += f"YOU BOT : {PRO.bot} \n"
    NEKO += f"RESTRICTED : {PRO.restricted} \n"
    NEKO += f"USER ID : {boy}\n"
    NEKO += f"USERNAME : {PRO.username}\n"
    await event.answer(NEKO, alert=True)
  except Exception as e:
    await event.reply(f"{e}")


__mod_name__ = "myinfo"
__command_list__ = [
    "myinfo"
]
