from tinydb import TinyDB, Query
from app.config import DB_PATH

db_instance = TinyDB(DB_PATH)
