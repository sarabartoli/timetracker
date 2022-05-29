# importo moduli e funzioni
from re import findall

# definisco la funzione
def leggiProgetti():
    '''legge il file elencoProgetti.txt e resitituisce un dizionario con codici e nome dei progetti'''

    with open('elencoProgetti.txt', 'r') as elencoProgetti:
        progetti = elencoProgetti.readlines()

    codici = [''.join(findall('\A[a-zA-Z]+[0-9]*-{1}', progetto))[:-1].lower() for progetto in progetti]

    descrizione = [''.join(findall('-.+', progetto))[1:] for progetto in progetti]

    dizionarioProgetti = {}.fromkeys(codici, None)

    for i in range(len(progetti)):
        dizionarioProgetti[codici[i]] = descrizione[i]

    return dizionarioProgetti
