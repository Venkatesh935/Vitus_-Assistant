import os

APPLICATION_WHITELIST = {
    "open_chrome": "chrome.exe",
    "open_edge": "msedge.exe",
    "open_notepad": "notepad.exe",
    "open_calculator": "calc.exe",
    "open_file_explorer": "explorer.exe",
    "open_command_prompt": "cmd.exe",
    "open_powershell": "powershell.exe",
    "open_vscode": "code"
}

def open_application(intent):
    app_exe = APPLICATION_WHITELIST.get(intent)
    if app_exe:
        print(f"🚀 Launching {app_exe}...")
        os.system(f"start {app_exe}")
        return f"Opening {app_exe.replace('.exe', '')}."
    return "I am not authorized to open that application."
