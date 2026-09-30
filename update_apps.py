with open('commands/application_commands.py', 'r') as f:
    content = f.read()

content = content.replace('    "open_powershell": "powershell.exe"\n}', '    "open_powershell": "powershell.exe",\n    "open_vscode": "code"\n}')

with open('commands/application_commands.py', 'w') as f:
    f.write(content)
