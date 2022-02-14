from pathlib import Path
from typing import Any, Dict, Tuple

import tomli


SRC_DIR = Path(__file__).resolve(True).parent.parent
RESOURCES = SRC_DIR.joinpath("res")


def properties(path: Path) -> Tuple[str, Dict[str, Any]]:
    with open(path, mode="rb") as file:
        loaded = tomli.load(file)
    version = loaded["version"]
    # TODO warn if unstable version
    return (version, loaded["config"])


(VERSION, D_CONF) = properties(RESOURCES.joinpath("properties.toml"))


class Instance:
    def __init__(
        self,
        name: str,
        version: str,
    ) -> None:
        # TODO write docstring
        self.name = name
        self.version = version
