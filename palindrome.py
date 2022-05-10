# Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure meno.

myWord = input()
reverseWord = myWord[::-1]
if myWord == reverseWord:
    print('è palindromo')
else:
    print('non è palindromo')
