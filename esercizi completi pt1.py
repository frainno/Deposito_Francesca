#esercizio 1
numero=int(input("inserisci un numero:"))

#utilizzo la struttura condizionale if per verificare se il numero è pari o dispari
if numero % 2==0: #se il resto della divisione del numero per 2 è 0, il numero è pari 
    print("il numero è pari")
else: #altrimenti il numero è dispari
    print("il numero è dispari")


#esercizio 2
while True: #cilco che si ripete all'infinito 
    n=int(input("inserisci un numero intero positivo"))

    if n<0:
        print("il numero inserito non è positivo, riprova")
    else:
        for i in range(n, -1,-1): #se il numero è positivo utilizza la funzione range per ottenere una sequenza di numeri da n a 0, decrementando di 1, il ciclo for stampa ogni numero della sequenza
            print(i)


#esercizio 3
numeri=[]

while True:
    numero=input("inserisci un numero")

    numeri.append(int(numero))

for numero in numeri:
    print