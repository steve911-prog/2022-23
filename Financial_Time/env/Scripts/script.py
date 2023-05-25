import sqlite3 as sql #Added in Python DB, used for small projects, needs no DB-server.

conn = sql.connect("golden-eye.db")   #create & connect new file

cur = conn.cursor()   #object which reads DB

cur.execute("SELECT * FROM xrates")   #We send an SQL-request to cursor
# * means "all rows from db"

rows = cur.fetchall()
#result of sql-request

for row in rows:
    print(row)

conn.close()
#24:00




































