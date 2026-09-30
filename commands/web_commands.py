import webbrowser

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
