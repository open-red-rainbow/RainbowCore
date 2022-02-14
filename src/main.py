#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit("module 'Red-Rainbow' must be executed directly")

from core.repl import RRShell

RRShell().cmdloop()
