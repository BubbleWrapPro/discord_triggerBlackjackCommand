# Discord Blackjack Auto Claim Bot

A simple Python bot that automatically triggers `/spin` and `/claimall` slash commands for Discord Blackjack bot (https://discordapp.com/oauth2/authorize?client_id=478202666355523585&scope=bot%20applications.commands&permissions=347200) at regular intervals, using the [discum](https://github.com/Merubokkusu/Discord-S.C.U.M) library.

---

## Features

- **Automates** `/spin` command every 5 minutes and `/claimall` every hour.
- **Easy to configure**: Just provide your Discord user token and relevant IDs.
- **Headless**: Runs in the background, no UI necessary.

---

## ⚠️ Disclaimer

- **This bot requires your Discord account token.** Using user tokens to automate actions on Discord is against Discord's Terms of Service. Use this project **at your own risk**. Your account may be banned or restricted.
- This project is intended for educational purposes only.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/PapierBulle1631/autoBlackjack.git
cd autoBlackjack
```

### 2. Install dependencies

```bash
pip install discum
```

### 3. Configuration

Open the script and edit the following variables:

```python
TOKEN = "YOUR_DISCORD_USER_TOKEN" (line 8)
GUILD_ID = "YOUR_SERVER_ID" (line 16)
CHANNEL_ID = "YOUR_CHANNEL_ID" (line 17)
APPLICATION_ID = "BLACKJACK_BOT_APPLICATION_ID" (line 18)
```

- `TOKEN`: Your Discord account's token.
- `GUILD_ID`: The server (guild) ID where the Blackjack bot is running.
- `CHANNEL_ID`: The channel ID where you want the commands to be sent.
- `APPLICATION_ID`: The application ID of the Blackjack bot (get it from the bot's slash commands).

**Never share your Discord token with anyone!**

### 4. Running

```bash
python main.py
```

The bot will start sending `/spin` every 5 minutes and `/claimall` every hour.

---

## How it Works

- Uses the [discum](https://github.com/Merubokkusu/Discord-S.C.U.M) library to log in as a user and send raw slash commands.
- Schedules commands with Python's `time` module.
- Runs indefinitely until stopped. (Ctrl+C)

---

## Notes

- The command versions and IDs may change if the Blackjack bot updates its slash commands. TO CHECK THEM :
    + CONNECT TO DISCORD WITH WEB VERSION
    + GO IN THE NETWORK TAB IN THE DEVELOPPER MODE (F12)
    + SEND THE COMMAND YOU WANT AND NOTE THE ID AND VERSION YOU SEE IN THE FRAME
- This bot does **not** interact with Discord's API in an officially supported way.

---

## License

This project is provided for educational purposes and is **not affiliated with Discord** or any Blackjack bot developers.


---
