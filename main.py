import asyncio
import os

import discord
from discord.ext import commands

from extensions import initial_extensions
from utils import cfg, db, logger

intents = discord.Intents.all()
mentions = discord.AllowedMentions(everyone=False, users=True, roles=False)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # force the config object and database connection to be loaded
        if cfg and db:
            logger.info("Presetup phase completed! Connecting to Discord...")

    async def setup_hook(self):
        bot.remove_command("help")
        for extension in initial_extensions:
            await self.load_extension(extension)


bot = Bot(command_prefix='!', intents=intents, allowed_mentions=mentions)


@bot.event
async def on_ready():
    print("Blootooth")
    logger.info(
        f'Logged in as: {bot.user.name} - {bot.user.id} ({discord.__version__})')
    logger.info(f'Successfully logged in and booted...!')
    await bot.change_presence(status=discord.Status.invisible)


async def main():
    async with bot:
        await bot.start(os.environ.get("BLOOTOOTH_TOKEN"), reconnect=True)

asyncio.run(main())
