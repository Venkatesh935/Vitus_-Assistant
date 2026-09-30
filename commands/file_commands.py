import os
import threading
from core.state import state

# Dynamically map standard Windows directories
USER_HOME = os.path.expanduser("~")
DIRECTORIES = {
    "downloads": os.path.join(USER_HOME, "Downloads"),
    "documents": os.path.join(USER_HOME, "Documents"),
    "desktop": os.path.join(USER_HOME, "Desktop"),
    "pictures": os.path.join(USER_HOME, "Pictures"),
    "music": os.path.join(USER_HOME, "Music"),
    "videos": os.path.join(USER_HOME, "Videos"),
}

def open_folder(command):
    """Opens standard user directories safely."""
    cmd = command.lower()
    for name, path in DIRECTORIES.items():
        if name in cmd:
            if os.path.exists(path):
                print(f"📁 Opening {name.title()}...")
                os.startfile(path)
                return f"Opening your {name} folder."
            else:
                return f"I couldn't find the {name} folder on this system."
    
    # Fallback if no specific folder matched
    os.startfile(USER_HOME)
    return "Opening your home folder."

def _search_thread(query, search_dirs):
    """Runs a recursive search in a background thread to prevent GUI freezing."""
    found_paths = []
    state.emit("system", f"Searching for '{query}'... This may take a moment.")
    
    for s_dir in search_dirs:
        try:
            for root, dirs, files in os.walk(s_dir):
                for file in files:
                    if query in file.lower():
                        found_paths.append(os.path.join(root, file))
                # Break early if we found enough matches to save time
                if len(found_paths) >= 5:
                    break
        except Exception:
            pass
        if len(found_paths) >= 5:
            break
            
    if found_paths:
        first_result = found_paths[0]
        folder_path = os.path.dirname(first_result)
        os.startfile(folder_path)
        state.emit("system", f"Found matches for '{query}'. Opening folder: {folder_path}")
    else:
        state.emit("system", f"Could not find any files matching '{query}'.")

def find_file(command):
    """Strips the command down to the query and dispatches the search thread."""
    print("🔍 Parsing file search request...")
    cmd = command.lower()
    
    prefixes = ["find my ", "find the ", "find ", "locate my ", "search for file ", "where is my "]
    query = cmd
    for p in prefixes:
        if p in cmd:
            query = cmd.split(p, 1)[-1].strip()
            break
            
    if not query:
        return "What file would you like me to find?"
        
    search_dirs = [DIRECTORIES["documents"], DIRECTORIES["desktop"], DIRECTORIES["downloads"]]
    
    # Run the intensive search in a background thread
    threading.Thread(target=_search_thread, args=(query, search_dirs), daemon=True).start()
    
    return f"I am searching your common folders for {query}. I will open the folder when I find it."