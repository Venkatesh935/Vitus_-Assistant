import re

INTENTS = {
    "open_chrome": [r"\bchrome\b", r"\bgoogle chrome\b"],
    "open_edge": [r"\bedge\b", r"\bmicrosoft edge\b"],
    "open_firefox": [r"\bfirefox\b"],
    "open_notepad": [r"\bnotepad\b"],
    "open_calculator": [r"\bcalculator\b", r"\bcalc\b"],
    "open_file_explorer": [r"\bfile explorer\b", r"\bwindows explorer\b", r"\bfiles\b"],
    "open_vscode": [r"\bvs code\b", r"\bvisual studio code\b", r"\bvscode\b"],
    "open_task_manager": [r"\btask manager\b"],
    "open_settings": [r"\bsettings\b", r"\bcontrol panel\b"],
    "open_command_prompt": [r"\bcommand prompt\b", r"\bcmd\b"],
    "open_powershell": [r"\bpowershell\b"],
    
    "search_web": [r"\bsearch for\b", r"\bsearch google\b", r"\bgoogle\b"],
    "search_youtube": [r"\bsearch youtube\b", r"\bplay on youtube\b"],
    "open_google": [r"\bopen google\b"],
    "open_youtube": [r"\bopen youtube\b"],
    "open_gmail": [r"\bopen gmail\b", r"\bcheck my email\b"],
    "open_github": [r"\bopen github\b"],
    "open_linkedin": [r"\bopen linkedin\b"],
    "open_chatgpt": [r"\bopen chatgpt\b"],
    
    "take_screenshot": [r"\bscreenshot\b", r"\btake a screenshot\b"],
    "increase_volume": [r"\bvolume up\b", r"\bincrease volume\b", r"\blouder\b"],
    "decrease_volume": [r"\bvolume down\b", r"\bdecrease volume\b", r"\bquieter\b"],
    "mute_volume": [r"\bmute\b", r"\bsilence\b"],
    "lock_pc": [r"\block computer\b", r"\block pc\b", r"\block screen\b"],
    "sleep_pc": [r"\bsleep\b", r"\bgo to sleep\b"],
    "restart": [r"\brestart\b", r"\breboot\b"],
    "shutdown": [r"\bshut down\b", r"\bshutdown\b", r"\bturn off computer\b"],
    
    "set_reminder": [r"\bremind me\b", r"\bset a reminder\b", r"\bset reminder\b"],
    "check_weather": [r"\bweather\b", r"\btemperature\b"],
    "send_email": [r"\bsend email\b", r"\bemail\b", r"\bsend an email\b"],
    "system_information": [r"\bsystem\b", r"\bcpu\b", r"\bram\b", r"\bbattery\b", r"\bmemory\b"],
    
    # Phase 21: File and Folder Control
    "open_folder": [
        r"\bopen downloads\b", r"\bopen documents\b", r"\bopen desktop\b", 
        r"\bopen pictures\b", r"\bopen music\b", r"\bopen videos\b", r"\bopen my\b"
    ],
    "find_file": [r"\bfind my\b", r"\bfind the\b", r"\blocate my\b", r"\bwhere is my\b", r"\bsearch for file\b"],
    
    "analyze_vision": [r"\\bwhat do you see\\b", r"\\bwhat am i holding\\b", r"\\blook at this\\b", r"\\bwhat is this\\b"],
    "exit": [r"\bexit\b", r"\bquit\b", r"\bstop vitus\b"]
}

def detect_intent(command):
    command = command.lower()
    for intent, patterns in INTENTS.items():
        for pattern in patterns:
            if re.search(pattern, command):
                return intent
    return "unknown"