from discord.ext import tasks, commands
import discord
import json
from utils.fetch_data import fetch_server_data

with open("config.json") as f:
    config = json.load(f)

TOKEN = config["bot_token"]
CHANNEL_ID = config["channel_id"]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

status_message = None

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    update_status.start()

@tasks.loop(seconds=15)
async def update_status():
    global status_message
    channel = bot.get_channel(CHANNEL_ID)

    try:
        server_data = fetch_server_data(config["server_ip"], config["server_port"])
        print(server_data)

        if not server_data or not isinstance(server_data, dict):
            raise ValueError("Invalid or empty server data")

        embed = discord.Embed(
            title=config["embed_customization"]["title"],
            description=config["embed_customization"]["description"],
            color=discord.Color.blue()
        )
        embed.set_footer(text=config["embed_customization"]["footer"])

        if "author" in config["embed_customization"]:
            embed.set_author(
                name=config["embed_customization"]["author"]["name"],
                icon_url=config["embed_customization"]["author"]["icon_url"]
            )

        if "thumbnail" in config["embed_customization"]:
            embed.set_thumbnail(url=config["embed_customization"]["thumbnail"])

        embed.add_field(
            name="Server Population", 
            value=f"{server_data.get('player_count', 'N/A')}/{server_data.get('max_players', 'N/A')}"
        )
        embed.add_field(
            name="Queue", 
            value=server_data.get("queue", "N/A")
        )
        embed.add_field(
            name="Server Status", 
            value="Online" if server_data.get("status", True) else "Offline"
        )

        view = discord.ui.View()
        for button in config.get("buttons", []):
            url = button.get("url", "#")
            if url.startswith(("http://", "https://", "discord://")):
                view.add_item(discord.ui.Button(label=button.get("label", "Button"), url=url))
            else:
                print(f"Invalid URL scheme detected and skipped: {url}")

        if not status_message:
            status_message = await channel.send(embed=embed, view=view)
        else:
            await status_message.edit(embed=embed, view=view)

    except Exception as e:
        print(f"Error updating status: {e}")
        embed = discord.Embed(
            title="Error Updating Status",
            description="There was an issue fetching or displaying server data.",
            color=discord.Color.red()
        )
        if status_message:
            await status_message.edit(embed=embed)
        else:
            await channel.send(embed=embed)

bot.run(TOKEN)
