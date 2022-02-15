from pathlib import Path
from importlib.machinery import SourceFileLoader
import importlib.util

import lib


def load(path: Path):
    for mod in path.iterdir():
        if mod.name.strip().startswith("_"):
            continue

        mod_path = str(mod.joinpath("main.py").absolute())

        spec = importlib.util.spec_from_file_location(mod.name, mod_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        module.setup(lib)
