import logging
import pathlib

from discord.ext.commands import Bot

import lib


BOT = None


class Instance:
    def __init__(self, name: str, ld: pathlib.Path, ll: str) -> None:
        self.name = name

        self.root_logger = logging.getLogger(name)
        # TODO configure Logger(s)

        self.bot = Bot(name)
        
        if not lib.BOT:
            lib.BOT = self.bot

    def load(self):
        pass

    def start(self, token: str):
        # TODO load modules from module dir
        # TODO start bot

        self.bot.run(token)
