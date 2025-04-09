#Esercizio Slicing e F.Indexing
import numpy as np

#creazione array
arr_1d=np.random.randint(10,51, 20)
print(arr_1d)

#estrazione primi 10 con slicing
primi_10=arr_1d[:10] #dall'inizio dell'aray fino all'indice 10
print("primi 10 eleemnti:")
print(primi_10)

#estrazione degli ultimi 5 con slicing
ulitmi_5=arr_1d[-5:] #dagli ultimi 5 fino alla fine dell'array
print("ultimi 5 elementi:")
print(ulitmi_5)

#estrazione elementi dal 5 al 15 (escluso)
da_5_a_15=arr_1d[5:15]
print("elementi dall'indice 5 all'indice 15:")
print(da_5_a_15)

#estrazione di ogni terzo elemento dell'array
ogni_terzo=arr_1d[0:20:3] #dagli inizi dell'array fino alla fine, saltando 2 elementi
print("ogni terzo elemento:")
print(ogni_terzo)

#modifica, tramite slicing, degli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99
arr_1d[5:10]=99
print("array modificato:")
print(arr_1d)

#stampa dell'array originale e di tutti i sottoarray ottenuti tramite slicing
print("riepilogo:")
print("array originale:", arr_1d)
print("primi 10 elementi:", primi_10)
print("ultimi 5 elementi:", ulitmi_5)
print("elementi dall'indice 5 all'indice 15:", da_5_a_15)
print("ogni terzo elemento:", ogni_terzo)
