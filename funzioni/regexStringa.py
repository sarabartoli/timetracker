# importo moduli e funzioni
from re import findall
from datetime import date, datetime
from leggiProgetti import leggiProgetti
from colori import *

# definisco la funzione
def regexStringa(stringa, giorno, mese, anno, obbligoData):
    '''prende una stringa in input, giorno, mese, anno odierni e un booleano obbligoData; restituisce l'output da scrivere nel timesheet sotto forma di dizionario'''

    dizionario = {'quando': None, 'ore': 0, 'minuti': 0, 'codProgetto': None, 'desProgetto': None, 'timestamp': datetime.today()}

    try:
        giornoIns = ''.join(findall(r'\b(0?[1-9]?|[1-2]\d|3[0-1])\b', stringa)).strip()
        if giornoIns != '':
            giorno = int(giornoIns)

        if obbligoData and giornoIns == '':
            printRed('\nStai modificando il timesheet di un mese passato, è obbligatorio inserire il giorno\n')
            return

        dizionario['quando'] = str(date(anno, mese, giorno))

        oreIns = ''.join(findall('[0-9]?[0-9]?[0-9]+h+', stringa))
        if oreIns:
            dizionario['ore'] = int(oreIns[:-1])

        minutiIns = ''.join(findall('[0-9]?[0-9]?[0-9]+m+', stringa))
        if minutiIns:
            dizionario['minuti'] = int(minutiIns[:-1])

        codProgetto = ''.join(findall(r'\b[a-zA-Z]+[0-9]*[a-zA-Z]*\b', stringa))
        dizionario['codProgetto'] = codProgetto
        if leggiProgetti().get(codProgetto) is not None:
            desProgetto = leggiProgetti().get(codProgetto)
            dizionario['desProgetto'] = desProgetto

        else:
            printRed(f'\nIl codice progetto {codProgetto} non è stato censito, l\'orario non verrà inserito\n\n')
            return

        return dizionario

    except:
        printRed(f'\nErrore nell\'elaborazione dell\'input, il formato inserito non è corretto\n{stringa}\n\n')
        return
