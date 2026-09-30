class MemoryManager:
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
