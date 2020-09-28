import sqlite3

conn = sqlite3.connect("birthday.db")

c = conn.cursor()

# c.execute("""CREATE TABLE birthdays (
#             firstname text,
#             lastname integer,
#             date text )
#     """)

# c.execute("INSERT INTO birthdays VALUES ({}, {}, {})").format({}, {}, {})
# conn.commit()
c.execute("SELECT * FROM birthdays WHERE lastname = 'Hoesch'")
print(c.fetchone())

conn.commit()
conn.close()