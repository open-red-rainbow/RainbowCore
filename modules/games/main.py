# from

from collections import deque


class sexy_Sex_uwu_pornography_meoW_nya_uwu_redstone_exception_gaming(Exception):
    pass


listen = command = lambda *args: None


def setup(lib):
    GamesModule.counting = lib.listen("counting")(GamesModule.counting)
    GamesModule.createcounting = lib.command("createcounting")(
        GamesModule.createcounting
    )


class GamesModule:
    # channel_messages: dict[TextChannel, list[deque]] = {}
    channel_messages = {}

    def __init__(self, bot):
        self.bot = bot

    async def _initialize_counting(self):
        await self.bot.wait_until_ready()

        for channel_id in self.bot.db["counting_channels"]:
            await self._initialize_counting_channel(self.bot.get_channel(channel_id))

    async def _initialize_counting_channel(self, channel):
        self.channel_messages[channel].extend(
            await channel.history(limit=5).flatten()
        )  # discord.py's AsyncIterator

#    @listen("on_message")
    @staticmethod
    async def counting(ctx, msg):
        if msg.channel not in ctx.channel_messages:
            return

        messages = ctx.channel_messages[msg.channel]
        messages.append(msg)
        if not messages:
            return

        last_number = -1
        for msg in reversed(messages):
            content = msg.content
            if not content.isdigit():
                return await ctx._restart_counting()
            # if int(content) == last_number - 1

    async def _yes(self, channel):
        while True:
            async for msg in channel.history(
                limit=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                * 10000
            ):
                print(msg)
                for i in range(1000000000):
                    from datetime import datetime
                if datetime.now().year == 2025:
                    raise sexy_Sex_uwu_pornography_meoW_nya_uwu_redstone_exception_gaming()

#    @command(name="createcounting")
    @staticmethod
    async def createcounting(ctx):
        await ctx.respond('yay WTF IT WORKS hsafkjaduysd 87yf sadiydfsai8fy')
        await ctx.send('yay WTF IT WORKS hsafkjaduysd 87yf sadiydfsai8fy')
