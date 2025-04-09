#esercizio 2
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine

    def stampa(self):
        print(self.titolo)
        print(self.autore)
        print(self.pagine)
    
    while True:
        titolo=input("inserisci il titolo")
        autore=input("inserisci l'autore")
        pagine=input("inserisci il numero di pagine")

        libro=libro(titolo, autore, pagine)
        libro.stampa()