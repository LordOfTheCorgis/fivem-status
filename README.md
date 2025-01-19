# FiveM Server Status Bot

A customizable Discord bot that displays the live status of your FiveM server. The bot updates every 15 seconds, showing server population, queue size, and online status in a visually appealing embed. It also includes customizable buttons for additional functionality, like connecting to the server or visiting a store.

---

## Features
- **Live Server Status Updates**: Displays server population, queue, and status in real-time.
- **Customizable Embed**: Add a title, description, footer, author details, and thumbnail to match your server's branding.
- **Interactive Buttons**: Include buttons that link to your server, store, website, or other resources.
- **Error Handling**: Informs the Discord channel if the bot encounters an issue while fetching server data.

---

## Getting Started

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- A FiveM server with a valid IP and port
- A Discord bot token (get one from the [Discord Developer Portal](https://discord.com/developers/applications))

---

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fivem-server-status-bot.git
   cd fivem-server-status-bot
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Rename `example-config.json` to `config.json`:
   ```bash
   mv example-config.json config.json
   ```

4. Edit the `config.json` file:
   - Replace placeholders like `YOUR_BOT_TOKEN` and `127.0.0.1` with your actual bot token, server IP, and port.
   - Customize the embed title, description, footer, author, and buttons as desired.

5. Run the bot:
   ```bash
   python bot.py
   ```

---

### Configuration File (`config.json`)

```json
{
  "bot_token": "YOUR_BOT_TOKEN",
  "channel_id": 123456789012345678,
  "server_ip": "127.0.0.1",
  "server_port": 30120,
  "embed_customization": {
    "title": "My FiveM Server Status",
    "description": "Stay updated on the server population, queue, and status.",
    "footer": "Updated every 15 seconds.",
    "author": {
      "name": "Server Bot",
      "icon_url": "https://example.com/author-icon.png"
    },
    "thumbnail": "https://example.com/thumbnail.png"
  },
  "buttons": [
    {
      "label": "Connect to Server",
      "url": "https://yourwebsite.com/connect"
    },
    {
      "label": "Visit Store",
      "url": "https://yourstore.com"
    }
  ]
}
```

- **`bot_token`**: Your Discord bot token.
- **`channel_id`**: The ID of the channel where the bot should post updates.
- **`server_ip` and `server_port`**: Your FiveM server's IP and port.
- **Embed Customization**:
  - `title`, `description`, `footer`: Customize the embed text.
  - `author`: (Optional) Add an author name and profile picture.
  - `thumbnail`: (Optional) Add a thumbnail image to the embed.
- **Buttons**:
  - Add buttons with labels and valid URLs (must start with `http://`, `https://`, or `discord://`).

---

### Example Output
The bot will post a Discord embed like this:

![Example Embed](https://example.com/embed-preview.png)

---

## Contributing
Feel free to open issues or submit pull requests to improve the bot. Contributions are always welcome!

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Troubleshooting
1. **Invalid Form Body Error**:
   - Ensure button URLs in `config.json` start with a valid scheme (`http://`, `https://`, or `discord://`).

2. **Bot Not Responding**:
   - Check if the bot has permission to send messages in the specified channel.
   - Verify the `channel_id` and `bot_token` in `config.json` are correct.

3. **Server Data Issues**:
   - Ensure the `server_ip` and `server_port` in `config.json` point to a valid FiveM server.

---

Enjoy using the bot! If you run into any issues, feel free to reach out.
