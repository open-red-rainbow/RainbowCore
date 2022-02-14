from .instance import VERSION

from yachalk import chalk
from functools import reduce
import sys, cmd


def v_str(version):
    v = f"{version.major}.{version.minor}.{version.micro}"
    v += (
        f"{version.releaselevel}{version.serial}"
        if version.releaselevel.casefold() != "final".casefold()
        else ""
    )
    return v


class RRShell(cmd.Cmd):
    _intro = [
        f"Red-Rainbow v{VERSION} (Python {v_str(sys.version_info)}, {sys.implementation.name} {v_str(sys.implementation.version)})",
    ]

    @property
    def intro(self):
        m = reduce(lambda m, l: max(m, len(l)), 0)
        lines = [
            "╔" + (m + 2) * "═" + "╗",
            *[f"║ {line} ║" for line in self._intro],
            "╚" + (m + 2) * "═" + "╝",
        ]
        return "\n".join(lines)

    @property
    def prompt(self):
        return chalk.gray("$ ")

    # ----- hooks -----

    # ----- managing instances -----
    def do_spawn(self, arg):
        """Spawn a new bot"""

    def do_list(self, arg):
        """List bots"""

    def do_restart(self, arg):
        """Restarts a bot"""

    def do_stop(self, arg):
        """Stops a bot"""

    def do_remove(self, arg):
        """Removes a stopped bot"""

    def do_reload(self, arg):
        """Instructs a bot instance to reload modules"""

    # ----- general -----
    def do_exit(self, arg):
        return True
