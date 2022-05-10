# Crea due tuple che rappresentano i due elenchi di nomi e cognomi descritti sotto:

# nomi: Numa, Tullo, Anco
# cognomi: Pompilio, Ostilio, Marzio

# Ottenere una lista in cui ogni elemento è un
# dizionario {'nome': nome, 'cognome':
# cognome}, che accoppia nomi e cognomi in
# base all'ordine.

names = ('Numa', 'Tullo', 'Anco')
surnames = ('Pompilio', 'Ostilio', 'Marzio')

userList = []

for name, surname in zip(names, surnames):
    userList.append({'nome': name, 'cognome': surname})

print('ecco la lista', userList)
