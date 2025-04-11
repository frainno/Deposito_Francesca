import sqlite3
import random

class Libreria:
    def __init__(self, nome_db="libreria.db"):
        self.conn=sqlite3.connect(nome_db)
        self.cur=self.conn.cursor()

#creare tabella libri
    def crea_tabella(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS libri (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titolo TEXT,
                autore TEXT
             )
        """)
        self.conn.commit()

#inserimento di 3 libri
    def inserisci_libri(self,libri):
        self.cur.executemany('''
            INSERT INTO libri (titolo, autore) VALUES (?, ?)",
        ''', libri)
        self.conn.commit()

#recupero e stampa dei libri
        self.cur.execute("SELECT id, titolo, autore FROM libri")
        libri=self.cur.fetchall()
        for libro in libri:
            print(f"ID: {libro[0]}, Titolo: {libro[1]}, Autore: {libro[2]}")

#aggiunta della colonna vendite
    def aggiungi_colonna_vendite(self):
        self.cur.execute("ALTER TABLE libri ADD COLUMN VENDITE INTEGER")
        self.conn.commit()

#recupero e stampa di tutti i libri
        self.cur.execute("SELECT FROM libri")
        ids=[r[0] for r in self.cur.fetchall()]
        for libro_id in ids:
            vendite_random=random.randint(10, 1000)
            self.cur.execute('UPDATE libri SET vendite = ? WHERE id = ?', (vendite_random, libro_id))
        
    def chiudi(self):
        self.conn.close
