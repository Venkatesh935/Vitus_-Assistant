import os

files = {
    'gui/app.py': '''import tkinter as tk
import threading
from core.state import state
from core.assistant import VitusAssistant

class VitusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vitus AI Assistant")
        self.root.geometry("500x600")
        
        self.status_label = tk.Label(root, text="System Offline", font=("Helvetica", 14))
        self.status_label.pack(pady=20)
        
        self.start_btn = tk.Button(root, text="Start Vitus", command=self.start_assistant, bg="green", fg="white", font=("Helvetica", 12))
        self.start_btn.pack(pady=10)
        
        self.log = tk.Text(root, height=20, width=55, state=tk.DISABLED)
        self.log.pack(pady=10)
        
        self.assistant_thread = None
        self.root.after(100, self.process_queue)
        
    def start_assistant(self):
        self.status_label.config(text="Listening for Wake Word...")
        self.start_btn.config(state=tk.DISABLED)
        
        self.assistant = VitusAssistant()
        self.assistant_thread = threading.Thread(target=self.assistant.run, daemon=True)
        self.assistant_thread.start()
        
    def process_queue(self):
        while not state.ui_queue.empty():
            msg = state.ui_queue.get()
            
            self.log.config(state=tk.NORMAL)
            self.log.insert(tk.END, f"[{msg['type'].upper()}]: {msg['data']}\\n")
            self.log.see(tk.END)
            self.log.config(state=tk.DISABLED)
            
            if msg['type'] == 'wake_word':
                self.status_label.config(text="Wake Word Detected! Listening...", fg="green")
            elif msg['type'] == 'user_command':
                self.status_label.config(text="Processing Command...", fg="blue")
            elif msg['type'] == 'response':
                self.status_label.config(text="Listening for Wake Word...", fg="black")
                
        self.root.after(100, self.process_queue)

def run_gui():
    root = tk.Tk()
    app = VitusGUI(root)
    root.mainloop()
''',
    'core/assistant.py': '''from voice.speech_to_text import listen
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
''',
    'core/state.py': '''import queue

class GlobalState:
    def __init__(self):
        self.ui_queue = queue.Queue()
        self.is_running = True
        
    def emit(self, event_type, data):
        self.ui_queue.put({"type": event_type, "data": data})

state = GlobalState()
''',
    'core/memory_manager.py': '''class MemoryManager:
    def __init__(self):
        self.last_intent = None
        self.context = []
        
    def get_last_intent(self):
        return self.last_intent
        
    def set_last_intent(self, intent):
        self.last_intent = intent
        
    def add_context(self, text):
        self.context.append(text)
        if len(self.context) > 5:
            self.context.pop(0)

conversation_memory = MemoryManager()
''',
    'ai/ai_engine.py': '''import os
import openai
import json
from core.state import state

def process_with_ai(command):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        return {"error": "AI Engine offline. Please set your OPENAI_API_KEY in the .env file."}
        
    client = openai.OpenAI(api_key=api_key)
    
    system_prompt = """You are Vitus, an advanced AI desktop assistant. 
    Analyze the user's command. If it's a casual conversation, respond warmly.
    If it implies an action you think the system can handle, return ONLY a JSON object with {"intent": "the_intent"}.
    Otherwise, return ONLY a JSON object with {"response": "your conversational response"}."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": command}
            ],
            temperature=0.7
        )
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except:
            return {"response": content}
    except Exception as e:
        return {"error": f"AI Engine error: {e}"}
'''
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
