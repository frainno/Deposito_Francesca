class Automobile: #dichiaro la classe
    numero_di_ruote=4 #attributo di classe
    def __init__(self, marca, modello): #metodo costruttore
        self.marca=marca #attributo di istanza
        self.modello=modello #attributo di istanza
    def stampa_info(self): #metodo di istanza
        print("l'automobile è una", self.marca, self.modello)


#creazione di un oggetto
class Famiglia:
    def __init__(self, cognome, membri, citta):
        self.cognome = cognome
        self.membri = membri
        self.citta = citta
    def stampa_info(self):
        print("Famiglia", self.cognome)
        print("Numero di membri", self.membri)
        print("Città", self.citta)
famiglia_rossi = Famiglia("Rossi", 4, "Milano")
famiglia_rossi.stampa_info()


#metodostatico
class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return
risultato=Calcolatrice.somma(5,3) #uso del metodo statico senza creare un'istanza
print(risultato) #output


#metodo decorato
class Contatore:
    numero_istanze = 0 #attributo di classe
    def __init__(self): Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
#Creazione di alcune istanze 
c1 = Contatore()
c2 = Contatore()
Contatore.mostra_numero_istanze() #output: sono state create 2 istanze