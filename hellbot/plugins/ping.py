import telethon.utils


@hell_cmd(pattern="ping$")
async def _(event):
    client = await bot.get_me()
    uid = telethon.utils.get_peer_id(client)
    ForGo10God = uid
    HELL_USER = client.first_name
    await eor(event, f"Pong \n\n{ForGo10God}\n\n{HELL_USER}")
