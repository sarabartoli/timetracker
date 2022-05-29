# importo moduli e funzioni
from re import sub, search
from colori import *

# definisco la funzione
def stampa(cosa, noReport = True, yesPrint = True, printColor = printDefault):
    '''stampa a schermo liste e dizionari e ritorna le liste sottoforma di dizionari'''

    if type(cosa) is list:
        if noReport: # restituisce l'elenco dei timesheet sottoforma di dizionario e può stamparlo
            n = 0
            elenco = {}
            for elemento in cosa:
                if not (elemento == 'elencoProgetti.txt' or search('\Areport', elemento)):
                    elenco[n] = sub('.txt', '', elemento)
                    n +=1
                    if yesPrint:
                        printColor(sub('.txt', '', elemento), '\n')
            return elenco

        else: # restituisce l'elenco dei report finali sottoforma di dizionario e lo stampa invocando stampa sul dizionario
            n = 0
            elencoReport = {}
            reportStampa = {}
            for elemento in cosa:
                if search('\Areport_f', elemento):
                    inizio = elemento.split('_')[3]
                    fine = sub('.txt', '', elemento.split('_')[4])
                    timestamp = elemento.split('_')[2]
                    reportStampa[f'Report n. {n}'] = f'Dal {inizio} al {fine}, creato il {timestamp}'
                    elencoReport[str(n)] = sub('.txt', '', elemento)
                    n += 1
            stampa(cosa = reportStampa, printColor = printWhite)
            return elencoReport

    if type(cosa) is dict: # stampa i dizionari
        maxChiave = max([len(k) for k in cosa.keys()])
        for chiave, valore in cosa.items():
            printColor(f'{chiave.rjust(maxChiave)} - {valore}\n')
        return
