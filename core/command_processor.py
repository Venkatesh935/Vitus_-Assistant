from core.intent_manager import detect_intent
from commands.application_commands import open_application, APPLICATION_WHITELIST
from commands.web_commands import open_website, search_web, search_youtube, WEBSITES
from commands.system_commands import (
    take_screenshot, increase_volume, decrease_volume,
    mute_volume, lock_computer, sleep_computer, restart_computer, shutdown_computer
)
from commands.productivity_commands import set_reminder, check_weather
from commands.email_commands import send_email
from commands.info_commands import system_information
from commands.file_commands import open_folder, find_file
from commands.vision_commands import analyze_vision
from ai.ai_engine import process_with_ai
from core.memory_manager import conversation_memory
from core.security_manager import is_intent_allowed, requires_confirmation, confirm_action

def process_command(command, override_intent=None):
    if override_intent:
        intent = override_intent
    else:
        intent = detect_intent(command)
        
    last_intent = conversation_memory.get_last_intent()
    if intent == "search_web" and last_intent in ["open_youtube", "search_youtube"]:
        intent = "search_youtube"
        print("🧠 Context resolved: Redirecting web search to YouTube.")
        
    print("🧠 Final intent:", intent)
    
    # SECURITY CHECKPOINT
    if not is_intent_allowed(intent):
        print(f"⚠️ SECURITY ALERT: Blocked unauthorized intent '{intent}'.")
        return "I am not authorized to perform that action due to security restrictions."
        
    if requires_confirmation(intent):
        action_name = intent.replace("_", " ")
        if intent == "shutdown": action_name = "shut down the computer"
        if intent == "restart": action_name = "restart the computer"
        if not confirm_action(action_name):
            return "Action cancelled."
            
    conversation_memory.set_last_intent(intent)
    
    # Execution Routing
    if intent in APPLICATION_WHITELIST:
        return open_application(intent)
    elif intent in WEBSITES:
        return open_website(intent)
    elif intent == "search_web":
        return search_web(command)
    elif intent == "search_youtube":
        return search_youtube(command)
    elif intent == "take_screenshot":
        return take_screenshot()
    elif intent == "increase_volume":
        return increase_volume()
    elif intent == "decrease_volume":
        return decrease_volume()
    elif intent == "mute_volume":
        return mute_volume()
    elif intent == "lock_pc":
        return lock_computer()
    elif intent == "sleep_pc":
        return sleep_computer()
    elif intent == "restart":
        return restart_computer()
    elif intent == "shutdown":
        return shutdown_computer()
        
    # Phase 14-17: Productivity & System Info
    elif intent == "set_reminder":
        return set_reminder(command)
    elif intent == "check_weather":
        return check_weather(command)
    elif intent == "send_email":
        return send_email(command)
    elif intent == "system_information":
        return system_information(command)
        
    # Phase 21: File and Folder Control
    elif intent == "open_folder":
        return open_folder(command)
    elif intent == "find_file":
        return find_file(command)
        
    elif intent == "analyze_vision":
        return analyze_vision(command)
    elif intent == "exit":
        return "Goodbye. See you later."
        
    elif intent == "unknown":
        print("🤖 Asking AI Engine...")
        ai_result = process_with_ai(command)
        
        if isinstance(ai_result, str):
            return ai_result
        if "error" in ai_result:
            return ai_result["error"]
        if "intent" in ai_result:
            new_intent = ai_result["intent"]
            print(f"🤖 AI translated command to local intent: {new_intent}")
            if new_intent == "unknown":
                return "I couldn't determine how to do that."
            return process_command(command, override_intent=new_intent)
        if "response" in ai_result:
            return ai_result["response"]
            
        return "I received an invalid response from the AI."
    else:
        return f"I understood your intent to {intent.replace('_', ' ')}, but I haven't been programmed to execute that yet."