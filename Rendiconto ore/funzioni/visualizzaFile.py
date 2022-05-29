# importo moduli e funzioni
import os
from eliminaRiga import eliminaRiga
from colori import *

# definisco la funzione
def visualizzaFile(file):
    '''stampa le righe di un file passato in input'''

    try:
        if os.path.isfile(file):

            with open(file, 'r') as fileAperto:
                righe = fileAperto.readlines()

            print('Scegli il numero di riga da eliminare\n')

            for i in range(len(righe)):
                print(f'Riga n. {i}: {righe[i]}')

            riga = int(input('Elimina la riga n. '))

            eliminaRiga(file = file, nRiga = riga)

        else:
            printRed(f'\nIl file {file} non esiste\n')
    except:
        return
