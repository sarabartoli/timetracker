# importo moduli e funzioni
from datetime import date, datetime
from re import findall, sub
from leggiProgetti import leggiProgetti
from regexData import regexData
from somma import somma
from colori import *

# definisco la funzione
def stampaReport(listaFile):
    '''prende in input una lista di report intermedi, calcola, scrive e stampa il report finale'''

    oreLavoro = 8 # giornata lavorativa di 8 ore
    progettiLavorati = {}
    progetti = leggiProgetti()

    inizio = date(2099, 12, 31)
    fine = date(2000, 1, 1)
    oggi = datetime.today()
    nGiorni = 0

    for file in listaFile:
        with open(file, 'r') as report:
            righe = report.readlines()

        rigaBreak = righe.index('---\n')

        for riga in righe[:rigaBreak]:
            tempo = int(''.join(findall('.*\s', riga[:-1]))[:-1])
            progetto = ''.join(findall('\s.*', riga[:-1]))[1:]

            if progetto in progettiLavorati.keys():
                progettiLavorati[progetto] += tempo
            else:
                progettiLavorati[progetto] = tempo

        for riga in righe[rigaBreak+1:]:
            data = regexData(''.join(findall('\s.*', riga[:-1])))
            nGiorni += 1

            if data < inizio:
                inizio = data
            if data > fine:
                fine = data

    scrivere = f'report_f_{oggi.date()}-{oggi.hour}-{oggi.minute}-{oggi.second}-{oggi.microsecond}_{inizio}_{fine}.txt'
    printWhite(f'\nReport ore per progetto lavorato, dal '); printYellow(inizio); printWhite(' al '); printYellow(f'{fine}\n\n')

    chiavi = list()
    for chiave in progettiLavorati:
        chiavi.append(progetti.get(chiave, chiave))
    progettiLavoratiAlf = dict(sorted(zip(chiavi, list(progettiLavorati.values()))))

    with open(scrivere, 'w') as fileScritto:
        minutiEffettivi = 0
        for progetto, tempo in progettiLavoratiAlf.items():
            minutiEffettivi += tempo
            ore = tempo // 60
            minuti = tempo % 60
            fileScritto.write(f'{ore} {minuti} {progetto}\n')
            printCyan(f'{ore}h '.rjust(6), f'{minuti}m - '.rjust(6), progetto, '\n')
        fileScritto.write('---\n')
        for file in listaFile:
            fileScritto.write(f'{file}\n')

    printCyan(f'\nTotale: {minutiEffettivi // 60}h e {minutiEffettivi % 60} minuti in {nGiorni} giorni\n')
    minutiTeorici = nGiorni * oreLavoro * 60
    differenza = minutiEffettivi - minutiTeorici
    oreDifferenza = int(differenza / 60)
    minutiDifferenza = differenza % 60

    if differenza:
        printOrange(f'\nAttenzione: risultano {nGiorni} giorni lavorati, e uno scarto di {oreDifferenza}h e {minutiDifferenza} minuti rispetto a giornate di {oreLavoro} ore\n')

    printWhite('\nCreato tramite i report intermedi:\n')
    for intermedio in listaFile:
        printYellow(f"{sub('.txt', '', intermedio)}\n")

    inpt = input('\nPremi "S" per sommare le ore di due o più progetti, Invio altrimenti: ').strip().lower()
    if inpt == 's':
        somma(progettiLavorati)

    return
