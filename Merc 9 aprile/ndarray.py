import numpy as np

#creazione di un array
arr = np.array([1, 2, 3, 4, 5])

#utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) #output:(5,)
print("Dimensioni dell'array:", arr.ndim) #output:1
print("Tipo di dati:", arr.dtype) #output:int64(varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) #output:5
print("Somma degli elementi:", arr.sum()) #output:15
print("Media degli elementi:", arr.mean()) #output:3.0
print("Valore massimo:", arr.max()) #output:5
print("Indice del valore massimo:", arr.argmax()) #output:4

#esempio di reshape
arr=np.arange(6)
reshaped_arr=arr.reshape((2, 3))
print(reshaped_arr) #Output:[[0 1 2] [3 4 5]]