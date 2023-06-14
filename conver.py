import sqlite3


fd = open('tablice.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')
con = sqlite3.connect("faks.db")
cur = con.cursor()
for command in sqlCommands:
    con.execute(command)
    con.commit()