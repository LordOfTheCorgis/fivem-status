import discord
from datetime import datetime

def create_embed(server_data):
    if not server_data:
        embed = discord.Embed(
            title="Server Status",
            description="Unable to fetch server data. Please check the server.",
            color=discord.Color.red()
        )
        return embed

    embed = discord.Embed(
        title=f"{server_data['server_name']} Status",
        description="Live updates every 15 seconds",
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Players Online",
        value=f"{server_data['player_count']}/{server_data['max_players']}",
        inline=False
    )
    embed.add_field(
        name="Queue",
        value=f"{server_data['queue']} in Queue",
        inline=True
    )
    embed.add_field(
        name="Server Status",
        value="🟢 Online" if server_data else "🔴 Offline",
        inline=True
    )
    embed.set_image(url="attachment://banner.png")
    embed.set_footer(text=f"Last Updated: {datetime.utcnow()} UTC")
    return embed
