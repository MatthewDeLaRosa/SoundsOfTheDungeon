import discord
from discord import FFmpegPCMAudio, guild, Guild
from discord.ext import commands
from discord_buttons_plugin import *
from discord import Intents

intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
buttons = ButtonsClient(bot)


@bot.event
async def on_ready():
    print("Beep Boop")


@buttons.click
async def join(ctx):
    member = ctx.guild.get_member(ctx.member.id)
    if member.voice.channel:
        channel = member.voice.channel
        await channel.connect()
        await ctx.reply("The bot has joined the channel.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def leave(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.reply("The bot has left the channel.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def fire(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("fire.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Fire**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def waves(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("ocean.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Waves**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def explosion(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("explosion.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Explosion**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)

@buttons.click
async def thunder(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("thunder.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Thunder**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def rain(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("rain.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Rain**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def crowd(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("crowd.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Crowd**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def clink(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clink.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Clink**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def roar(ctx):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("roar.mp3"))
    ctx.guild.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.reply("The bot has begun playing **Roar**. To play another sound you must wait for this sound to end or click **Stop**.", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def play(ctx):
    ctx.guild.voice_client.resume()
    await ctx.reply("The bot has begun **playing** the sound", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def pause(ctx):
    ctx.guild.voice_client.pause()
    await ctx.reply("The bot has **paused** the sound", flags=MessageFlags().EPHEMERAL)


@buttons.click
async def stop(ctx):
    ctx.guild.voice_client.stop()
    await ctx.reply("The bot has **stopped** the sound", flags=MessageFlags().EPHEMERAL)


@bot.command()
async def sb(ctx):
    await buttons.send(
        content="**SoundBoard**",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label="Fire",
                    style=2,
                    custom_id="fire"
                ),
                Button(
                    label="Waves",
                    style=2,
                    custom_id="waves"
                ),
                Button(
                    label="Explosion",
                    style=2,
                    custom_id="explosion"
                ),
                Button(
                    label="Thunder",
                    style=2,
                    custom_id="thunder"
                )
            ]),



            ActionRow([
                Button(
                    label="Rain",
                    style=2,
                    custom_id="rain"
                ), Button(
                    label="Crowd",
                    style=2,
                    custom_id="crowd"
                ), Button(
                    label="Clink",
                    style=2,
                    custom_id="clink"
                ), Button(
                    label="Roar",
                    style=2,
                    custom_id="roar"
                )
             ]),

            ActionRow([
                Button(
                    label="Join",
                    style=3,
                    custom_id="join"
                ), Button(
                    label="Leave",
                    style=ButtonType().Danger,
                    custom_id="leave"
                ), Button(
                    label="Play",
                    style=1,
                    custom_id="play"
                ), Button(
                    label="Pause",
                    style=1,
                    custom_id="pause"
                ), Button(
                    label="Stop",
                    style=1,
                    custom_id="stop"
                )

            ])
        ]
    )


bot.run(TOKEN)
