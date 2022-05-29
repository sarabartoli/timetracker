# importo moduli e funzioni
import os
from re import sub
from regexData import regexData
from stampa import stampa
from colori import *

# definisco la funzione
def leggiReport(file):
    '''legge un report finale esistente, stampa le ore per ogni progetto e un warning se i timesheet del periodo sono stati modificati dopo la creazione del report'''

    infoFile = file.split('_')
    meseInizio = regexData(infoFile[3]).month
    meseFine = regexData(sub('.txt', '', infoFile[4])).month
    annoInizio = regexData(infoFile[3]).year
    annoFine = regexData(sub('.txt', '', infoFile[4])).year

    elencoTimesheet = stampa(cosa = os.listdir(), yesPrint = False, printColor = printWhite)
    tsCoinvolti = list()

    for timesheet in elencoTimesheet.values():
        anno = int(timesheet[:4])
        mese = int(timesheet[4:])

        if annoInizio <= anno <= annoFine:
            if meseInizio <= mese <= meseFine:
                tsCoinvolti.append(timesheet)

    ultimaModTs = [os.path.getmtime(f'{os.getcwd()}\\{ts}.txt') for ts in tsCoinvolti]
    ultimaModReport = os.path.getmtime(f'{os.getcwd()}\\{file}')

    for i in range(len(ultimaModTs)):
        if ultimaModTs[i] > ultimaModReport:
            printRed(f"\nAttenzione: il timesheet {tsCoinvolti[i]} è stato modificato dopo la creazione di {sub('.txt', '', file)}\n")

    with open(file, 'r') as report:
        righe = report.readlines()
    rigaBreak = righe.index('---\n')

    printWhite('\nReport: ')
    printYellow(f"{sub('.txt', '', file)}\n\n")
    for riga in righe[:rigaBreak]:
        riga = riga.split()
        ore = riga[0]
        minuti = riga[1]
        progetto = ' '.join(riga[2:])
        printCyan(f'{ore}h '.rjust(6), f'{minuti}m - '.rjust(6), progetto, '\n')

    printWhite('\nCreato tramite i report intermedi:\n')
    for intermedio in righe[rigaBreak+1:]:
        printYellow(f"{sub('.txt', '', intermedio)}")

    return
