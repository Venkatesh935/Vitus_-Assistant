import customtkinter as ctk
import threading
from core.state import state
from core.assistant import VitusAssistant

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class VitusGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Vitus AI")
        self.geometry("550x700")
        
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="VITUS AI", font=ctk.CTkFont(size=30, weight="bold"))
        self.title_label.pack(pady=20)
        
        # Status Label
        self.status_label = ctk.CTkLabel(self, text="System Offline", font=ctk.CTkFont(size=18), text_color="gray")
        self.status_label.pack(pady=10)
        
        # Start Button
        self.start_btn = ctk.CTkButton(self, text="START VITUS", command=self.start_assistant, 
                                       font=ctk.CTkFont(size=16, weight="bold"), height=50, fg_color="#006400", hover_color="#004d00")
        self.start_btn.pack(pady=20)
        
        # Log Textbox
        self.log = ctk.CTkTextbox(self, width=500, height=450, font=ctk.CTkFont(size=14))
        self.log.pack(pady=10)
        self.log.configure(state="disabled")
        
        self.assistant_thread = None
        self.after(100, self.process_queue)
        
    def start_assistant(self):
        self.status_label.configure(text="Listening for Wake Word...", text_color="orange")
        self.start_btn.configure(state="disabled", fg_color="gray")
        
        self.assistant = VitusAssistant()
        self.assistant_thread = threading.Thread(target=self.assistant.run, daemon=True)
        self.assistant_thread.start()
        
    def process_queue(self):
        while not state.ui_queue.empty():
            msg = state.ui_queue.get()
            
            self.log.configure(state="normal")
            self.log.insert("end", f"[{msg['type'].upper()}]: {msg['data']}\n")
            self.log.see("end")
            self.log.configure(state="disabled")
            
            if msg['type'] == 'wake_word':
                self.status_label.configure(text="Wake Word Detected! Listening...", text_color="#00ff00")
            elif msg['type'] == 'user_command':
                self.status_label.configure(text="Processing Command...", text_color="#00ffff")
            elif msg['type'] == 'response':
                self.status_label.configure(text="Listening for Wake Word...", text_color="orange")
                
        self.after(100, self.process_queue)

def run_gui():
    app = VitusGUI()
    app.mainloop()
