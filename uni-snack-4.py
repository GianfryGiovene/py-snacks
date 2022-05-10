# Scrivere un programma che legga un intero n da tastiera
# e stampi a schermo:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ...
# E così via fino a n.
# ● Per stampare senza andare a capo, aggiungere una
# virgola in fondo alla riga con l'istruzione print:
# print 'foo',
# ● Per andare a capo, dare l'istruzione print senza
# argomenti:
# print


numero = int(input('Inserire un numero intero: '))
3
for i in range(numero):
    for k in range(i+1):
        if k+1 == i+1:
            print(k+1)
        else:
            print(k+1, end=" "),
