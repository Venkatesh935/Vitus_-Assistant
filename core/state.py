import queue

class GlobalState:
    def __init__(self):
        self.ui_queue = queue.Queue()
        self.is_running = True
        
    def emit(self, event_type, data):
        self.ui_queue.put({"type": event_type, "data": data})

state = GlobalState()
