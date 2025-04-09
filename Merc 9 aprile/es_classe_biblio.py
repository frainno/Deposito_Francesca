#esercizio crea classe biblioteca
class Libro: #definiamo la classe
    def __init__(self, titolo, autore, pagine): #metodo costruttore che prende i parametri
        self.titolo=titolo #metodo costruttore assegna i valori
        self.autore=autore
        self.pagine=pagine

class Biblioteca: #definiamo la classe
    def __init__(self): #metodo costruttore inizializza un attributo chiamato libri
        self.libri = []

    def aggiungi_libro(self):
        titolo=input("Inserisci il titolo del libro:")
        autore=input("Inserisci l'autore del libro:")
        pagine=int(input("Inserisci il numero di pagine del libro:"))
        libro=Libro(titolo, autore, pagine) 
        self.libri.append(libro)

    def stampa_libri(self):
        for i, libro in enumerate(self.libri, start=1): #parti dalla pagina 1 per stampare
            print(f"Libro{i}: {libro.titolo} di {libro.autore}, {libro.pagine} pagine")

#menù per la gestione del libro
biblioteca=Biblioteca()
while True:
    print("Aggiungi libro")
    print("Stampa libri")
    print("Esci")
    scelta = input("Inserisci la tua scelta:")
    if scelta=="1":
        biblioteca.aggiungi_libro()
    elif scelta=="2":
        biblioteca.stampa_libri()
    elif scelta=="3":
        break
    else:
        print("Scelta non valida. Riprova.")