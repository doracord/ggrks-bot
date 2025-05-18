import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import re

TOKEN = "TOKEN"

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

@bot.slash_command(name="ggrks", description="Googleで調べます")
async def ggrks(
  interaction: Interaction,
  text: str = SlashOption(description="調べたいテキスト")
):
  search_url = f"https://www.google.com/search?q={text}"
  await interaction.response.send_message(search_url)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.strip().lower() == "ggrks" and message.reference:
        replied_message = await message.channel.fetch_message(message.reference.message_id)
        if replied_message:
            search_url = f"https://www.google.com/search?q={replied_message.content}"
            await message.channel.send(f"しらべてみよう！: {replied_message.content}\n{search_url}")
    await bot.process_commands(message)

if __name__ == "__main__":
  bot.run(TOKEN)
