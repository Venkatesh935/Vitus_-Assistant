import re

with open('core/command_processor.py', 'r') as f:
    content = f.read()

if 'analyze_vision' not in content:
    content = content.replace('from commands.file_commands import open_folder, find_file', 'from commands.file_commands import open_folder, find_file\nfrom commands.vision_commands import analyze_vision')
    
    # insert before elif intent == "exit"
    content = content.replace('    elif intent == "exit":', '    elif intent == "analyze_vision":\n        return analyze_vision(command)\n    elif intent == "exit":')
    
    with open('core/command_processor.py', 'w', encoding='utf-8') as f:
        f.write(content)
