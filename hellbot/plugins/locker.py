from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights

from . import *


@hell_cmd(pattern="lock ?(.*)")
@errors_handler
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    hell = await eor(event, f"Trying to lock `{input_str}`")
    cid = await client_id(event)
    hell_mention = cid[2]
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await eod(hell, "`Need something to lock sur!!`🚶")
            return
        else:
            await eod(hell, f"**🤐 Invalid lock type:** {input_str} \nDo `{hl}ltype` to get all lock types.")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id, banned_rights=lock_rights)
        )
        await hell.delete()
        await event.client.send_file(
            event.chat_id,
            restlo,
            caption=f"{hell_mention} Locked `{what}` \n__Cause its Rest Time !!__",
            )
    except BaseException as e:
        await eod(event, f"`Do I have proper rights for that ??`\n**Error:** {str(e)}")
        return


@hell_cmd(pattern="unlock ?(.*)")
@errors_handler
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    hell = await eor(event, f"Trying to unlock `{input_str}`")
    cid = await client_id(event)
    hell_mention = cid[2]
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await eod(hell, "`I need something to unlock sur!!`🚶")
            return
        else:
            await eod(hell, f"**🤐 Invalid unlock type:** {input_str} \nDo `{hl}ltype` to get all lock/unlock types.")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(
                peer=peer_id, banned_rights=unlock_rights
            )
        )
        if Config.ABUSE == "ON":
            await hell.delete()
            await event.client.send_file(
                event.chat_id,
                shuru,
                caption=f"**{hell_mention} unlocked** `{what}`",
            )
        else:
            await eor(event, f"{hell_mention} Unlocked `{what}` \n__Now Start Chit Chat !!__")
    except BaseException as e:
        await eod(event, f"`Do I have proper rights for that ??`\n**Error:** {str(e)}")
        return


@hell_cmd(pattern="ltype$")
async def _(event):
    await eor(event, "**Following are the lock types :** \n\n• all\n• msg\n• media\n• sticker\n• gif\n• game\n• inline\n• poll\n• invite\n• pin\n• info\n")


CmdHelp("locker").add_command(
  "lock", "<lock type>", "Locks the mentioned lock type in current chat. You can Get all lock type by using '.ltype'."
).add_command(
  "unlock", "<lock type>", "Unlocks the mentioned lock type in current chat. You can Get all lock types by using '.ltype'."
).add_command(
  "ltype", None, "Use this to get the list of lock types..."
).add_info(
  "Chat Locker."
).add_warning(
  "✅ Harmless Module."
).add()
