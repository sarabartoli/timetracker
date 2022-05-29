# importo moduli e funzioni
from leggiProgetti import leggiProgetti
from stampa import stampa
from colori import *

# definisco la funzione
def somma(progettiTempo):
    '''prende in input un dizionario di progetti e tempo lavorato e stampa la somma delle ore di più progetti'''

    dizProgetti = {}
    for progetto in progettiTempo:
        dizProgetti[progetto] = leggiProgetti().get(progetto, progetto)

    print('\nProgetti:')
    stampa(cosa = dizProgetti, printColor = printYellow)

    inpt = input('\nInserisci il codice dei progetti di cui vuoi sommare le ore:\n').strip().lower()
    daSommare = inpt.split()

    tempo = 0
    for progetto in daSommare:
        tempo += progettiTempo.get(progetto, 0)

    desProgetti = [dizProgetti.get(cod, cod) for cod in daSommare]
    printCyan(f"\n{int(tempo / 60)}h e {tempo % 60} minuti - {' + '.join(desProgetti)}\n")

    return
