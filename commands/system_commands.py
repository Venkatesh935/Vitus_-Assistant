import os
import webbrowser
import subprocess
import pyautogui


def open_chrome():
    print("🌐 Opening Google Chrome...")
    os.startfile("chrome.exe")
    return "Opening Google Chrome."


def open_youtube():
    print("▶️ Opening YouTube...")
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."


def open_google():
    print("🔎 Opening Google...")
    webbrowser.open("https://www.google.com")
    return "Opening Google."


def open_notepad():
    print("📝 Opening Notepad...")
    subprocess.Popen("notepad.exe")
    return "Opening Notepad."


def open_downloads():
    print("📁 Opening Downloads...")
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    os.startfile(downloads_path)
    return "Opening Downloads folder."


def open_vscode():
    print("💻 Opening Visual Studio Code...")
    subprocess.Popen("code")
    return "Opening Visual Studio Code."


def take_screenshot():
    print("📸 Taking screenshot...")

    screenshot = pyautogui.screenshot()

    path = os.path.join(
        os.path.expanduser("~"),
        "Desktop",
        "nova_screenshot.png"
    )

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