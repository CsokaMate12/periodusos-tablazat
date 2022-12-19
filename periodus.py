import sqlite3

f = open("periódus.txt", "r", encoding = "UTF-8")
data = []
for sor in f:
    data.append(sor.strip().split(","))
data.remove(data[0])
f.close()



con = sqlite3.connect("periodusrendszer.db")

cur = con.cursor()

cur.execute("CREATE TABLE periodic(atomicnumber, element, symbol, atomicmass)")

cur.executemany("INSERT INTO periodic VALUES(?, ?, ?, ?)", data)

con.commit()
