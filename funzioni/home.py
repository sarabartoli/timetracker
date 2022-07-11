# importo moduli e funzioni
import os
from pathlib import Path
from re import search
from datetime import datetime, timedelta
from leggiProgetti import leggiProgetti
from progetti import progetti
from report import report
from visualizzaFile import visualizzaFile
from timesheet import timesheet
from stampa import stampa
from leggiReport import leggiReport
from colori import *

# definisco la funzione
def home(printFunctions = True):
    '''chiede all'utente cosa vuole fare e invoca la funzione'''

    if printFunctions:
        printWhite("""
             ELENCO DELLE FUNZIONI:
         P - Visualizza e modifica l'elenco dei progetti
         O - Report orario di oggi
         I - Report orario di ieri
         S - Report orario della settimana in corso
         D - Report orario personalizzato
         E - Elimina riga da un timesheet
         L - Leggi un report già creato
         H - Leggi la guida
         C - Chiudi l'applicazione
     Invio - Inserisci orario del mese in corso (es. [4h] [30m] [4h30m] be [27])
    YYYYMM - Inserisci orario in un timesheet esistente (es. 202203)
              \n""")

    inpt = input('Funzione scelta: ').strip().lower()

    if inpt == 'p':
        progetti()
        home()

    elif inpt == 'o':
        report(inizio = datetime.today().date(), fine = datetime.today().date(), file = list())
        home()

    elif inpt == 'i':
        sabatoLavorativo = False # True se il sabato è lavorativo
        oggi = datetime.today().date()
        if oggi.weekday() == 0 and sabatoLavorativo:
            ieri = oggi - timedelta(days = 2)
        elif oggi.weekday() == 0 and not sabatoLavorativo:
            ieri = oggi - timedelta(days = 3)
        else:
            ieri = oggi - timedelta(days = 1)
        report(inizio = ieri, fine = ieri, file = list())
        home()

    elif inpt == 's':
        report(fine = datetime.today().date(), file = list())
        home()

    elif inpt == 'd':
        inizio = input('\nData inizio (AAAA MM DD): ')
        fine = input('Data fine (AAAA MM DD): ')
        report(inizio = inizio, fine = fine, file = list())
        home()

    elif inpt == 'e':
        print('\nScegli il file da cui eliminare la riga:')
        stampa(cosa = os.listdir(), printColor = printWhite)
        file = input('\nFile: ').strip()
        visualizzaFile(file = f'{file}.txt')
        home()

    elif inpt == 'l':
        print('\n')
        reportStampa = stampa(cosa = os.listdir(), noReport = False)
        quale = input('\nInserisci il numero del report: ').strip()
        if quale in reportStampa:
            leggiReport(file = f'{reportStampa.get(quale)}.txt')
        else:
            printRed(f'Il report specificato (n. {quale}) non esiste\n')
        home()

    elif inpt == 'h':
        percorso = Path(os.path.realpath(__file__)).parent.parent
        with open(f'{percorso}\\readme.txt', 'r') as guida:
            readme = guida.readlines()
        printRainbow(listaTesto = readme)
        home()

    elif inpt == 'c':
        return

    elif search('\A20\d{3}\d?\Z', inpt):
        if os.path.isfile(f'{inpt}.txt'):
            print(f'\nFile: {inpt}\n\nProgetti:')
            stampa(cosa = leggiProgetti(), printColor = printYellow)
            ore = input('\nOrario: ').strip().lower()
            timesheet(evento = ore, nomeFile = f'{inpt}.txt', obbligoData = True)
            home()
        else:
            printRed(f'\nIl file specificato {inpt} non esiste in {os.getcwd()}, scegliere un nome file tra quelli esistenti:\n')
            stampa(cosa = os.listdir(), printColor = printWhite)
            home()

    elif inpt == '':
        print('\nProgetti:')
        stampa(cosa = leggiProgetti(), printColor = printYellow)
        ore = input('\nOrario: ').strip().lower()
        timesheet(evento = ore)
        home()

    else:
        printRed('\nLa funzione scelta non esiste\n\n')
        home(printFunctions = False)

