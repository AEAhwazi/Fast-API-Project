import sqlite3

DBNAME = 'MyDatabase.db'

conn = sqlite3.connect(DBNAME)
cursor = conn.cursor()
query = '''
        CREATE TABLE IF NOT EXISTS movie
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         movie_id INTEGER,
         title TEXT,
         poster TEXT,
         year TEXT,
         runtime TEXT,
         country TEXT,
         imdb_rating TEXT,
         genres TEXT)'''

cursor.execute(query)
conn.commit()
conn.close()
