#eserczio 1

while True: #verificare se la condizione è vera
     numero=int(input("Inserisci un numero per iniziare il conto alla rovescia")) #conto alla rovescia a partire da quel numero fino a 0
     
    for i in range(numero, 20, 0): #numeri da 20 a 1
        print(i)

    ripeti=input("Vuoi ripetere?").lower()
    if ripeti=="sì":
        continue
    else:
    print("Fine")
    break 
