vocali = ['a', 'e', 'i', 'o', 'u']

lettera = input()
booleana = False
for vocal in vocali:
    if lettera == vocal:
        booleana = True
if booleana:
    print('è una vocale')
else:
    print('non è una vocale')
