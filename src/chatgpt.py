from dotenv import load_dotenv
import os
from openai import OpenAI

# 환경 변수에서 API 키 로드
load_dotenv()
API_KEY = os.environ.get('GPT_KEY')

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)