import sqlite3
DB_NAME = "railways.db"

def db_init():
	conn = sqlite3.connect(DB_NAME)
	conn.execute("""CREATE TABLE clients(
		client_id INTEGER PRIMARY KEY,
		username TEXT,
		password TEXT,
		email TEXT
	)""")
	conn.commit()

def db_check():
	conn = sqlite3.connect(DB_NAME)
	cur = conn.cursor()
	for i in cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"):
		print(i)

from os.path import exists
if not exists(DB_NAME):
	db_init()
db_check()