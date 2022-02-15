from inspect import iscoroutinefunction
from typing import Optional, Callable
from discord import SlashCommand

import lib

from .bot import BOT

def command(
    name: Optional[str] = None,
    description: Optional[str] = None,
    aliases: list[str] = [],
    hidden: bool = False,
    enabled: bool = True,
):
    def wrapper(func: Callable):
        if not iscoroutinefunction(func):
            raise TypeError("not an async function")
        c = SlashCommand(
            func,
            guild_ids=[758717570101936210],
            name=name,
            description=description,
            default_permission=not hidden,
        )
        lib.BOT.add_application_command(c)
        return func

    return wrapper


def listen(event: str = None):
    def wrapper(func: Callable):
        if not iscoroutinefunction(func):
            raise TypeError("not an async function")
        _event = event.lower()
        if not _event.startswith('on_'):
            _event = 'on_' + _event
        setattr(lib.BOT, _event, func)

    return wrapper
