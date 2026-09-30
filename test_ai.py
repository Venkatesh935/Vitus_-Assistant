import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f'Key loaded: {api_key[:5]}...')

try:
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': 'hello'}],
        max_tokens=5
    )
    print('Response:', response.choices[0].message.content)
except Exception as e:
    print('ERROR:', e)
