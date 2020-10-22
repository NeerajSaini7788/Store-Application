import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text , author text , year integer , isbn integer)")
    conn.commit()
    conn.close()



def insert(title, author , year ,isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL , ?,?,?,?)" , (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from book")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(title = "",author ="",year ="",isbn = ""):  ## python will use these argument values incase if not recive any values during the function call
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year,isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows




def delete(id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book  WHERE id = ?" , (id,))
    conn.commit()
    conn.close()



def update(id , title, author,year,isbn):  ## python will use these argument values incase if not recive any values during the function call
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ? , isbn = ? WHERE id = ?" , (title,author,year,isbn,id))
    rows = cursor.fetchall()
    conn.commit()
    conn.close()


connect()
#insert("Skull Candy" , "Mp3" , 2015 ,98950)
insert("Apple" , "Electronics" , 2018 ,9125)
print(view())
update(2 , "New Apple" , "New Electronics" , 2012 , 45)
print(view())
