import sqlite3

con = sqlite3.connect("faks.db")
cur = con.cursor()

query = """ UPDATE blagajna
SET ukupna_zarada='10'
WHERE id_racuna=1;
                 """
cur.execute(query)
con.commit()

