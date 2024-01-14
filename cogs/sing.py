import nextcord
from nextcord.ext import commands
import asyncio


class Sing(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def sing(self, ctx):
        channel = ctx.author.voice.channel
        if channel:
            if ctx.voice_client:
                await ctx.voice_client.disconnect()
            vc = await channel.connect()
            await ctx.send(f"Joined {channel.name}!")
            source = await nextcord.FFmpegOpusAudio.from_probe("./song/supaidol.mp3", method="fallback")
            vc.play(source)
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()
        else:
            await ctx.send("You are not in a voice channel!")
        #source = await nextcord.FFmpegOpusAudio.from_probe("./song/supaidol.mp3", method="fallback")
        #await vc.play(source)


    @commands.command()
    async def stop(self, ctx):
            channel = ctx.author.voice.channel
            if channel:
                if ctx.voice_client:
                    ctx.voice_client.stop()
                    await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        channel = ctx.author.voice.channel
        if channel:
            if ctx.voice_client:
                ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        channel = ctx.author.voice.channel
        if ctx.voice_client:
            ctx.voice_client.resume()
        


def setup(bot : commands.Bot):
    bot.add_cog(Sing(bot))
