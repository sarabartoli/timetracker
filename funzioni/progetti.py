# importo moduli e funzioni
from re import findall
from leggiProgetti import leggiProgetti
from stampa import stampa
from colori import *

# definisco la funzione
def progetti():
    '''stampa i progetti presenti e permette di censire progetti in elencoProgetti.txt'''

    with open('elencoProgetti.txt', 'a') as elencoProgetti:
        progettiPresenti = leggiProgetti()

        print('\nI progetti su cui stai lavorando sono:')
        stampa(cosa = progettiPresenti, printColor = printYellow)
        print(f"""\nAggiungi un nuovo progetto
il codice progetto deve iniziare con una lettera e può contenere solo lettere (non accentate) e numeri,
altrimenti premi Invio\n""")

        nuovoProgetto = input('codiceProgetto descrizione del progetto: ').strip()

        if nuovoProgetto.strip() == '':
            elencoProgetti.close()
            return

        else:
            codProgetto = ''.join(findall('\A[a-zA-Z]+[0-9]*', nuovoProgetto))
            desProgetto = ''.join(findall(' .+', nuovoProgetto))[1:]

            if desProgetto == '' or codProgetto == '':
                elencoProgetti.close()
                printRed('\nL\'input non è nel formato corretto\n')
                progetti()

            elif codProgetto.lower() in progettiPresenti.keys():
                elencoProgetti.close()
                printRed(f'\nIl codice progetto {codProgetto} esiste già, l\'elenco dei progetti non è stato modificato\n')
                progetti()

            else:
                elencoProgetti.write(f'{codProgetto}-{desProgetto}\n')
                elencoProgetti.close()
                printGreen(f'\nIl progetto {codProgetto} {desProgetto} è stato aggiunto\n')

                return
