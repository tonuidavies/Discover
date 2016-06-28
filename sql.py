import sqlite3

with sqlite3.connect("sample.db") as connection:
	C = connection.cursor()
	#c.excute("""DROP TABLE posts""")
	c.excute("""CREATE TABLE posts(title TEXT, description TEXT)""")
	c.excute('INSERT INTO posts VALUES("well", "I\'m good.")')
	c.excute('INSERT INTO posts VALUES("well", "I\'m well.")')
