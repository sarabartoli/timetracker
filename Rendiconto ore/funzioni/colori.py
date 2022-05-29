# importo moduli e funzioni
import os

# abilito l'output colorato
os.system('color')

# definisco le funzioni
def printRed(*args):
    for testo in args:
        print('\033[91m{}\033[39m'.format(testo), end = '')
    return

def printOrange(*args):
    for testo in args:
        print('\033[33m{}\033[39m'.format(testo), end = '')
    return

def printYellow(*args):
    for testo in args:
        print('\033[93m{}\033[39m'.format(testo), end = '')
    return

def printGreen(*args):
    for testo in args:
        print('\033[92m{}\033[39m'.format(testo), end = '')
    return

def printCyan(*args):
    for testo in args:
        print('\033[94m{}\033[39m'.format(testo), end = '')
    return

def printMagenta(*args):
    for testo in args:
        print('\033[95m{}\033[39m'.format(testo), end = '')
    return

def printWhite(*args):
    for testo in args:
        print('\033[97m{}\033[39m'.format(testo), end = '')
    return

def printDefault(*args):
    for testo in args:
        print('\033[39m{}\033[39m'.format(testo), end = '')
    return

def printRainbow(listaTesto):
    iT = 0
    iC = 0
    listaColori = [printRed, printOrange, printYellow, printGreen, printCyan, printMagenta, printWhite]

    while iT < len(listaTesto):
        if iC == len(listaColori):
            iC = 0
        listaColori[iC](listaTesto[iT])
        iC += 1
        iT += 1

    return
