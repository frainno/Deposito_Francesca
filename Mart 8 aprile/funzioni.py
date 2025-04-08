#semantica delle funzioni
def nome_della_funzione ():
    pass

def saluta(): #funzione di esecuzione
    print("ciao")

saluta()


#funzione con parametri
def somma(x,y,z): 
    risultato=x+y+z
    print(risultato)

somma(1,2,2)
somma(3,4,5)

def saluta_con_parametro(nome):
    print("ciao", nome)

saluta_con_parametro("erica")


#funzioni di ritorno
def riporta_dato(x):
   risultato=x*x
   return risultato

numero=riporta_dato(3)
print(riporta_dato(3))

somma(riporta_dato(3), riporta_dato(3), riporta_dato(3))

if riporta_dato(3)>10:
    pass
else:
    pass


#funzione di ritorno con input interno
def riporta_dato_senza_parametri():
    x=int(input("dammi un numero da elevare a potenza"))
    return x*x


#funzione con parametri standard
def funzione_standard(x=1):
    return x+x

print(funzione_standard())
