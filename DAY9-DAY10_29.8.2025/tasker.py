"""
👉 Task Manager (OOP + JSON)
This project is a simple command-line Task Manager application.

Features:
- Add new tasks with a title and optional description
- View all saved tasks
- Remove tasks by their ID
- Persistent storage using a JSON file (tasks are saved between runs)

Learning Goals:
- Practice Object-Oriented Programming (OOP) with Python classes
- Understand how JSON works for structured data storage
- Learn how to separate logic into multiple files (modular design)
- Build a real-world CLI tool that goes beyond text file storage """


"========================================================================="


"""so at first we will import the needed libraries : chore ; 
we have to set up the paths and imports that the json file needs . 
 and we are importing datetime for the timestamps ; """


from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

#tasks.json file will be stored next to this very .py file (next to this file)
STORAGE_FILE = Path(__file__).with_name("tasks.json")

