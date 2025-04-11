import sqlite3
conn=sqlite3.connect('libri.db')
cur=conn.cursor()

#metodo execute()
cur.execute('''
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY,
        titolo TEXT
    )
''')
conn.commit()

#Inserimento sicuro con parametro
cur.execute("INSERT INTO libri (titolo) VALUES (?)", ("LOTR",))

conn.commit()

#metodo executemany()
import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()

libri= [("Harry Potter",), ("1984",), ("Il Piccolo Principe",)]
cur.executemany("INSERT INTO libri (titolo) VALUES (?)", libri)

conn.commit()

#metodo commit
import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("INSERT INTO libri (titolo) VALUES (?)", ("Il Nome della Rosa",))
conn.commit()