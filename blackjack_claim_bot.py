# Discord Blackjack Auto Claim Bot

import discum
import time
import json

# ========== USER SETUP ==========
TOKEN = "Your_Discord_Bot_Token_Here"  # Replace with your bot token

# ========== MAIN BOT LOGIC ==========

def main():
    bot = discum.Client(token=TOKEN, log=False)
    
    # === Fill these with the correct values ===
    GUILD_ID = "YOUR_SERVER_ID"
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    APPLICATION_ID = "BLACKJACK_BOT_APPLICATION_ID"
    
    COMMAND_NAME_SPIN = "spin"
    COMMAND_NAME_CLAIMALL = "claimall"
    # add all the command you want to trigger here (type /help to see the available commands)

    

    # Scheduling
    last_spin = 0
    last_claimall = 0

    print("\nStarting main loop...")
    while True:
        now = time.time()
        if now - last_spin > 5 * 60:
            print("Triggering /spin...")
            bot.triggerSlashCommand(
                applicationID=APPLICATION_ID,
                guildID=GUILD_ID,
                channelID=CHANNEL_ID,
                data={"version":"973027931213398027",
                      "id":"973027931213398026",
                      "name":COMMAND_NAME_SPIN,
                      "type":1,
                      "options":[]
                    }
            )
            last_spin = now
        if now - last_claimall > 60 * 60:
            print("Triggering /claimall...")
            bot.triggerSlashCommand(
                applicationID=APPLICATION_ID,
                guildID=GUILD_ID,
                channelID=CHANNEL_ID,
                data={"version":"973027843007209483",
                      "id":"973027843007209482",
                      "name":COMMAND_NAME_CLAIMALL,
                      "type":1,
                      "options":[]
                    }
            )
            last_claimall = now
        else:
            print("Waiting for next cycle...")
        time.sleep(60)  # Sleep for 1 minute before checking again

if __name__ == "__main__":
    main()