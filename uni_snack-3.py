# Scrivere un programma che stampi la
# lunghezza delle stringhe fornite dall'utente,
# finchè l'utente non inserisce la stringa
# 'exit'

word = ''
record = 0

while word != 'exit':
    word = input('Inserisci una stringa: ')
    for i, letter in enumerate(word):

        record = i+1

    print(record)
print('sei uscito')

# OR

while True:
    line = input('Inserisci una stringa-2: ')
    if line == 'exit':
        break
    print(len(line))
