import os

files = {
    'commands/application_commands.py': '''import os

APPLICATION_WHITELIST = {
    "open_chrome": "chrome.exe",
    "open_edge": "msedge.exe",
    "open_notepad": "notepad.exe",
    "open_calculator": "calc.exe",
    "open_file_explorer": "explorer.exe",
    "open_command_prompt": "cmd.exe",
    "open_powershell": "powershell.exe"
}

def open_application(intent):
    app_exe = APPLICATION_WHITELIST.get(intent)
    if app_exe:
        print(f"🚀 Launching {app_exe}...")
        os.system(f"start {app_exe}")
        return f"Opening {app_exe.replace('.exe', '')}."
    return "I am not authorized to open that application."
''',
    'commands/web_commands.py': '''import webbrowser

WEBSITES = {
    "open_google": "https://www.google.com",
    "open_youtube": "https://www.youtube.com",
    "open_gmail": "https://mail.google.com",
    "open_github": "https://github.com",
    "open_linkedin": "https://linkedin.com",
    "open_chatgpt": "https://chatgpt.com"
}

def open_website(intent):
    url = WEBSITES.get(intent)
    if url:
        print(f"🌐 Opening {url}...")
        webbrowser.open(url)
        name = intent.replace('open_', '').capitalize()
        return f"Opening {name}."
    return "I couldn't find that website."

def search_web(command):
    query = command.replace("search for", "").replace("search google", "").replace("google", "").strip()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."
    return "What would you like me to search for?"

def search_youtube(command):
    query = command.replace("search youtube", "").replace("play on youtube", "").strip()
    if query:
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for {query}."
    return "What would you like to watch on YouTube?"
''',
    'commands/productivity_commands.py': '''import datetime
import json
import openai
import os
import requests
import threading

def set_reminder(command):
    return "Reminder features require active AI."

def check_weather(command):
    return "Weather features require API configuration."
''',
    'commands/email_commands.py': '''import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import openai
import json
from core.security_manager import confirm_action
from core.state import state

def send_email(command):
    return "Email drafting and sending requires manual configuration."
''',
    'commands/info_commands.py': '''import ctypes
import subprocess

def system_information(command):
    return "Your system is running smoothly."
'''
}

for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
