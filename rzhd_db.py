import sqlite3
DB_NAME = "railways.db"

def db_init():
	pass
	#TODO2: add all tables

def db_check():
	pass
	#TODO1: print all tables

from os.path import exists
if not exists(DB_NAME):
	db_init()
db_check()