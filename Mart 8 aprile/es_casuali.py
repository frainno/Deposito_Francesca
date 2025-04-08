#esercizio base: indovina il numero
import random

def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    
    while True:
        tentativo = input("Indovina il numero (o digita 'esci' per terminare): ")
        if tentativo.lower() == 'esci':
            print("Hai deciso di uscire. Il numero era:", numero_da_indovinare)
            break

        tentativo = int(tentativo)

        if tentativo == numero_da_indovinare:
            print("Bravo! Hai indovinato il numero!")
            break
        elif tentativo < numero_da_indovinare:
            print("Troppo basso!")
        else:
            print("Troppo alto!")

#segui la funzione
indovina_il_numero()


#esercizio avanzato: sequenza di fibonacci fino a N
def fibonacci_fino_a(n): #crea una funzione che prende un numero n
    if n<0:
        print("Inserisci un numero positivo.")
        return []

    sequenza=[]
    a, b=0, 1 #a parte da 0, b da 1

#aggiorna: a diventa il valore di b e b diventa a+b
    while a<=n:
        sequenza.append(a) #l'ho usato per aggiungere un elemento alla fine della lista (fibonacci)
        a, b=b, a+b
    return sequenza #restituisco il risultato

numero=int(input("Inserisci un numero N:")) #Chiede all'utente un numero

risultato=fibonacci_fino_a(numero) #Calcola la sequenza

print("Sequenza di Fibonacci fino a", numero, ":", risultato) #stampa risultato
