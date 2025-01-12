from datetime import datetime

class Logging():
    def __init__(self):
        pass
    def log(self, text):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{formatted_time}] {text}")