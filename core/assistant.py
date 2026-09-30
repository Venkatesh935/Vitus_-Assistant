from voice.speech_to_text import listen
from voice.text_to_speech import speak
from core.command_processor import process_command
from core.state import state

class VitusAssistant:
    def run(self):
        state.emit("system", "Vitus AI initialized and ready.")
        speak("Hello, I am Vitus. I am ready to help.")
        
        while state.is_running:
            state.emit("system", "Waiting for command...")
            command = listen()
            
            if not command:
                continue
                
            command = command.lower().strip()
            state.emit("user_command", command)
            
            if "exit" in command or "quit" in command or "stop vitus" in command:
                state.emit("response", "Goodbye.")
                speak("Goodbye. See you later.")
                break
                
            response = process_command(command)
            state.emit("response", response)
            speak(response)
