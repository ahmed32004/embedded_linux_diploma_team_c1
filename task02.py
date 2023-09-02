#!/usr/bin/python3
import keyboard
import subprocess


def on_trigger():
    subprocess.run(['nautilus', '/home/ahmed/Desktop'])


def shortcut_listener():
    shortcut = "ctrl + alt + s"
    keyboard.add_hotkey(shortcut, on_trigger)
    keyboard.wait()


shortcut_listener()
