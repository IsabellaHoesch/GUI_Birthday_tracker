import sqlite3



conn=sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE test(name TEXT, vorname TEXT)''')