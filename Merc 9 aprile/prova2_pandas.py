import pandas as pd

#dati da scrivere nel csv
dati=[
    {"nome": "francesca", "cognome": "innocente", "età": "24", "città": "milano"},
    {"nome": "erica", "cognome": "mia", "età": "2", "città": "roma"},
    {"nome": "luca", "cognome": "monso", "età": "30", "città": "genova"},
    {"nome": "zia", "cognome": "zio", "età": "90", "città": "torino"},
]

#creazione dataframe
df = pd.DataFrame(dati)

#salvataggio in file csv
file_path = 'persone.csv'
df.to_csv(file_path, index=False)

df_letto = pd.read_csv(file_path)
print(df_letto.head())