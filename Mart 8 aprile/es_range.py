#eserczio 1

while True: #verificare se la condizione è vera
    numero=int(input("Inserisci un numero per iniziare il conto alla rovescia")) #conto alla rovescia a partire da quel numero fino a 0
     
    for i in range(numero, -1, -1): #numeri da 20 a 1
        print(i)

    ripeti=input("Vuoi ripetere?").lower()
    if ripeti=="sì":
        continue
    else:
        print("Fine")
        break

#esercizio 2

numeri_pari=[] #lista per salvare i numeri pari trovati

while len(numeri_pari)<5: #ciclo finchè non si trovano 5 numeri pari
    numero=int(input("inserisci un numero:"))

    if numero % 2 == 0:
     print("il numero è pari")
     numeri_pari.append(numero)
    else:
     print("il numero non è pari")

print("hai stampato 5 numeri pari:", numeri_pari) #termina stampando i numeri pari raccolti