from pyrogram.types import Message
from pyrogram import filters
from NekoRobot import pbot
from NekoRobot.utils.errors import capture_err
from NekoRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text to Generate Carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text to Generate Carbon.`")
    m = await message.reply_text("`please wait 5 secs...`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Generating Carbon...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()

__mod_name__ = "Carbon"

