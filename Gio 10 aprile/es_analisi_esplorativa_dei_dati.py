#Analisi esplorativa dei dati
import pandas as pd
import numpy as np

#Caricare i dati in un DataFrame autogenerandoli casualmente
np.random.seed(0)
dati = {
    "Nome": [f"Persona {i}" for i in range(1, 101)],
    "Età": np.random.randint(0, 100, 100),
    "Città": np.random.choice(["Roma", "Milano", "Napoli", "Torino"], 100),
    "Salario": np.random.randint(20000, 100000, 100)
}
df = pd.DataFrame(dati)

#Visualizzare le prime e le ultime cinque righe del DataFrame
print("Prime 5 righe:")
print(df[0:5])
print("Ultime 5 righe:")
print(df[-5:])

#Visualizzare il tipo di dati di ciascuna colonna
print("Tipo di dati di ciascuna colonna:")
print(df.dtypes)

#Calcolare statistiche descrittive di base per le colonne numeriche
print("Statistiche descrittive per le colonne numeriche:")
print(df[["Età", "Salario"]].describe())

#Identificare e rimuovere eventuali duplicati
df = df.drop_duplicates()

#Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna
df["Età"]=df["Età"].replace(np.nan,df["Età"].median())
df["Salario"]=df["Salario"].replace(np.nan,df["Salario"].median())

#Aggiungere una nuova colonna chiamata "Categoria Età"
def categorizza_eta(eta):
    if eta < 19:
        return 'Giovane'
    elif eta <= 65:
        return 'Adulto'
    else:
        return 'Senior'
df['Categoria Età']=df['Età'].apply(categorizza_eta)

#Salvare il DataFrame pulito in un nuovo file CSV
df.to_csv("dati_puliti.csv", index=False)