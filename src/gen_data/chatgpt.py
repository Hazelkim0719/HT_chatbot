from openai import OpenAI

class GPTLoader:
    def __init__(self, api_key):
        self.system_rule = self.load_system_rule()
        self.client = OpenAI(api_key=api_key)

    def load_system_rule(self):
        with open('./systemRule.txt','r', encoding='utf-8') as f:
            return f.read()

    def run_gpt(self,input):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_rule},
                {
                    "role": "user",
                    "content": str(input)
                }
            ]
        )
        return completion.choices[0].message.content
