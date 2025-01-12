from openai import OpenAI
import os

class GPTLoader:
    def __init__(self, api_key):
        self.system_rule = self.load_system_rule()
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        
    def load_system_rule(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))    
        with open(os.path.join(current_dir, "systemRule.txt"),'r', encoding='utf-8') as f:
            return f.read()

    def run_gpt(self,input):
        completion = self.client.chat.completions.create(
            model= self.model,
            messages=[
                {"role": "system", "content": self.system_rule},
                {
                    "role": "user",
                    "content": str(input)
                }
            ]
        )
        return completion.choices[0].message.content
