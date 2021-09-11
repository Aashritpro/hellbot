import inspect
import re

from pathlib import Path
from telethon import events

from .session import H2, H3, H4, H5
from hellbot import *
from hellbot.config import Config


def hell_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if pattern is not None:
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            hell_reg = sudo_reg = re.compile(pattern)
        else:
            hell_ = "\\" + Config.HANDLER
            sudo_ = "\\" + Config.SUDO_HANDLER
            hell_reg = re.compile(hell_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            args["pattern"] = hell_reg
            if command is not None:
                cmd1 = hell_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (hell_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    if "disable_edited" in args:
        del args["disable_edited"]

    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        if allow_sudo:
            bot.add_event_handler(func, events.NewMessage(from_users=list(Config.SUDO_USERS), **args))
        if H2:
            H2.add_event_handler(func, events.NewMessage(**args))
        if H3:
            H3.add_event_handler(func, events.NewMessage(**args))
        if H4:
            H4.add_event_handler(func, events.NewMessage(**args))
        if H5:
            H5.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator
