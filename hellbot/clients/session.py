from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from hellbot.config import Config


if Config.HELLBOT_SESSION:
    session = StringSession(str(Config.HELLBOT_SESSION))
else:
    session = "hellbot"

try:
    Hell = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"HELLBOT_SESSION - {e}")
    sys.exit()


if Config.SESSION_2:
    session2 = StringSession(str(Config.SESSION_2))
else:
    session2 = "hellbot2"

try:
    H2 = TelegramClient(
        session=session2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except:
    H2 = None


if Config.SESSION_3:
    session3 = StringSession(str(Config.SESSION_3))
else:
    session3 = "hellbot3"

try:
    H3 = TelegramClient(
        session=session3,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except:
    H3 = None


if Config.SESSION_4:
    session4 = StringSession(str(Config.SESSION_4))
else:
    session4 = "hellbot4"

try:
    H4 = TelegramClient(
        session=session4,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except:
    H4 = None


if Config.SESSION_5:
    session5 = StringSession(str(Config.SESSION_5))
else:
    session5 = "hellbot5"

try:
    H5 = TelegramClient(
        session=session5,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except:
    H5 = None


HellBot = TelegramClient(
    session="Hell-TBot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
