import sqlite3  #Importa il modulo per lavorare con SQLite

#Connessione (crea un file 'miodatabase.db' se non esiste)
conn = sqlite3.connect('miodatabase.db')

#Cursore per eseguire comandi SQL
cur = conn.cursor()

#Creazione di una tabella (se non esiste)
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

#Inserimento di un dato
cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mirko",))

#Salvataggio delle modifiche
conn.commit()

#Query per leggere i dati
cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()


#Stampa dei risultati
for riga in righe:
    print(riga)


#creazione di una tabella
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')


#inserimento dati
cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mario",))
conn.commit() # Importante: salva le modifiche


#lettura dati
cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()
for r in righe:
    print(r)


#modifca dati
cur.execute("UPDATE utenti SET nome = ? WHERE id = ?", ("Luigi", 1))
conn.commit()


#eliminazione dati
cur.execute("DELETE FROM utenti WHERE id = ?", (1,))
conn.commit()