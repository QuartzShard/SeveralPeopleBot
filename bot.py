## Initialization
import os
import discord
from common import config, log
from discord.ext import commands

## Constants and Config
intents = discord.Intents.default()

## Define severalBot
class severalBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ## Load Cogs - Modules in ./cogs directory
        for file in os.listdir("./cogs"):             # List contents of ./cogs
            if file.endswith(".py"):                  # Find ".py" files
                name = file[:-3]                      # Trim ".py" from string
                self.load_extension(f"cogs.{name}")   # Load Cog

    ## Log when ready
    async def on_ready(self):
        log.log('--------------------------------')
        log.log('Bot Ready.')
        log.log(f'Logged in as {self.user.name}')
        log.log(f'User ID: {self.user.id}')
        log.log('--------------------------------')
        await client.change_presence(status=discord.Status.offline)

## Create instance of severalBot using config.cfg['discord']['token']
client = severalBot(command_prefix=config.cfg['options']['prefix'], intents=intents)
client.run(config.cfg['discord']['token'])