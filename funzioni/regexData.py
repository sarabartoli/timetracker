# importo moduli e funzioni
from re import findall
from datetime import date, datetime
from colori import *

# definisco la funzione
def regexData(data):
    '''prende una data o stringa in input (formato YYYY MM DD) e restituisce un oggetto data'''

    try:
        if type(data) is not date:
            anno = int(''.join(findall('\d', data)[:4]))
            mese = int(''.join(findall('\d', data)[4:6]))
            giorno = int(''.join(findall('\d', data)[6:]))
            data = date(anno, mese, giorno)
        return data
    except:
        printRed(f'\nLa data inserita {data} non è nel formato corretto "YYYY MM DD"\n')
        return
