# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro.
# In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!

myWord = input()

len = 0

for char in myWord:
    len += 1

print(len)
