import disnake
from disnake.ext import commands
import os

from cogs.data import settings

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} started!')

@bot.event
async def on_guild_join(guild):
    pass


for filename in os.listdir("./cogs/commands"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.commands.{filename[:-3]}')
        print("Loaded: " + f"cogs.commands.{filename[:-3]}")

bot.run(settings.token)