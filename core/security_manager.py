from voice.text_to_speech import speak
from voice.speech_to_text import listen

ALLOWED_INTENTS = {
    'open_chrome', 'open_edge', 'open_firefox', 'open_notepad', 'open_calculator', 
    'open_file_explorer', 'open_vscode', 'open_task_manager', 'open_settings', 
    'open_command_prompt', 'open_powershell', 
    'open_google', 'open_youtube', 'open_gmail', 'open_github', 'open_linkedin', 
    'open_chatgpt', 'open_google_maps', 'open_youtube_music', 'play_music', 
    'search_youtube', 'search_web', 
    'take_screenshot', 'increase_volume', 'decrease_volume', 'mute_volume', 
    'shutdown', 'restart', 'lock_pc', 'sleep_pc',
    'send_email', 'read_email', 'check_weather', 'set_alarm', 'set_reminder', 
    'tell_time', 'tell_date', 'calculator', 'system_information', 
    'open_folder', 'find_file', 'analyze_vision',
    'exit', 'unknown'
}

DANGEROUS_INTENTS = {
    'shutdown',
    'restart',
    'format',
    'delete',
    'terminate_process'
}

def is_intent_allowed(intent):
    return intent in ALLOWED_INTENTS

def requires_confirmation(intent):
    return intent in DANGEROUS_INTENTS

def confirm_action(action_name):
    print(f"⚠️ Security check: Requires confirmation to {action_name}.")
    speak(f"Are you sure you want to {action_name}?")
    
    confirmation = listen().lower()
    
    if "yes" in confirmation or "yeah" in confirmation or "do it" in confirmation or "confirm" in confirmation:
        print("✅ Action confirmed.")
        return True
    else:
        print("❌ Action cancelled.")
        speak("Action cancelled.")
        return False
