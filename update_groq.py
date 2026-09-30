with open('ai/ai_engine.py', 'r') as f:
    content = f.read()

content = content.replace('llama3-8b-8192', 'llama-3.1-8b-instant')

with open('ai/ai_engine.py', 'w') as f:
    f.write(content)
