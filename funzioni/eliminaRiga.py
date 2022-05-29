# importo moduli e funzioni
from re import search, sub
from colori import *

# definisco la funzione
def eliminaRiga(file, nRiga = -1):
    '''elimina una riga da un timesheet'''

    # if file == 'elencoProgetti.txt' or search('\Areport', file):
    if search('\Areport', file):
        printRed(f"Non è possibile eliminare righe da {sub('.txt', '', file)}\n\n")
        return

    else:
        try:
            with open(file, 'r') as fileR:
                righe = fileR.readlines()

            eliminata = righe.pop(nRiga)

            with open(file, 'w') as fileW:
                fileW.writelines(righe)

            printOrange(f"\nLa riga \"{eliminata[:-1]}\" è stata eliminata da {sub('.txt', '', file)}\n\n")

            return

        except:
            printRed(f"\nNon è stato possibile eliminare la riga {nRiga} da {sub('.txt', '', file)}\n\n")
            return
