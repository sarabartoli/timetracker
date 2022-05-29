# importo moduli e funzioni
from re import sub
from datetime import datetime
from regexData import regexData
from colori import *

# definisco la funzione
def calcoloOre(inizio, fine):
    '''prende in input un oggetto data inizio e data fine, calcola il numero di ore di un timesheet per progetto e giorno e scrive un report intermedio, ritorna il nome del file scritto'''

    oreLavoro = 8 # giornata lavorativa di 8 ore
    minutiProgetto = {}
    minutiGiorno = {}
    oggi = datetime.today()
    leggere = f'{inizio.year}{inizio.month}.txt'
    scrivere = f'report_i_{oggi.date()}-{oggi.hour}-{oggi.minute}-{oggi.second}-{oggi.microsecond}_{inizio}_{fine}.txt'

    try:
        with open(leggere, 'r') as fileLetto:
            timesheet = [riga.split(' ') for riga in fileLetto]

        for riga in timesheet:
            quando = regexData(riga[0])
            progetto = riga[3]
            minuti = int(riga[1]) * 60 + int(riga[2])

            if inizio <= quando <= fine:
                if progetto in minutiProgetto.keys():
                    minutiProgetto[progetto] += minuti
                else:
                    minutiProgetto[progetto] = minuti
                if quando in minutiGiorno.keys():
                    minutiGiorno[quando] += minuti
                else:
                    minutiGiorno[quando] = minuti

        for giorno, tempo in minutiGiorno.items():
            if tempo / 60 != oreLavoro:
                printOrange(f'\nAttenzione: il giorno {giorno} risultano {tempo} minuti lavorati, una differenza di {int((tempo - oreLavoro * 60) / 60)}h e {(tempo - oreLavoro * 60) % 60} minuti rispetto ad una giornata di {oreLavoro} ore\n')

        with open(scrivere, 'w') as fileScritto:
            for progetto, tempo in minutiProgetto.items():
                fileScritto.write(f'{tempo} {progetto}\n')
            fileScritto.write('---\n')
            for giorno, tempo in minutiGiorno.items():
                fileScritto.write(f'{tempo} {giorno}\n')

        return scrivere

    except FileNotFoundError:
        printRed(f"\nIl timesheet {sub('.txt', '', leggere)} non esiste\n")
        return
