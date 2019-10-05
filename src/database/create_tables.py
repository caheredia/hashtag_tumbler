import sqlite3
from src.constants import DATABASE_FILE

conn = sqlite3.connect(DATABASE_FILE)

c = conn.cursor()

c.execute(
    """CREATE TABLE hashtags (
   themes text,
   groups text,
   hashtags text
   )"""
)

conn.commit()
conn.close()
