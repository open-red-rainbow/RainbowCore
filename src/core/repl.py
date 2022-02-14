import sys
from .instance import VERSION

from yachalk import chalk
import cmd


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
        result = ""
        m = 0
        for line in self._intro:
            m = max(len(line), m)
            result += "║ " + line + " ║\n"
        return "╔" + (m + 2) * "═" + "╗\n" + result + "╚" + (m + 2) * "═" + "╝"

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
