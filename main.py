import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

intents = nextcord.Intents.default()
bot = commands.Bot(intents=intents)

@bot.slash_command(name="ggrks", description="Googleで調べます")
async def ggrks(
  interaction: Interaction,
  text: str = SlashOption(description="調べたいテキスト")
):
  search_url = f"https://www.google.com/search?q={text}"
  await interaction.response.send_message(search_url)

if __name__ == "__main__":
  bot.run(TOKEN)