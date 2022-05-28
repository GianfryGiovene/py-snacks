"""
Il ROT-13 è un semplice cifrario monoalfabetico,
in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata, 
o decriptarla se la stringa è già stata precedentemente codificata.
"""


def rot_13(word):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    abet = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_word = ''
    for char, in word:
        for c in range(0, 12):
            if char == ' ':
                char = ' '
                encrypted_word += char
            elif char == abet[c]:
                char = alph[c]
                encrypted_word += char
            elif char == alph[c]:
                char = abet[c]

                encrypted_word += char
    print(encrypted_word)


rot_13('''qnv yn puvnir qry prffb nq ha pbtyvbar r aba pntuv cvu ''')
