import asyncio
from hypy import Mojang

import lib


async def _echo(ctx, *, text):
    await ctx.respond(text)


async def _eval(ctx, *, code: str):
    # TODO filter actual code
    result = eval(
        code,
        {
            "print": ctx.send,
            "bot": lib.BOT,
            "ctx": ctx,
            "lib": lib,
        },
    )
    if asyncio.iscoroutine(result):
        result = await result
    if not result:
        await ctx.respond("looks like nothing to me")
    else:
        await ctx.respond("```" + str(result) + "```")


def setup(lib):
    global _echo, _eval
    _echo = lib.command(name="echo")(_echo)
    _eval = lib.command(name="eval")(_eval)


class MainModule:
    def __init__(self, bot) -> None:
        self.bot = bot

    async def _echo(self, ctx, *, args):
        print("echo")
        await ctx.send(args)
