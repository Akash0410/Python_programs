import sqlite3
mydb = sqlite3.connect("akash.db")
dbcur = mydb.cursor()
dbcur.execute('''CREATE TABLE akash(
    ROLL INTEGER,
    NAME TEXT);''')
mydb.commit()
mydb.close()