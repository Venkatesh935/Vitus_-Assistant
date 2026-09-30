from commands.system_commands import (
    open_chrome,
    open_youtube,
    open_google,
    open_notepad,
    open_downloads,
    open_vscode,
    take_screenshot,
    increase_volume,
    decrease_volume,
    mute_volume
)


def process_command(command):

    command = command.lower().strip()

    # Chrome
    if "chrome" in command:
        return open_chrome()

    # YouTube
    elif "youtube" in command:
        return open_youtube()

    # Google
    elif "google" in command:
        return open_google()

    # Notepad
    elif "notepad" in command:
        return open_notepad()

    # Downloads
    elif "download" in command:
        return open_downloads()

    # VS Code
    elif "visual studio code" in command or "vs code" in command:
        return open_vscode()

    # Screenshot
    elif "screenshot" in command or "screen shot" in command:
        return take_screenshot()

    # Volume Up
    elif "increase volume" in command or "volume up" in command:
        return increase_volume()

    # Volume Down
    elif "decrease volume" in command or "volume down" in command:
        return decrease_volume()

    # Mute
    elif "mute" in command:
        return mute_volume()

    # Unknown command
    else:
        return "Sorry, I don't know that command yet."