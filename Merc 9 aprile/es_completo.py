#Es1: ndarray, dtype, shape, arange
import numpy as np

#creazione di un array
arr=np.arange(10,50) #utilizzo questa funzione per creare un array di num da 10 a 49
print("Array iniziale:", arr)

#verifico il tipo di dato dell'array e cambio risultato
print("Tipo di dati:", arr.dtype)
arr=np.arange(10,50, dtype=np.float64) #cambio il tipo di dato
print(arr)

#stampo forma dell'arrey
print("Forma dell'array:", arr.shape)