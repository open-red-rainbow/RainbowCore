#!/usr/bin/env python3
from collections import namedtuple
from operator import itemgetter
from pathlib import Path
import hashlib, time, csv, configparser, tomli

import aiohttp, hypy
import lib

from lib.bot import Instance
import modules

if __name__ == "__main__":
    src_dir = Path(__file__).resolve(True).parent
    res_dir = src_dir.parent.joinpath("res")

    Author = namedtuple("Author", ["id", "role", "github", "nickname"])
    authors = []
    with open(res_dir.joinpath("authors.csv"), newline="") as f:
        reader = csv.DictReader(f, ["id", "role", "github", "nickname"])
        for row in reader:
            authors.append(Author(**row))

    with open(res_dir.joinpath("properties.toml"), mode="rb") as f:
        version, config = itemgetter("version", "config")(tomli.load(f))

    with open(Path(".").joinpath("bot.conf")) as f:
        parser = configparser.ConfigParser()
        parser.read_file(f)
        config.update(parser["Bot"])

    token = config.get("token")
    ld = Path(config.get("log_dir"))
    ll = config.get("log_level")
    mod_d = Path(config.get("modules"))

    name = hashlib.sha256(
        bytes(f"Bot {version} {int(time.time())})".encode("utf-8"))
    ).hexdigest()

    bot = Instance(name, ld, ll)

    @bot.bot.listen("ready")
    async def on_ready(self):
        print("Ready!")
        self.session = aiohttp.ClientSession()
        self.mojang = hypy.Mojang(session=self.session)

    modules.load(mod_d)
    bot.start(token)
