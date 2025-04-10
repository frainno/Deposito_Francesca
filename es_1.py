import numpy as np

#crea array di 12 num equidistanti tra 0 e 1
arr=np.linspace(0,1,12)
print(arr)

#cambia forma a una matrce 3x4
matrice_1=arr.reshape(3,4)
print(matrice_1)

#genera matrice di num casuali tra 0 e 1 
matrice_2=np.random.rand(3,4)
print(matrice_2)

#somma degli elementi
somma_matrice_1=np.sum(matrice_1)
somma_matrice_2=np.sum(matrice_2)
print(somma_matrice_1)
print(somma_matrice_2)
