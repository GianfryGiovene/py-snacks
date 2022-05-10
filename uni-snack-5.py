# Scrivere un programma che, dati i due elenchi di
# numeri sottostanti, crei la matrice dei loro prodotti:
# v1: 1,2,3,4,5
# v2: 6,7,8,9,10
# mat:
# 1*6 1*7 1*8 ...
# 2*6 2*7 2*8 ...
# ...
# ● Completare il programma con una stampa della
# matrice riga per riga:
# [6, 7, 8 ...]
# [12, 14, 16 ...]
# ...

v1 = [1, 2, 3, 4, 5]
v2 = [6, 7, 8, 9, 10]

for i in v1:
    counter = 0
    for k in v2:
        counter += 1
        if counter < len(v2):
            print((i * k), end="")
        else:
            print(i * k)
            counter = 1
