import os


from pyrogram import filters
from pyrogram.types import Message

from NekoRobot import pbot as app
from NekoRobot.services.sections import section

from NekoRobot import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
)


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
    photo_id = user.photo.big_file_id if user.photo else None
    
    body = {
        "ID": user_id,
        "First Name": [first_name],
        "Last Name": [last_name],
        "Username": [("@" + username) if username else "Null"],
        "User Link": [mention],
    }
    caption = section("User info", body)
    return [caption, photo_id]

if user_id == OWNER_ID:
        text += "\n\nᴛʜᴇ ᴅɪsᴀsᴛᴇʀ ʟᴇᴠᴇʟ ᴏғ ᴛʜɪs ᴜsᴇʀ ɪs <b>ɢᴏᴅ</b>.\n"


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
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)
