import os


from pyrogram import filters
from pyrogram.types import Message

from NekoRobot import pbot as app
from NekoRobot.services.sections import section



async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    last_name = user.last_name
    

    


    body = {
        "ID": user_id,
        "First Name": [first_name],
        "Last Name": [last_name],
        "Username": [("@" + username) if username else "Null"],
        "User Link": [mention],


    }
    caption = section("User info", body)
    return [caption]



@app.on_message(filters.command("info") & ~filters.edited)
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("`Processing...`")

    try:
        info_caption = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    

    await message.reply_text(caption=info_caption, quote=False)
    await m.delete()
    
