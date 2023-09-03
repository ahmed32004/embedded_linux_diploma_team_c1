#!/usr/bin/python3
import pyautogui
import time
import os

def open_vscode():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.typewrite('vscode')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)

def download_extension(extension_name):
    cwd = os.getcwd()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'X')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('del')
    time.sleep(1)
    pyautogui.typewrite(extension_name)
    button_install_location = None
    try:
        time.sleep(3)
        button_install_location = pyautogui.locateOnScreen(f'{cwd}/install.png', confidence=0.65)
        time.sleep(2)
        button_install_point = pyautogui.center(button_install_location)
        time.sleep(2)
        pyautogui.click(button_install_point.x, button_install_point.y)
    except:
        print (f"Extension with ID: {extension_name} might be already installed.")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'E')
    time.sleep(3)

def main():
    extension_id_list = [ 'llvm-vs-code-extensions.vscode-clangd', 'matepek.vscode-catch2-test-adapter', 'amiralizadeh9480.cpp-helper', 'twxs.cmake', 'ms-vscode.cmake-tools' ]    
    open_vscode()
    for extension_id in extension_id_list:
        download_extension(extension_id)

if __name__ == "__main__":
    main()
    




