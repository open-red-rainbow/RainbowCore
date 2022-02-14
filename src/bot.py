#!/usr/bin/env python3
from collections import namedtuple
from operator import itemgetter
import pathlib, csv, tomli


class Instance:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    src_dir = pathlib.Path(__file__).resolve(True).parent
    res_dir = src_dir.parent.joinpath("res")

    Author = namedtuple("Author", ["id", "role", "github", "nickname"])
    authors = []
    with open(res_dir.joinpath("authors.csv"), newline="") as f:
        reader = csv.DictReader(f, ["id", "role", "github", "nickname"])
        for row in reader:
            authors.append(Author(**row))

    with open(res_dir.joinpath("properties.toml"), mode="rb") as f:
        version, config = itemgetter("version", "config")(tomli.load(f))

    token = input("token: ")
    ld = input("log dir: ")
    ll = input("log level: ")
