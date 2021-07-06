import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=str("d."), intents=discord.Intents.default())
bot.TOKEN = "TOKEN_HERE"


@bot.event
async def on_ready():
    print("Bot is ready!")

for i in os.listdir('cogs'):
    if i.endswith('.py'):
      if not i.startswith('_'):
        bot.load_extension(f"cogs.{i[:-3]}")


if __name__ == '__main__':
  bot.run(bot.TOKEN)
