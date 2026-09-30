import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from gui.app import run_gui

if __name__ == "__main__":
    run_gui()
