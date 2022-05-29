# importo moduli e funzioni
from datetime import date, timedelta
from calendar import monthrange
from regexData import regexData
from stampaReport import stampaReport
from calcoloOre import calcoloOre

# definisco la funzione
def report(inizio = None, fine = None, file = list(), radice = True):
    '''a partire dall'oggetto data di fine (e di inizio facoltativa), invoca calcoloOre e stampaReport per creare e stampare i report del periodo'''

    try:
        if inizio == None:
            inizio = fine - timedelta(days = fine.weekday())

        inizio = regexData(inizio)
        fine = regexData(fine)

        if (inizio.month == fine.month) and (inizio.year == fine.year): # se si sta considerando un solo mese, invoca calcoloOre sul mese e aggiunge il nome del file alla lista
            file.append(calcoloOre(inizio = inizio, fine = fine))

        else: # invoca ricorsivamente report su un sottoperiodo passando la lista dei report intermedi già creati
            intermedio1 = date(inizio.year, inizio.month, monthrange(inizio.year, inizio.month)[1])
            intermedio2 = intermedio1 + timedelta(days = 1)
            report(inizio = inizio, fine = intermedio1, file = file, radice = False) # se radice = True stampa il report anche mese per mese (oltre a quello completo)
            report(inizio = intermedio2, fine = fine, file = file, radice = False) # se radice = True stampa il report anche mese per mese (oltre a quello completo)

        if radice: # le funzioni invocate ricorsivamente sono terminate, invoco stampaReport per creare il report finale
            listaFile = [nome for nome in file if nome is not None]
            stampaReport(listaFile = listaFile)
            return
    except:
        return

