#primo esercizio
nome=input("inserisci il primo nome per essere identificato")
if nome=="Francesca":

    nome=input("ok, ora inserisci un secondo nome")
    if nome=="Alessia":

        nome=input("perfetto, inserisci l'ultimo nome")
        if nome=="Sara":
            print("Identificazione completata")

        else:
            print("Incompresione nel secondo livello")


    else:
        print("incomprensione nell'ultimo livello")

else:
    print("Identificazione negata al primo livello")


#secondo esercizio
nomi=["Davide", "Angelica", "Angelo"]

scelta=input("scegli cosa vuoi fare")

if scelta.lower()=="e":
    print(nomi)
    scelta==input("scegli quale vuoi eliminare")
    nomi.remove(scelta)
    print(nomi)
elif scelta.lower()=="a":
    scelta=input("scegli cosa vuoi aggiungere")
    nomi.append(scelta)
    print(nomi)
elif scelta.lower()=="m":
    print(nomi)
    scelta=int(input("scegli quale posizione vuoi modificare da 0 a 2"))
    scelta2=input("scegli quale vuoi aggiungere")
    nomi[scelta]=scelta2
    print(nomi)
else:
    print("comando sbagliato")


#terzo esercizio
#creazione variabili
nome=""
password=""
id=0
x=True

#condizioni

#registrazione
if x:
    nome=input("inserisci il tuo nickname")
    password=input("inserisci la tua password")
    id +=1

#login
if nome== "":
    print("non hai valorizzato")
else:
    nome_inserito=input("inserisci il tuo nickname")
    password_inserito=input("inserisci la tua password")             
if nome_inserito==nome and password_inserito==password:
    print("sei loggato")
