import os
from pathlib import Path
from tinydb import TinyDB


DATA_DIR = os.path.join(Path(__file__).parent.parent.parent, "data")
DB_PATH = os.path.join(DATA_DIR, "books.json")
DB = TinyDB(DB_PATH)
