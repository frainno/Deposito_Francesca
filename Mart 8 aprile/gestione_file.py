file=open("esempio_testo.txt", "r")

tutte_le_righe=file.read()
riga=file.readline()

print(tutte_le_righe)

file.close()

file=open("esempio_testo.txt", "w")

file.write("sto sostituendo il testo")
file.close()