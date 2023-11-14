import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DB_PATH = f'{BASE_DIR}/database/db.json'
