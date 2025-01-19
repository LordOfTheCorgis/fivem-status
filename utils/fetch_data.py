import requests

def fetch_server_data(ip, port):
    try:
        players_url = f"http://{ip}:{port}/players.json"
        info_url = f"http://{ip}:{port}/info.json"

        players = requests.get(players_url).json()
        server_info = requests.get(info_url).json()

        return {
            "player_count": len(players),
            "max_players": server_info.get("vars", {}).get("sv_maxClients", "Unknown"),
            "server_name": server_info.get("vars", {}).get("sv_hostname", "Unknown"),
            "queue": 0,
        }
    except Exception as e:
        print(f"Error fetching server data: {e}")
        return None
