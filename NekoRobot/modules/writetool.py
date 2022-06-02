from pyrogram import filters

from NekoRobot import pbot


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Give some text to write it on my copy...")
    m = await message.reply_text("» wait a sec, let me write that text...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("» Uploading...")
    await pbot.send_chat_action(message.chat.id, "upload_photo")
    await message.reply_photo(hand, caption="Written with🖊 by [Ⲥⲏʟⲟⲉ](t.me/ChloeXRobot)")
    await m.delete()

__mod_name__ = "Handwrite"

__help__ = """

*Writes the given text on white page with a pen* 🖊

 ‣ `/write <text>` *:* writes the given text.
 """
