import os
import openai
import json
from core.state import state

def process_with_ai(command):
    # We are now using a 100% FREE API key from Groq!
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {"error": "AI Engine offline. Please set your GROQ_API_KEY in the .env file."}
        
    # By changing the base_url, we trick the OpenAI library into talking to Groq's free servers!
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    system_prompt = """You are Vitus, an advanced AI desktop assistant. 
    Analyze the user's command. If it's a casual conversation, respond warmly.
    If it implies an action you think the system can handle, return ONLY a JSON object with {\"intent\": \"the_intent\"}.
    Otherwise, return ONLY a JSON object with {\"response\": \"your conversational response\"}."""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", # Extremely fast and completely free Meta Llama model
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
