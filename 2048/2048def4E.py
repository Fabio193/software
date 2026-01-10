### PCTO 4E A.S:2025/2026 


import time
import os
import random 
import msvcrt

os.system('color 3')
os.system('cls')

class Gioco():                                              ### classe principale del gioco
    def __init__(self):                                     ### metodo di inizializzazione della classe. L'inizializzazzione consiste nel creare oggetti indipiendenti della classe. Richimabili in  ogni metodo           
        self.y = 4                                          ### numero di colonne della matrice                    
        self.x = 4                                          ### numero di righe della matrice
        self.larg = 4                                       ### larghezza della cella della matrice     
        self.p = ' ' * self.larg + '|'                      ### rappresentazione di una cella vuota nella matrice, moltiplicazione di spazi per la larghezza della cella per far entrare i numeri
        self.matr = []                                      ### inizializzazione della matrice come lista vuota che sarà la nosta matrice   
        for i in range(self.x):                             ### ciclo per creare le righe della matrice 
            n = []                                          ### inizializzazione di una riga vuota             
            for j in range(self.y):                         ### ciclo per creare le colonne della matrice
                n.insert(i, self.p)                         ### inserisce nella riga una cella vuota rappresentata da self.p
            self.matr.append(n)                             ### aggiunge la riga alla matrice vuota    
    





    def popola(self):                                       ### metodo per popolare la matrice con due numeri iniziali          
        self.add()                                          ### chiama il metodo add per aggiungere un numero nella matrice       
        self.add()                                          ### chiama il metodo add per aggiungere un secondo numero nella matrice (Aggiunge due numeri iniziali alla matrice vuota)
                                        






    def add(self):                                          ### metodo per aggiungere un nuovo numero nella matrice
        pos = []                                            ### lista per memorizzare le posizioni vuote
        for i in range(len(self.matr)):                     ###ciclo sulle righe della matrice. Per ogni elemento della riga scnasiona le colonne
            for j in range(len(self.matr[i])):              ### Scansione delle colonne della matrice   
                if self.matr[i][j] == self.p:               ### se la cella è vuota. Cella vuota è rappresentata da self.p, nel inizializzazzione della matrice
                    pos.append([i, j])                      ### aggiunge la poszione vuota alla lista pos
        if pos == []:                                       ### se non ci sono posizione vuote
            return                                          ### esce dalla funzione
        cord = random.choice(pos)                           ### sceglie una posizione vuota a caso dalla lista pos
        tmp = random.random()                               ### genera un numero casuale tra 0 e 1. Per decidere se mettere un 2 o un 4 nella matrice. Con 90% di probabilità esce 2 e con 10% esce 4: 9 possibilità di generare il 2 e 1 possibilità di generare il 4 
        if tmp < 0.9:                                       ### se il numero casuale è minore di 0.9
            numero = 2                                      ### assegna il valore 2 alla variabile numero: più probabile
        else:                                               ### altrimenti
            numero = 4                                      ### assegna il valore 4 alla variabile numero: meno probabile 
        self.matr[cord[0]][cord[1]] = self.cella(numero)    ### inserisce il numero generato nella matrice nella posizione scelta casualmente




    def sposta(self):
           pass





    def stampa(self):                                       ### metodo per stampare la matrice nel terminale              
        bordo = "+" + ("-" * self.larg + "+") * 4           ### crea la stringa del bordo superiore e inferiore della matrice in base alla larghezza delle celle(self.lang). Rendere il gioco più piacevole e dinamico
        for i in range(len(self.matr)):                     ### ciclo sulle righe della matrice
            print(bordo)                                    ### Stampa il bordo superiore della matrice      
            print("|", end='')                              ### Stampa il bordo sinistro della matrice senza andare a capo
            for j in range(len(self.matr[i])):              ### ciclo sulle colonne della matrice
                print(self.matr[i][j], end ='')             ### Stampa il contenuto della cella senza andare a capo(end=')
            print()                                         ### va a capo dopo aver stampato una riga della matrice        
        print(bordo)                                        ### Stampa il bordo inferiore della matrice      





    def valore(self, cella):                                ### metodo per ottenere il valore numerico di una cella della matrice, utile per le fusioni e aggiungere numeri. La cella è rappresentata come stringa ed è un oggetto interno del metodo
        if cella == self.p:                                 ### se la cella è vuota (rappresentata da self.p)
            return 0                                        ## restituisce 0 come valore numerico della cella vuota                 
        return int(cella.replace('|', '').strip())          ### altrimenti, rimuove il carattere '|' dalla stringa della cella, rimuove gli spazi vuoti con strip() e converte il risultato in un intero. Ci serve int per le operazioni matematiche
    


    
    def cella(self, n):                                     ### metodo per convertire un numero in una rappresentazione di cella della matrice come stringa       
        if n == 0:                                          ### se il numero è 0, di def valore
            return self.p                                   ### restituisce la rappresentazione di una cella vuota
        return f'{str(n).rjust(self.larg)}|'                ### altrimenti, converte il numero in stringa, lo giustifica a destra con rjust() in base alla larghezza della cella(self.larg) e aggiunge il carattere '|' alla fine per rappresentare la cella completa
    
    
    
    
    
    def merge(self, raw):                                  ### metodo per fondere una riga o colonna della matrice durante uno spostamento
        nonzero = []                                       ### lista temporanea per memorizzare i valori non zero della riga o colonna
        for i in raw:                                      ### ciclo sugli elementi della riga o colonna
            v = self.valore(i)                             ### ottiene il valore numerico dell'elemento usando il metodo valore
            if v != 0:                                     ### se il valore non è zero            
                nonzero.append(v)                          ### aggiunge il valore alla lista nonzero

        fusione = []                                       ### lista per memorizzare i valori fusi              
        tmp = 0                                            ### variabile temporanea per tenere traccia del valore da confrontare   
        for i in nonzero:                                  ### ciclo sui valori non zero                     
            if tmp == 0:                                   ### se tmp è zero, significa che non c'è un valore da confrontare
                tmp = i                                    ### assegna l'elemento corrente a tmp per il confronto successivo
            elif tmp == i:                                 ### se tmp è uguale all'elemento corrente, significa che possono essere fusi
                fusione.append(tmp + i)                    ### aggiunge la somma di tmp e l'elemento corrente alla lista fusione 
                tmp = 0                                    ### resetta tmp a zero per il prossimo confronto        
            else:
                fusione.append(tmp)                        ### se tmp e l'elemento corrente sono diversi, aggiunge tmp alla lista fusione
                tmp = i                                    ### aggiorna tmp con l'elemento corrente
        if tmp != 0:                                       ### dopo il ciclo, se tmp non è zero, significa che c'è un valore rimanente da aggiungere              
            fusione.append(tmp)                            ### aggiunge l'ultimo valore a fusione

        while len(fusione) < 4:                            ### riempie la lista fusione con zeri fino a raggiungere la lunghezza di 4 (dimensione della riga o colonna)           
            fusione.append(0)                              ### aggiunge zeri alla lista fusione   

        lista = []                                         ### lista finale per memorizzare la rappresentazione delle celle fusi       
        for i in fusione:                                  ### ciclo sui valori fusi 
            lista.append(self.cella(i))                    ### converte ogni valore fuso in una rappresentazione di cella usando il metodo cella e lo aggiunge alla lista finale  
        return lista                                       ### restituisce la lista finale delle celle fuse 

    def left(self):                                        ### metodo per spostare la matrice a sinistra      
        for i in range(4):                                 ### ciclo sulle righe della matrice      
            self.matr[i] = self.merge(self.matr[i])        ### fonde la riga usando il metodo merge e aggiorna la riga nella matrice

    def right(self):                                       ### metodo per spostare la matrice a destra         
        for i in range(4):                                 ### ciclo sulle righe della matrice            
            self.matr[i] = self.merge(self.matr[i][::-1])[::-1] ### inverte la riga, la fonde usando il metodo merge e poi inverte di nuovo la riga fusa per ottenere lo spostamento a destra

    def up(self):                                          ### metodo per spostare la matrice verso l'alto. Tratta le colonne come righe poiché il metodo merge funziona su righe da fondere verso sinistra
        for i in range(4):                                 ### ciclo sule colonne della matrice
            colonna = []                                   ### lista temporanea per memorizzare gli elementi della colonna
            for j in range(4):                             ### ciclo sulle righe della matrice
                colonna.append(self.matr[j][i])            ### aggiunge l'elemento della colonna alla lista temporanea
            colonna = self.merge(colonna)                  ### fonde la colonna usando il metodo merge
            for j in range(4):                             ### ciclo sulle righe della matrice(Agguinge elementi alle colonne)
                self.matr[j][i] = colonna[j]               ### aggiorna l'elemento della matrice con l'elemento fuso della colonna

    def down(self):                                        ### metodo per spostare la matrice verso il basso. Tratta le colonne come righe invertite poiché il metodo merge funziona su righe da fondere verso sinistra  
        for i in range(4):                                 ### ciclo sulle colonne della matrice            
            colonna = []                                   ### lista temporanea per memorizzare gli elementi della colonna      
            for j in range(4):                             ### ciclo sulle righe della matrice     
                colonna.append(self.matr[j][i])            ### aggiunge l'elemento della colonna alla lista temporanea    
            colonna = self.merge(colonna[::-1])[::-1]      ### inverte la colonna, la fonde usando il metodo merge e poi inverte di nuovo la colonna fusa per ottenere lo spostamento verso il basso   
            for j in range(4):                             ### ciclo sulle righe della matrice              
                self.matr[j][i] = colonna[j]               ### aggiorna l'elemento della matrice con l'elemento fuso della colonna

    def gioco(self):                                       ### metodo principale per eseguire il gioco
        self.popola()                                      ### chiama il metodo popola per inizializzare la matrice con due numeri
        self.stampa()                                      ### chiama il metodo stampa per visualizzare la matrice iniziale SUL TERMINALE
        try:                                               ### prov affinché l'utente possa interrompere il gioco con Ctrl+C      
            while True:                                    ### ciclo infinto per il gioco principale
                time.sleep(0.1)                            ### pausa di 0.1 secondi per evitare confussone 
                tasto = msvcrt.getch().decode('utf-8').lower()  ### legge un tasto premuto dall'utente e lo decodifica in una stringa minuscola

                prima = []                                  ### lista per memorizzare lo stato precedente della matrice per verificare se è cambiato qulcosa dopo uno spostamento e decidere se aggiungere un nuovo numero
                for r in self.matr:                         ### ciclo sulle righe della matrice
                    prima.append(r.copy())                  ### aggiunge una copia della riga alla lista prima

                if tasto == 'a':                            ### se il tasto premuto è 'a' (sinistra)   
                    self.left()                             ### chiama il metodo left per spostare la matrice a sinistra
                elif tasto == 'd':                          ### se il tasto premuto è 'd' (destra) 
                    self.right()                            ### chiama il metodo right per spostare la matrice a destra      
                elif tasto == 'w':                          ### se il tasto premuto è 'w' (su)         
                    self.up()                               ### chiama il metodo up per spostare la matrice verso l'alto          
                elif tasto == 's':                          ### se il tasto premuto è 's' (giù)
                    self.down()                             ### chiama il metodo down per spostare la matrice verso il basso      
                elif tasto == 'q':                          ### se il tasto premuto è 'q' (esci)
                    break                                   ### esce dal ciclo e termina il gioco

                if tasto in ['w', 'a', 's', 'd']:           ### se il tasto premuto è uno dei tasti di movimento  
                    if prima != self.matr:                  ### se lo stato della matrice è cambiato dopo lo spostamento         
                        self.add()                          ### chiama il metodo add per aggiungere un nuovo numero alla matrice             

                    os.system('cls')                        ### pulisce il terminale per aggiornare la visualizzazione della matrice       
                    self.stampa()                           ### chiama il metodo stampa per visualizzare la matrice aggiornata                

        except KeyboardInterrupt:                           ### gestisce l'interruzione del gioco con Ctrl+C          
            print('\n[*] ABORTO')                           ### stampa un messaggio di aborto del gioco           

print('-' * 60)
print(' '*18, 'GIOCO 2048 PCTO 4E')
print('-' * 60)
print('[1] Gioca a 2048' \
'\n[2] Visualizzazione' \
'\n[3] Esci')
print('-' * 60)


scelta = input('[+] Opzione: ')
gioco = Gioco()                                    ### crea un'istanza della classe Gioco
try:
    if scelta == '1':
        os.system('cls')
        gioco.gioco()                                      ### chiama il metodo gioco per avviare il gioco
    elif scelta == '2':
        gioco = Gioco()                                    ### crea un'istanza della classe Gio
        print('')
        print('-' * 60)
        print(' '*18,'COSTRUZIONE 2048')
        print('-' * 60)
        print('\n↳ Costruzione della matrice di gioco')
        gioco.stampa()                                     ### chiama il metodo stampa per visualizzare la matrice iniziale
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Popolamento della matrice con due numeri iniziali')
        gioco.popola()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Spostamento a sinistra')
        gioco.left()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Aggiunta di un nuovo numero')
        gioco.add()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Spostamento a destra')
        gioco.right()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Aggiunta di un nuovo numero')
        gioco.add()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Spostamento verso l\'alto')
        gioco.up()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Aggiunta di un nuovo numero')
        gioco.add()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Spostamento verso il basso')
        gioco.down()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Aggiunta di un nuovo numero')
        gioco.add()
        gioco.stampa()
        input('\n[+] Premi invio per continuare.')
        print('\n↳ Fusione')
        raw = [2, 2, 4, 0]
        print('[+] Riga originale:', raw)
        fused = gioco.merge([gioco.cella(n) for n in raw])
        print('[*] Riga fusa:', fused)

        input('\n[+] Premi invio per uscire.')
    elif scelta == '3':
        print('[*] Uscita in corso...')
    else:
        print('[*] Scelta non valida. Uscita...')


except KeyboardInterrupt:
    print('\n[*] ABORTO')                               ### gestisce l'interruzione del gioco con Ctrl+C e stampa un messaggio di aborto del gioco
