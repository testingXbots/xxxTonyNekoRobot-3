from NekoRobot.modules.sql_extended.night_mode_sql import add_nightmode, rmnightmode, get_all_chat_id, is_nightmode_indb
from telethon.tl.types import ChatBannedRights
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from telethon import functions
from telethon import types
from NekoRobot.events import register
from NekoRobot import telethn as tbot
import os




async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None




hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

@register(pattern="^/night")
async def close_ws(event):
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("❗Only admins can execute this command.")
       return
      
    

    if not event.is_group:
        await event.reply("You Can Only Enable Night Mode in Groups.")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.reply("Currently NightMode is Enabled for this Chat.")
        return
    add_nightmode(str(event.chat_id))
    await event.reply(f"Added chat **{event.chat.title}** with id : `{event.chat_id}` to database.\n\n**This Group will be Closed at 12am(IST) & will be Opened at 06am(IST)**")

@register(pattern="^/rmnight")
async def disable_ws(event):
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("❗Only admins can execute this command.")
       return

     


    if not event.is_group:
        await event.reply("You Can Only Disable Night Mode in Groups.")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.reply("NightMode is Disabled for this Chat")
        return
    rmnightmode(str(event.chat_id))
    await event.reply(f"Removed chat **{event.chat.title}** with id : `{event.chat_id}` From Database.")


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
              int(warner.chat_id), "12:00 AM, Group is Closing till 6 AM. Night Mode Started!"
            )
            await tbot(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=hehes
            )
            )
        except Exception as e:
            logger.info(f"Unable To Close Group {warner} - {e}")

#Run everyday at 12am
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=59)
scheduler.start()

async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
              int(warner.chat_id), "06:00 AM, Group Is Opening."
            )
            await tbot(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=openhehe
            )
        )
        except Exception as e:
            logger.info(f"Unable To Open Group {warner.chat_id} - {e}")

# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open, trigger="cron", hour=5, minute=59)
scheduler.start()

__help__ = """
*Admins Only*

 ‣ /night*:* Adds Group to NightMode Chats
 ‣ /rmnight*:* Removes Group From NightMode Chats

*» Note:* Night Mode chats get Automatically closed at 12 am(IST) and Automatically opened at 6 am(IST) to Prevent Night Spams.
"""

__mod_name__ = "Nightmode​"
