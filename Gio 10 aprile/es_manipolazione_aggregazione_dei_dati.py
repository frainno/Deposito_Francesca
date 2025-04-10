import pandas as pd

#Caricare i dati in un DataFrame
dati={
    "Prodotto":["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Quantità":[10, 20, 30, 15, 25, 35, 20, 30, 40],
    "Prezzo Unitario":[100, 200, 300, 150, 250, 350, 200, 300, 400],
    "Città":["Roma", "Milano", "Napoli", "Roma", "Milano", "Napoli", "Roma", "Milano", "Napoli"]
}
df=pd.DataFrame(dati)

#Aggiungere una colonna "Totale Vendite"
df["Totale Vendite"]=df["Quantità"]*df["Prezzo Unitario"]

#Raggruppare i dati per Prodotto e calcolare il totale delle vendite
vendite_per_prodotto=df.groupby("Prodotto")["Totale Vendite"].sum()
print(vendite_per_prodotto)

#Trovare il prodotto più venduto in termini di Quantità
prodotto_piu_venduto=df.groupby("Prodotto")["Quantità"].max()
print(prodotto_piu_venduto)

#Identificare la città con il maggior volume di vendite totali
citta_con_piu_vendite=df.groupby("Città")["Totale Vendite"].max()
print(citta_con_piu_vendite)

#Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore
vendite_superiori=df[df["Totale Vendite"]>100]
print(vendite_superiori)

#Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente
df_ordinato=df.sort_values("Totale Vendite", ascending=False)
print(df_ordinato)

#Visualizzare il numero di vendite per ogni città
num_vendite_per_citta=df.groupby("Città")["Prodotto"].count()
print(num_vendite_per_citta)