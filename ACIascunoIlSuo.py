# Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

listString = ['banana', 'pero']
listInt = []

for word in listString:
    listInt.append(len(word))

print(listInt)
