import re

with open('core/intent_manager.py', 'r') as f:
    content = f.read()

if 'analyze_vision' not in content:
    content = content.replace('    "exit":', '    "analyze_vision": [r"\\\\bwhat do you see\\\\b", r"\\\\bwhat am i holding\\\\b", r"\\\\blook at this\\\\b", r"\\\\bwhat is this\\\\b"],\n    "exit":')
    with open('core/intent_manager.py', 'w') as f:
        f.write(content)
