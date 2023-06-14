import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ 

SELECT * FROM clan;

"""

data = cur.execute(query).fetchall()

for d in data:
    print(d)
