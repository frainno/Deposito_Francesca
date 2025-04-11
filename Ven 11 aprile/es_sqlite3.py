import sqlite3

#1.creare db scuola.db
conn=sqlite3.connect('scuola.db')
cursor=conn.cursor()

#2.creare la tabella studenti
cursor.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')
conn.commit()

#inserire gli studenti tramite menu
def inserisci_studenti():
    nome=input("Inserisci il nome dello studente: ")
    cursor.execute("INSERT INTO studenti (nome) VALUES (?)", (nome,))
    conn.commit()

#leggere e stampare tutti i nomi dalla tabella
def leggi_studenti():
    cursor.execute("SELECT nome FROM studenti")
    studenti=cursor.fetchall()
    for studente in studenti:
        print(studente[0])

#creazione menu
def menu():
    while True:
        print("Menu")
        print("1.Inserisci nome studente")
        print("2.Visualizza tutti gli studenti")
        print("3.Esci")
        scelta=input("Scegli un'opzione (1-3):")

        if scelta=='1':
            inserisci_studenti()
        elif scelta=='2':
            leggi_studenti()
        elif scelta=='3':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")


#lettura e stampa
if __name__=="__main__":
    menu()