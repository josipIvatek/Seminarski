import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ 

   SELECT ukupna_zarada FROM blagajna 
;

"""

data = cur.execute(query).fetchall()
uzarada = data + svirke[len(svirke) - 1].cijena


for d in data:
    print(d)