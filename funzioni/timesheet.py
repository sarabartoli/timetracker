# importo moduli e funzioni
from re import findall, sub
from datetime import datetime
from regexStringa import regexStringa
from eliminaRiga import eliminaRiga
from colori import *

# definisco la funzione
def timesheet(evento, nomeFile = None, obbligoData = False):
    '''prende in input la stringa inserita, il nome del file se non è quello del mese corrente, scrive  l'input nel timesheet'''

    try:
        giorno = datetime.today().date().day
        mese = datetime.today().date().month
        anno = datetime.today().date().year

        if nomeFile is None:
            nomeFile = f'{anno}{mese}.txt'
        else:
            mese = int(''.join(findall('\d', nomeFile.strip()[4:])))
            anno = int(nomeFile.strip()[:4])

        daScrivere = regexStringa(stringa = evento, giorno = giorno, mese = mese, anno = anno, obbligoData = obbligoData)

        with open(nomeFile, 'a') as elencoOre:
            elencoOre.write(f"{daScrivere.get('quando')} {daScrivere.get('ore')} {daScrivere.get('minuti')} {daScrivere.get('codProgetto')} {daScrivere.get('timestamp')}\n")

        printGreen(f"""\n{daScrivere.get('timestamp')}:
Sono state aggiunte {daScrivere.get('ore')}h e {daScrivere.get('minuti')} minuti al progetto {daScrivere.get('desProgetto')}
per il giorno {daScrivere.get('quando')} nel file {sub('.txt', '', nomeFile)}\n\n""")

        inpt = input(f"""Se vuoi eliminare l\'ultima riga inserita digita "elimina"
oppure inserisci un nuovo orario per modificare il timesheet {sub('.txt', '', nomeFile)},
altrimenti premi Invio:\n""").strip().lower()
        if inpt == 'elimina':
            eliminaRiga(nomeFile)
        elif inpt == '':
            return
        else:
            timesheet(evento = inpt, nomeFile = nomeFile, obbligoData = obbligoData)
        return

    except:
        return
