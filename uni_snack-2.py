# Creare un dizionario che contenga come
# chiavi 'nome' e 'cognome', inserendo i propri
# dati come valori
# ● Aggiungere 'matricola'
# ● Aggiungere 'esami', provando ad immaginare
# che tipi di dato usare per rappresentare sia
# nome che voto degli esami

import random

studente = {'nome': input('inserisci nome: '),
            'cognome': input('inserisci cognome: ')}

print(studente)

numberMatricola = ''

for n in 6:
    n = str(random.random(0, 9))
    numberMatricola += n


matricola = studente['nome'][0] + studente['cognome'][0]


print('random', numberMatricola)
print(matricola)
