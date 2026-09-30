import os

content = '''import os
import subprocess
import pyautogui

def take_screenshot():
    print("📸 Taking screenshot...")
    screenshot = pyautogui.screenshot()
    path = os.path.join(os.path.expanduser("~"), "Desktop", "vitus_screenshot.png")
    screenshot.save(path)
    return "Screenshot taken and saved on your desktop."

def increase_volume():
    print("🔊 Increasing volume...")
    for _ in range(5):
        pyautogui.press("volumeup")
    return "Volume increased."

def decrease_volume():
    print("🔉 Decreasing volume...")
    for _ in range(5):
        pyautogui.press("volumedown")
    return "Volume decreased."

def mute_volume():
    print("🔇 Muting volume...")
    pyautogui.press("volumemute")
    return "Volume muted."

def lock_computer():
    print("🔒 Locking computer...")
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking the computer."

def sleep_computer():
    print("💤 Putting computer to sleep...")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "Putting the computer to sleep."

def restart_computer():
    print("🔄 Restarting computer...")
    os.system("shutdown /r /t 5")
    return "Restarting the computer in 5 seconds."

def shutdown_computer():
    print("🛑 Shutting down computer...")
    os.system("shutdown /s /t 5")
    return "Shutting down the computer in 5 seconds."
'''

with open("commands/system_commands.py", "w", encoding="utf-8") as f:
    f.write(content)
