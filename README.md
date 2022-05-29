# Cosa fa
Rendiconta le ore lavorate sui progetti e crea report

# Cosa serve
L'installazione base di [python](https://www.python.org/downloads/)

# Setup
1. Scarica i file
2. Unzippa `timetracker-main` dove vuoi
3. Crea un collegamento a `RendicontoOre.py` (è nella sottocartella `funzioni`) dove ti è comodo
4. Cambia l'icona del collegamento, una possibile icona è nella sottocartella `file`

# Come si usa
1. Apri il collegamento
2. Censisci i progetti
    * Inserisci `P` e premi `Invio`
    *  Scrivi il codice del progetto e la descrizione: `pr1 Questo è il primo progetto`
3. Rendiconta le ore lavorate
    * Premi `Invio` per rendicontare le ore del mese in corso
    * Scrivi l'anno e il mese per rendicontare ore su un mese passato (es. `20223`)
    * Inserisci, nell'ordine che vuoi: il codice progetto su cui hai lavorato, ore e minuti, il giorno (di default è oggi) → `pr1 1h 30m 27`
4. Scegli uno tra `O`, `I`, `S`, `D` per creare report
5. Scegli `L` per leggere un report creato in precedenza
6. Scegli `E` per eliminare un orario inserito

# Good to know
* Il sabato non è lavorativo e la giornata ha otto ore, scegli `H` per scoprire come cambiare queste impostazioni
* È case insensitive
* Quando si inseriscono le date, inserire prima l'anno, poi il mese ed infine il giorno; spazi, trattini, barre, ecc. non sono influenti: `202203 27` e `2022-03/27` sono date valide
