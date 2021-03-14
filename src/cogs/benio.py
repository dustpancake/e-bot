import logging

import discord
from discord.ext import commands

_ID = 691729794462908487
FILE = "benmessages.txt"

class BenIO(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logging = logging.getLogger(__name__)

    def _append_message(self, content):
        with open(FILE, "a") as f:
            f.write(f"\n\ncontent")

    @commands.Cog.listener()
    async def on_message(self, message):
        self.logging.info(f"{message.author.name}, {message.author.id}")
        if message.author.name == "shellywell123":
            self._append_message(message.content)
        
def setup(bot):
    bot.add_cog(
        BenIO(bot)
    )

    return