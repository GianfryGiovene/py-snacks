# Siete stati chiamati dal responsabile IT del Contact Center della vostra ditta per scrivere un programma Python che calcoli il sentiment (sentiment analysys) delle mail che arrivano in modo da poterlo misurare mese per mese.

# Non conosciamo ancora i metodi del machine learning, quindi proviamo ad usare un semplice ma efficace metodo basato sui Dictionary.

# Un collega esperto del contact center ci fornisce un Dictionary in cui sono presenti parole chiavi e per ciascuna un punteggio da 0 a 5, con questa scala:

# 1 = negativo
# 2 = parzialmente negativo
# 3 = neutro
# 4 = parzialmente positivo
# 5 = positivo
# Di seguito il Dictionary:

# wordict = { "purtroppo" : 2, "anomalia" : 1, "errore" : 1, "lamentele" : 2, "rimborsi" : 1, "disservizi" : 1, "ritardi" : 2, "problema" : 1, "grande": 4, "ringraziare": 4, "eccellente": 5, "bravissimi": 5 }

# L’esercizio consiste nello scrivere un programma python che legge il contenuto delle mail (per semplicità le considereremo una string) e in caso di presenza delle parole contenute nel dizionario, effettui la media dei punteggi ottenuti.


import re


wordict = {"purtroppo": 2, "anomalia": 1, "errore": 1, "lamentele": 2, "rimborsi": 1, "disservizi": 1,
           "ritardi": 2, "problema": 1, "grande": 4, "ringraziare": 4, "eccellente": 5, "bravissimi": 5}

email_1 = "Purtroppo il dispositivo è quasi sempre in queste condizioni..se ne richiede pertanto, ASSISTENZA RISOLUTIVA, per via anche, delle continue lamentele e dei continui rimborsi ai clienti. Cordiali Saluti"
email_2 = "con la presente segnaliamo numerosi disservizi alla Clientela, nelle ultime settimane, derivanti dai ritardi nella generazione/spedizione dei documenti che si aspettano. Abbiamo difficoltà a tranquillizzare i Clienti in quanto il problema e’ diffuso e si protrae da molto tempo. Sapete dirci se e’ stata analizzata la questione e se e’ gia’ stata individuata una data potenziale di risoluzione dell’anomalia?"
email_3 = "Ciao, mi prendo un momento per ringraziare te e tutta la squadra per il grande lavoro che state facendo in queste settimane. Avete consentito in modo eccellente di continuare a lavorare, funzionare, servire i clienti. Un grazie sincero. Siete stati bravissimi. Davvero! Non ci sono tante aziende in Italia che hanno avuto la stessa continuità"


emails = [email_1, email_2, email_3]

for email in emails:

    emailConverted = re.split("'| ", email)
    somma = 0
    counter = 0

    for word in emailConverted:
        for key in wordict:
            if word.lower() == key:
                counter += 1
                print('questa è una parola: ', word,
                      'ne sono state individuate: ', counter)
                somma += wordict[key]

    media = somma / counter
    print('la media è: ', media)
