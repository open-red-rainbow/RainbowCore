import base64
import orjson

class MinecraftModule:
    def __init__(self, bot) -> None:
        self.bot = bot

    @command(name="minecraft")
    async def _minecraft(self, ctx, user):
        async with ctx.typing():
            uuid = await self.bot.mojang.name_to_uuid(user)
            name_history = [x.name for x in await self.bot.mojang.get_name_history(uuid)]
            current_name = name_history[0]
            em = discord.Embed(title=f'{current_name}\'s Minecraft Infos')
            em.set_thumbnail(url=f'https://crafatar.com/renders/body/{uuid}')
            em.add_field(name="*Name-History*", description='\n'.join(name_history))
            await ctx.send(em)

def setup(bot):
    bot.add_module(MinecraftModule())
