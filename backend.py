import sqlite3

def createTable():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookt (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def viewDB():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookt")
    rows=cur.fetchall()
    conn.close()
    return rows

def insertRow(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookt VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def searchDB(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookt WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def deleteRow(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookt WHERE id=?",(id,))
    conn.commit()
    conn.close()

def updateRow(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookt SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

createTable()
#insertRow("The Earth","John Smith", 1912, 912354683)
#deleteRow(6)
print(viewDB())
print(searchDB(author="John Smith"))
