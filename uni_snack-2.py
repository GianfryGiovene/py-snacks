# Data la stringa 'abcdefghi', scrivere
# un programma che analizzi la stringa e
# stampi a video:
# Lettera 1: a
# Lettera 2: b
# ...
# E così via.
# ● Modificare poi il programma in modo da
# leggere la stringa da tastiera.

stringa = input('Inserisci una stringa: ')
cont = 1
for i in stringa:
    print('Lettera ' + str(cont) + ': ' + i)
    cont += 1

# OR

for i, letter in enumerate(stringa):
    print('Lettera ' + str(i) + ': ' + letter)
