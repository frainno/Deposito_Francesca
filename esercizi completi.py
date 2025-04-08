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
numeri=[1,2,3,4,5] #lista numeri
numeripotenze=[] #lista numeri

for i in numeri: #calcolo del quadrato per ogni numero della lista
    print(i**2)
    numeripotenze.append(i**2) #aggiunta del quadrato alla lista

print(numeripotenze)


#esercizio 4
numeri=[]

while True:
    num=input("inserisci un numero (o 'fine' per terminare):")
    
    if num.lower()=='fine':
        break
    
    numeri.append(int(num))

if len(numeri)==0:
    print("lista vuota")
else:
    max_num=numeri[0] 
    for num in numeri: #ciclo for per trovare il numero max nella lista
        if num>max_num:
            max_num=num
    
    count=0
    i=0
    while i<len(numeri): #ciclo while per contare gli elementi nella lista
        count+=1
        i+=1

#stampa il num max e il num di elementi
    print("il numero massimo è:", max_num)
    print("il numero di elementi è:", count)
