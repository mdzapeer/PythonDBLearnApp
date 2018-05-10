import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookt (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def viewDB(self):
        self.cur.execute("SELECT * FROM bookt")
        rows=self.cur.fetchall()
        return rows

    def insertRow(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO bookt VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()

    def searchDB(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM bookt WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def deleteRow(self,id):
        self.cur.execute("DELETE FROM bookt WHERE id=?",(id,))
        self.conn.commit()

    def updateRow(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE bookt SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#insertRow("The Earth","John Smith", 1912, 912354683)
#deleteRow(6)
#print(viewDB())
#print(searchDB(author="John Smith"))
