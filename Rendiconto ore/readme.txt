Sviluppato da github.com/sarabartoli
Coding utf-8
Formato inserimento date: AAAAMMDD, AAAA MM DD, AAAA-MM-DD, AAAA/MM/DD (202203 21, 2022-03/21)
Formato inserimento attivita': codProgetto Xh Xm dD (be 2h 30m 27, 2h be, 27 30m be)
                            di default il giorno e' oggi e ore e minuti sono 0
                            tempi negativi vengono automaticamente trasformati in positivi
                            non inserire spazi tra numeri e h/m
Per inserire l'orario relativo ad un progetto, è necessario prima censire il progetto
    Il codice progetto deve iniziare con una lettera, puo' contenere solo lettere e numeri
    Gli input sono case-insensitive e vengono trasformati in lowercase, ma i codici progetto e le descrizioni possono essere stampati con le maiuscole
    Per rendere non modificabile l'elenco dei progetti, modificare il eliminaRiga.py commentando la riga 10 e togliendo il commento dalla riga 9
Il nome dei timesheet e' AAAAMm.txt, quando si visualizza un timesheet il nome va inserito senza .txt (20223, 202212)
I timesheet e i report sono salvati nella sottocartella file, non rinominarli e non spostarli
E' sconsigliato modificare manualmente il contenuto dei file
Le funzioni sono nella sottocartella funzioni, non rinominarle e non spostarle
Se stampando un report su piu' mesi, si vuole anche il report mese per mese (ad eccezione dell'ultimo), modificare la funzione report
Se la giornata lavorativa non è di 8 ore, modificare le funzioni calcoloOre e stampaReport
Se il sabato e' un giorno lavorativo, modificare sabatoLavorativo in home
I file di report intermedi (report_i_timestamp_AAAAMmDdInizio_AAAAMmDdFine.txt), contengono report per progetto e per data (di un solo mese)
I file di report finali (report_f_timestamp_AAAAMmDdInizio_AAAAMmDdFine.txt), contengono report per data di più mesi
Non viene controllato il numero di ore inserito per ogni giorno, viene stampato un warning a schermo (in fase di creazione del report) se le ore inserite per ogni giorno sono diverse da otto
Per il calcolo dello scarto delle ore lavorate, non vengono considerati i giorni che non hanno entrate
    se un giorno sono inserite otto ore e un altro zero, non verranno stampati warning
Il report settimanale considera i giorni dal lunedi' al giorno odierno, anche se sono inserite ore per i giorni futuri
Quando si aggiunge un'attivita' in un timesheet di un mese passato e' obbligatorio inserire il DD
Non e' possibile aggiungere attivita' di mesi futuri,
    a meno di creare manualmente il file AAAAMm.txt nella sottocartella file e modificarlo come se fosse un mese passato
Funziona per date dal 1 gennaio 2000 al 31 dicembre 2099
Durante la lettura di un report, non viene controllato se la data di creazione e di ultima modifica coincidono
    se non coincidono, il report e' stato modificato a mano e i risultati potrebbero essere inconsistenti
Icona da https://www.flaticon.com/free-icon/schedule_1497835
Colori https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
Spostare la cartella scaricata in qualsiasi percorso, poi creare un collegamento a RendicontoOre.py dalla cartella funzioni in qualsiasi percorso per avviarlo velocemente
