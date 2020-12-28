import discord_rpc
import win32gui, win32api
import time


# Vars
APP_ID = 761471072754729000 # Enter CLIENT_ID ur application here


# Functions
def readyCallback(user):
    print(f"Auth as {user['username']}#{user['discriminator']}")


def disconnectedCallback(code, msg):
    print(f"Disconnected becouse {code}: {msg}")


def errorCallback(code, msg):
    print(f"Error {code}: {msg}")


# Start
if __name__ == "__main__":
    # Callback
    callbacks = {
        "ready": readyCallback,
        "disconnected": disconnectedCallback,
        "error": errorCallback,
    }
    discord_rpc.initialize(APP_ID, callbacks=callbacks, log=False)


    # Update presence every 1second
    name = None
    while True:
        # Window title & Timestamp
        old_name = name
        name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if name != old_name:
            seconds = time.time()

        # Presence
        discord_rpc.update_presence(
            **{
                "details": win32api.GetComputerName() + "/" + win32api.GetUserName(),
                "state": name[0:127],
                "start_timestamp": seconds,
                "large_image_key": "large_image",
                "large_image_text": "Я - банан, я я банан банан, чищу банан",
                #"small_image_key": "key 4 small",
                #"small_image_text": "text 4 small"
            }
        )

        discord_rpc.update_connection()
        time.sleep(2)
        discord_rpc.run_callbacks()

    # Shutdown if user press CTRL+C
    discord_rpc.shutdown()
