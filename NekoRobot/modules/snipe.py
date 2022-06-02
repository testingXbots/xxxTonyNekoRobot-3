
from time import sleep
from typing import Optional, List
from telegram import TelegramError
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import Filters, CommandHandler
from telegram.ext.dispatcher import run_async, CallbackContext

import random
import NekoRobot.modules.sql.users_sql as sql
from NekoRobot.modules.helper_funcs.filters import CustomFilters
from NekoRobot import dispatcher, DEV_USERS, LOGGER
from NekoRobot.modules.disable import DisableAbleCommandHandler


@run_async
def snipe(update: Update, context: CallbackContext):
    args = context.args
    bot = context.bot
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError:
        update.effective_message.reply_text(
            "Please give me a chat to echo to!")
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            bot.sendMessage(int(chat_id), str(to_send))
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))
            update.effective_message.reply_text(
                "Couldn't send the message. Perhaps I'm not part of that group?")


__help__ = """
*⚠️ Notice:*
Commands listed here only work for users with special access and are mainly used for troubleshooting, debugging purposes.
Group admins/group owners do not need these commands.

 ╔ *List all special users:*
 ╠ `/dragons`*:* Lists all Dragon disasters
 ╠ `/demons`*:* Lists all Demon disasters
 ╠ `/tigers`*:* Lists all Tigers disasters
 ╠ `/wolves`*:* Lists all Wolf disasters
 ╠ `/heroes`*:* Lists all Hero Association members
 ╠ `/adddragon`*:* Adds a user to Dragon
 ╠ `/adddemon`*:* Adds a user to Demon
 ╠ `/addtiger`*:* Adds a user to Tiger
 ╠ `/addwolf`*:* Adds a user to Wolf
 ╚ `Add dev doesnt exist, devs should know how to add themselves`

 ╔ *Ping:*
 ╠ `/ping`*:* gets ping time of bot to telegram server
 ╚ `/pingall`*:* gets all listed ping times

 ╔ *Broadcast: (Bot owner only)*
 ╠  *Note:* This supports basic markdown
 ╠ `/broadcastall`*:* Broadcasts everywhere
 ╠ `/broadcastusers`*:* Broadcasts too all users
 ╚ `/broadcastgroups`*:* Broadcasts too all groups
"""

__mod_name__ = "Disasters"

SNIPE_HANDLER = CommandHandler(
    "snipe",
    snipe,
    pass_args=True,
    filters=CustomFilters.dev_filter)

dispatcher.add_handler(SNIPE_HANDLER)
