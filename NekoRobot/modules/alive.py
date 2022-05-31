"""
MIT License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022 Hodacka
Copyright (c) 2022, Yūki • Black Knights Union, <https://github.com/Hodacka/NekoRobot-3>
This file is part of @NekoXRobot (Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import events, Button, custom
import re, os
from NekoRobot.events import register
from NekoRobot import telethn as tbot
from NekoRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/7a13b2aab8242a1b80c61.jpg"
@register(pattern=("/alive"))
async def awake(event):
  NEKO = f"🤖 Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm **Ⲥⲏʟⲟⲉ** Robot\n\n"
  NEKO += f"✅ I'm Working with **Horniness**\n\n"
  NEKO += f"✅ Ⲥⲏʟⲟⲉ : Latest Version\n\n"
  NEKO += f"✅ python-Telegram-Bot: 13.11\n\n"
  NEKO += f"**♥️ My Heart : [Oppa🫰🏻](t.me/Horny_RUBY)**\n\n"
  NEKO += f"🧑🏻‍💻 My Creator : [LovelyPrince](t.me/DarlingPrince)\n\n"
  
  BUTTON = [[Button.url("🚑 Support", "https://t.me/Koyuki_Support"), Button.url("📝 Repo", "https://github.com/Awesome-Prince/NekoRobot-3.git")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NEKO,  buttons=BUTTON)
