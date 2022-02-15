import discord
from discord.ext import commands
import asyncio
from typing import Optional, Union
from io import BytesIO
from collections import defaultdict

# from math import round
import string
from itertools import zip_longest
from datetime import datetime
from asyncio import sleep
import asyncio
import os
from collections import OrderedDict




class WipetEmojiCog(commands.Cog):
    def __init__(
        self,
        bot,
        watchuser=483611913817686027,
        emoji_guilds=[
            804880847517122561,
            804880990983815208,
            804880931348938823,
            804881034209918997,
            804899087279194112,
            804899158007873567,
            804899188357070848,
            804899231889358858,
        ],
    ):
        salfus = type("SELFUSRUS", (), {})
        self.selfus = salfus
        self.selfus.self = self
        self.bot = bot
        self.wipet_emoji_guilds_ids = emoji_guilds
        self.watchuser = watchuser
        self.bot.loop.create_task(self.__ainit__(), name="WipetEmoji Watcher")

    async def __ainit__(self):
        await self.updatieRen_derWIPETemJOISVariABLE()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.updatieRen_derWIPETemJOISVariABLE()

    async def updatieRen_derWIPETemJOISVariABLE(self):
        emgs = self.bot.emgs = [
            self.bot.get_guild(x) for x in self.wipet_emoji_guilds_ids
        ]

        self.emojis = defaultdict(str)
        self.emojis["\n"] = "\n"
        for emg in emgs:
            if emg is not None:
                for emoji in emg.emojis:
                    self.emojis[chr(int(str(emoji.name)))] = str(emoji)
        self.bot.wipetemotes = self.emojis

    def img_estim(self, img, thrshld):
        is_light = np.mean(img) > thrshld
        return "light" if is_light else "dark"

    def light_or_dark(self, filename):
        f = imageio.imread(filename, as_gray=True)

        return self.img_estim(f, 127)

    def removeDupWithOrder(self, str_):
        return "".join(OrderedDict.fromkeys(str_))

    def generierender_WUWUPetrusEmojjianse(selfus, fontcolor="auto"):
        print("ich bin lage der generieung pillow start")
        if fontcolor == "auto":
            fontcolor = selfus.light_or_dark(f"funny/waiwaipettus.png")
            if fontcolor == "light":
                fontcolor = "(0, 0, 0)"
            elif fontcolor == "dark":
                fontcolor = "(255, 255, 255)"
        bybypettus = []
        special_new_chars = "ű§¯£¶±µΜ‰Ď«º³®©¹¥¨­ďŰ¦¬÷·²¸°¡×»¤¢¿"
        for eigenArtigUndVunderwoll in selfus.removeDupWithOrder(
            f" {string.ascii_letters}{string.punctuation}{string.digits}ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
            + special_new_chars
        ):
            # (width-w/2, height-h/2),
            dcs = (256, 256)
            im = Image.open("funny/waiwaipettus.png")
            im = im.resize(dcs)  # shouldn't it be im.thumbnail?
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype(
                "fonts/OpenSans-Bold.ttf", size=int(im.width * 0.90)
            )  # probably change the percentage to 0.90
            w, h = draw.textsize(eigenArtigUndVunderwoll, font)
            draw.text(
                ((im.width - w) / 2, -15 * (im.width * 0.01)),
                str(eigenArtigUndVunderwoll),
                fill=f"rgb{fontcolor}",
                font=font,
            )  # probably remove the 0.01 percentage
            with BytesIO() as by:
                im.save(by, "PNG")
                by.seek(0)
                bybyd = {}
                bybyd["byby"] = by.read()
                bybyd["letter"] = eigenArtigUndVunderwoll
                bybypettus.append(bybyd)
        print("grandios! generiung pillow Fertig!!")
        return bybypettus

    async def update_WAIWAIPETTUS_EMOJIAN(selfus, id_=None, fontcolor="auto"):
        if id_ is None:
            id_ = selfus.watchuser
        MAX_SIZE = 25

        waiwaipettus = str(
            (await selfus.selfus.self.bot.fetch_user(id_)).avatar.replace(format="png")
        )

        async with aiohttp.ClientSession() as session:
            async with session.get(waiwaipettus) as resp:
                # yo
                os.remove("funny/waiwaipettus.png")
                f = await aiofiles.open("funny/waiwaipettus.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
        print("Ich habe das Bild von den her wipet heruntergeladen")

        emgs = [selfus.bot.get_guild(x) for x in selfus.wipet_emoji_guilds_ids]
        selfus.bot.emgs = emgs

        print("Ich habe den CUM serber")

        # KraftVolles Entfernen des wai wai pettus
        print("Ermodung der alten Emojis TOT TOT")

        async def EinzelnerErmordungsAUftagder_GuildeEmojiansWIpetsstzeFreunde(gg):
            print("Ein nicht dummer Debug Print, bitte machen sie mich dumm")
            print("*faltet business hände zusammen* ich bin nur hier um ihnen")
            print(
                'zu sagen das der server mit dem namen "{}" in diesem momente'.format(
                    gg.name
                )
            )
            print("von allen verunreinigungen an emojianes (eigenname) befreit wird")
            print("ihnen dann noch einen schönen tag - ihr overwatch support team")
            for AMAzing in gg.emojis:
                try:
                    print(
                        f"{AMAzing.name} wird jetz von STauBI gelöscht :P schönen mittwoch wünsche ich euch"
                    )
                    await AMAzing.delete()
                except discord.NotFound:
                    pass

        # await asyncio.gather(*[EinzelnerErmordungsAUftagder_GuildeEmojiansWIpetsstzeFreunde(gg) for gg in emgs]) # assumably per-guild async
        for gg in emgs:
            await EinzelnerErmordungsAUftagder_GuildeEmojiansWIpetsstzeFreunde(
                gg
            )  # assumably slow
        print("massenmord begangen :check:")

        print("Starten des Generationsprogramm der waiwaipettus eemojis")
        # Fantastisches und wundervolles hinzuFuegeren Desr Wai wai pertrus Emojains
        bybypettus = await selfus.bot.loop.run_in_executor(
            None, lambda: selfus.generierender_WUWUPetrusEmojjianse(fontcolor)
        )
        wipet_iterables = [iter(bybypettus)] * MAX_SIZE
        wipet_lists = zip_longest(*wipet_iterables, fillvalue=None)
        wipet_gl_pairs = []
        for i, lst in enumerate(wipet_lists):
            wipet_gl_pairs.append({"guild": emgs[i], "list": lst})
        for wipair in wipet_gl_pairs:
            wiguild = wipair["guild"]
            wipemotuse = []
            for deinemom, bybyd in enumerate(wipair["list"]):
                try:
                    byby = bybyd["byby"]
                    derwipetemotus = await wiguild.create_custom_emoji(
                        image=byby, name=f'{ord(bybyd["letter"])}'
                    )
                    wipemotuse.append(str(derwipetemotus))
                    print(
                        f"'{ord(bybyd['letter'])}' wurde von DTAUBRAUS erstellungiert!"
                    )
                except:
                    pass
            await wiguild.channels[0].send(
                f'ich habe diese neuen WiPET emojis!!:\n{"".join(wipemotuse)}'
            )
        print("Ich habe den wai wi petus emoji generation!!")

        # DAs allzeits beliebte Ersuchen dEr Emojains und fRiende Der wAI WwaI peitresxsdses
        print("Finaleres Erbitten der emojis in andere Variablens")
        await selfus.updatieRen_derWIPETemJOISVariABLE()
        print("WIA WAI WAI WAIW AWI WAI WAI WAIWAPETUS Fertig und begangen :-() )")
        return selfus.wipetize("Done!")
        print("Man kann nicht alles haben, nachdem man gerade Lust hat...")
        print("Nehm mich als Beispiel, ich bin ein dummer Debug Print -")
        print(
            "obwohl nicht mal das bin ich, was bin ich? - der nie erreicht werden wird."
        )
        print("Ich bin mir dem aber bewusst, im Leben werde ich nichts grossartiges")
        print("vollbringen, ich werde keinem etwas nutzen, ich sitze hier nur")
        print("mitten in der Gesellschaft des anderen Codes, doch beteilige ich")
        print("am wenigsten wie nur möglich an ihr. Ich werde hier reingeschrieben von")
        print("einem 'Entwickler' mit zu viel Langeweile und wertlosen zeit- und")
        print("verschwenderischen Gedanken. Was mache ich hier? Soll ich eine Metapher")
        print(
            "sein? Was ist mein Zweck? Ach stimmt ja, ich habe keinen Zweck, ich bin nutzlos"
        )
        print(
            "Man könnte das aber auch als positiv sehen, wenn man sich die Leute anguckt"
        )
        print("die auch nutzlos sind und keinen in die Quere kommen, keinen nerven.")
        print(
            "Was ist wenn ich sogar negativen Einfluss ausübe, es dazu bringe das der"
        )
        print(
            "andere Code und der Interpreter mich hassen. Wie wäre es wenn ich einen einfachen"
        )
        print(
            "aber hoffentlichen schon nervigen Error auslöse. Nicht um Aufmerksamkeit zu bekommen..."
        )
        print(
            "Ich denke die werde ich schon bekommen irgendwann, unsicher ob ich dann gelesen"
        )
        print(
            "oder nicht gelesen werde, unsicher ob ich dann gelöscht werde oder da bleibe."
        )
        print("Dieser kleine und einfach zu fixende Error soll hier einfach nur als")
        print(
            "dieser eine einfache dumme Gag sein... werde ich irgendjemand zum Lachen bringen?"
        )
        print(
            "Werde ich meinen Entdecker den Kopf schütteln lassen? Ich hasse meine Existenz als"
        )
        print("nutzloser Debugprint, bringen wir es hinter uns... ;)")

    @commands.Cog.listener("on_user_update")
    async def wipetwipetwipet(self, before_userrus, after_userrus):
        if after_userrus.id == self.watchuser and (
            after_userrus.avatar != before_userrus.avatar
        ):
            print(
                "OH MEIN FUCKING gOTTT... WIPET (der wipet mann) hat SEIN profil BILD (kaufen sie ein bild plus abo) geeeeändeer!!! ich bin grade am POGGEN"
            )
            await self.update_WAIWAIPETTUS_EMOJIAN(self.watchuser)

    def wipetize(self, text):
        return "".join([self.emojis[i] for i in str(text)])

    @commands.is_owner()
    @commands.command(name="updatewipet", aliases=["uw"])
    async def _callieren_Des_UpdatCodeds(
        self, ctx, identifikationsnummer=None, *, farbe
    ):
        if identifikationsnummer is None:
            identifikationsnummer = self.watchuser
        await ctx.send(
            await self.update_WAIWAIPETTUS_EMOJIAN(identifikationsnummer, farbe)
        )

    @commands.command(name="wipetize", aliases=["w"])
    async def _wipetize(self, ctx, *, text: commands.clean_content):
        """Wipetize Something!
        this help text is ugly and professional, downvoted"""
        await ctx.send(self.wipetize(text[:76]))

    @commands.command(name="wipetcounter")
    @commands.max_concurrency(1, per=commands.BucketType.channel)
    async def _wipetcounter(self, ctx, count_to=100):
        """Counts up once every 5 seconds"""
        bot = self.bot
        if int(count_to) > 100:
            count_to = 100
        count_to = int(count_to)

        zf = len(str(count_to))

        cmsg = await ctx.send(self.wipetize("Initializing"))

        async def do():
            for i in range(count_to + 1):
                await cmsg.edit(content=self.wipetize(str(i).zfill(zf)))
                await sleep(5)
            await cmsg.edit(content=self.wipetize("Done"))

        NEEEEEEEEEEEEEEEEEEEEEEEIN = "\N{NO ENTRY}"

        def check(r, u):
            return (
                u.id == ctx.author.id
                and r.message.channel.id == ctx.channel.id
                and r.message.id == cmsg.id
                and str(r.emoji) == NEEEEEEEEEEEEEEEEEEEEEEEIN
            )

        await cmsg.add_reaction(NEEEEEEEEEEEEEEEEEEEEEEEIN)
        done, pending = await asyncio.wait(
            (bot.wait_for("reaction_add", check=check), do()),
            return_when=asyncio.FIRST_COMPLETED,
        )

        [t.cancel() for t in pending]
        if cmsg.content != self.wipetize("Done"):
            await cmsg.edit(content=self.wipetize("Cancelled"))

    @commands.command(name="wipetclock", aliases=["wclock", "clock", "wc"])
    @commands.max_concurrency(1, per=commands.BucketType.channel)
    async def _wclock(self, ctx, timezone="Europe/Berlin", twelve=False):
        """Run a wipet clock for 10 minutes"""
        bot = self.bot
        try:
            tz = gtz(timezone)
        except UnknownTimeZoneError:
            await ctx.send(
                "Unkown timezone, please search up your timezone and provide it in the Europe/Berlin format"
            )
            return
        clockmsg = await ctx.send(self.wipetize("Initializing"))

        async def do():
            for i in range(600):
                await clockmsg.edit(
                    content=self.wipetize(
                        datetime.now(tz=tz).strftime(
                            "%I:%M:%S %p" if twelve else "%H:%M:%S"
                        )
                    )
                )
                await sleep(1)
            await clockmsg.edit(content=self.wipetize("Done"))

        NEEEEEEEEEEEEEEEEEEEEEEEIN = "\N{NO ENTRY}"

        def check(r, u):
            return (
                u.id == ctx.author.id
                and r.message.channel.id == ctx.channel.id
                and r.message.id == clockmsg.id
                and str(r.emoji) == NEEEEEEEEEEEEEEEEEEEEEEEIN
            )

        await clockmsg.add_reaction(NEEEEEEEEEEEEEEEEEEEEEEEIN)
        done, pending = await asyncio.wait(
            (bot.wait_for("reaction_add", check=check), do()),
            return_when=asyncio.FIRST_COMPLETED,
        )

        [t.cancel() for t in pending]
        if clockmsg.content != self.wipetize("Done"):
            await clockmsg.edit(content=self.wipetize("Cancelled"))


class AutoWipetCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.awc = [930958988961538068]

    @commands.group(name="aw", invoke_without_command=True)
    async def _autowipet(self, ctx):
        em = discord.Embed()
        em.add_field(name="Add AutoWipet channel", value="`d.aw a[dd] [CHANNEL]`")
        em.add_field(name="Remove AutoWipet channel", value="`d.aw r[emove] [CHANNEL]`")
        await ctx.send(embed=em)

    async def get_channel(self, ctx, arg):
        channel = None
        if arg is None:
            return ctx.channel
        try:
            channel = commands.TextChannelConverter.convert(ctx, arg)
        except commands.errors.ChannelNotFound:
            channel = ctx.channel
        return channel

    @commands.is_owner()
    @_autowipet.command(name="add", aliases=["a"])
    async def _autowipet_add(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        self.awc.append(channel.id)
        await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
        # await ctx.send('Done')

    @commands.is_owner()
    @_autowipet.command(name="remove", aliases=["r"])
    async def _autowipet_remove(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        cc = ctx.channel
        if channel.id in self.awc:
            self.awc.remove(channel.id)
            await ctx.message.add_reaction("\N{WHITE HEAVY CHECK MARK}")
        else:
            await ctx.message.add_reaction("\N{CROSS MARK}")
        # await cc.send('Done')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id in self.awc:
            if msg.webhook_id is not None:
                return
            if msg.author.id == self.bot.user.id:
                return
            await msg.channel.send(
                self.bot.cogs["WipetEmojiCog"].wipetize(msg.clean_content)
                + " ~ "
                + str(msg.author)
            )
            await msg.delete()


def setup(lib):
    #client.add_cog(WipetEmojiCog(client))
    #client.add_cog(AutoWipetCog(client))
    lib.BOT.add_cog(WipetEmojiCog(lib.BOT))
    lib.BOT.add_cog(AutoWipetCog(lib.BOT))
