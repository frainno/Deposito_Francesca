import numpy as np

class ArrayProcessor:
    def __init__(self, start=0, end=10, size=50):
        self.start = start
        self.end = end
        self.size = size
        self.array1 = None
        self.array2 = None
        self.array_somma = None

    def genera_array(self):
        self.array1 = np.linspace(self.start, self.end, self.size)
        self.array2 = np.random.random(self.size)
        print("Array linspace (0-10):")
        print(self.array1)
        print("Array random (0-1):")
        print(self.array2)

    def somma_array(self):
        if self.array1 is not None and self.array2 is not None:
            self.array_somma = self.array1 + self.array2
            print("Array somma:")
            print(self.array_somma)
        else:
            print("Gli array non sono stati generati.")

    def calcola_somme(self):
        if self.array_somma is not None:
            somma_totale = np.sum(self.array_somma)
            somma_maggiori_5 = np.sum(self.array_somma[self.array_somma > 5])
            print("Somma totale:", somma_totale)
            print("Somma elementi > 5:", somma_maggiori_5)
        else:
            print("L'array somma non è stato ancora creato.")
