### PROGETTO AUTONOMO SVOLTO CON L'AUSILIO DI TUROIAL O PROGRAMMI OPEN SOURCE
### GIORNI DI LAVORO 04/12/2025 - 09/12/2025
###  Non mi sono mai impeganto così tanto ahahha 
### !IL DOSSIERGAGGIO O LA RACCOLTA DI DATI SENSEBILI È ILLEGALE!

import os
import time
import json

os.system("cls")
os.system("color 2")
def head():
    print("-" * 40)
    print("                DATABASE")
    print("-" * 40)

def operazioni():
    print("[1] Voci"
          "\n[2] Aggiungere voce"
          "\n[3] Sovrascrivere voce"
          "\n[4] Eliminare voce"
          "\n[5] Cerca voce"
          "\n[6] Cerca per nome e cognome" \
          "\n[7] Info"
          "\n[8] Exit")
    print("-" * 40)
class database:
    def __init__(self, voce, nome, cognome, età, data, stato, cittadinanza, comune, residenza, codice, recapito):
        self.voce = voce
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.data = data
        self.stato = stato
        self.cittadinanza = cittadinanza
        self.comune = comune
        self.residenza = residenza
        self.codice = codice
        self.recapito = recapito
    def aggiungi(self):
        record = {
            "Voce": self.voce,
            "Nome": self.nome,
            "Cognome": self.cognome,
            "Età": self.età,
            "Data di nascita": self.data,
            "Cittadinanza": self.cittadinanza,
            "Stato di Nascita": self.stato,
            "Comune di Nascita": self.comune,
            "Residenza": self.residenza,
            "Codice Fiscale": self.codice,
            "Recapito": self.recapito
        }

        db = self._carica()
        db.append(record)
        self._salva(db)

        print("[*] Voce aggiunta!")
        print("-" * 40, "\n")
    def print(self):
        db = self._carica()
        if not db:
            print("[*] Nessuna voce trovata!")
            print("-" * 40, "\n")
            return

        print("\nVOCI REGISTRATE:")
        for record in db:
            print("-" * 40)
            for k, v in record.items():
                print(f"[*] {k}: {v}")
        print("-" * 40, "\n")
    def sovrascrivi(self, voce_target):
        db = self._carica()
        db = [r for r in db if r.get("Voce") != voce_target]

        nuovo_record = {
            "Voce": self.voce,
            "Nome": self.nome,
            "Cognome": self.cognome,
            "Età": self.età,
            "Data di nascita": self.data,
            "Cittadinanza": self.cittadinanza,
            "Stato di Nascita": self.stato,
            "Comune di Nascita": self.comune,
            "Residenza": self.residenza,
            "Codice Fiscale": self.codice,
            "Recapito": self.recapito
        }

        db.append(nuovo_record)
        self._salva(db)

        print("[*] Voce sovrascritta correttamente.")
        print("-" * 40, "\n")
    def elimina(self, voce_target):
        db = self._carica()
        nuovo = [r for r in db if r.get("Voce") != voce_target]

        if len(nuovo) == len(db):
            print("[*] Nessuna voce trovata con quel nome.")
            print("-" * 40, "\n")
            return

        self._salva(nuovo)
        print("[*] Voce eliminata con successo!")
        print("-" * 40, "\n")
    def cerca(self, voce_target=None, nome_target=None, cognome_target=None):
        db = self._carica()
        trovati = []
        if voce_target is not None:
            trovati = [r for r in db if r.get("Voce", "").lower() == voce_target.lower()]
        if nome_target and cognome_target:
            trovati = [
                r for r in db
                if r.get("Nome", "").lower() == nome_target.lower()
                and r.get("Cognome", "").lower() == cognome_target.lower()
            ]
        if not trovati:
            print("[*] Nessun record trovato.")
            print("-" * 40, "\n")
            return
        print("\n[*] RISULTATI TROVATI:")
        for r in trovati:
            print("-" * 40)
            for k, v in r.items():
                print(f"{k}: {v}")
        print("-" * 40, "\n")
    def _carica(self):
        if not os.path.exists("database.json"):
            return []
        with open("database.json", "r") as f:
            return json.load(f)
    def _salva(self, db):
        with open("database.json", "w") as f:
            json.dump(db, f, indent=4)


try:
    while True:
        os.system("cls")
        head()
        operazioni()

        scelta = input("[+] Operazione: ")
        if scelta == "1":
            d = database(None, None, None, None, None, None, None, None, None, None, None)
            d.print()
            input("[*] Premi invio per continuare...")

        elif scelta == "2":
            print("-" * 40)
            voce = input("[+] Nome voce: ")
            nome = input("[+] Nome: ")
            cognome = input("[+] Cognome: ")
            età = input("[+] Età: ")
            data = input("[+] Data di nascita: ")
            cittadinanza = input("[+] Cittadinanza: ")
            stato = input("[+] Stato di nascita: ")
            comune = input("[+] Comune di nascita: ")
            residenza = input("[+] Residenza: ")
            codice = input("[+] Codice fiscale: ")
            recapito = input("[+] Recapito: ")

            d = database(voce, nome, cognome, età, data, stato, cittadinanza, comune, residenza, codice, recapito)
            d.aggiungi()
            input("[*] Premi invio per continuare...")
        elif scelta == "3":
            voce_target = input("[+] Voce da sovrascrivere: ")
            print("\n[*] Inserisci i nuovi dati:")
            voce = voce_target
            nome = input("[+] Nome: ")
            cognome = input("[+] Cognome: ")
            età = input("[+] Età: ")
            data = input("[+] Data di nascita: ")
            cittadinanza = input("[+] Cittadinanza: ")
            stato = input("[+] Stato di nascita: ")
            comune = input("[+] Comune di nascita: ")
            residenza = input("[+] Residenza: ")
            codice = input("[+] Codice fiscale: ")
            recapito = input("[+] Recapito: ")

            d = database(voce, nome, cognome, età, data, stato, cittadinanza, comune, residenza, codice, recapito)
            d.sovrascrivi(voce_target)
            input("[*] Premi invio per continuare.")
        elif scelta == "4":
            voce_target = input("[+] Nome voce da eliminare: ")
            d = database(None, None, None, None, None, None, None, None, None, None, None)
            d.elimina(voce_target)
            input("[*] Premi invio per continuare.")
        elif scelta == "5":
            voce_target = input("[+] Nome voce da cercare: ")
            d = database(None, None, None, None, None, None, None, None, None, None, None)
            d.cerca(voce_target=voce_target)
            input("[*] Premi invio per continuare.")
        elif scelta == "6":
            nome_target = input("[+] Nome da cercare: ")
            cognome_target = input("[+] Cognome da cercare: ")
            d = database(None, None, None, None, None, None, None, None, None, None, None)
            d.cerca(nome_target=nome_target, cognome_target=cognome_target)
            input("[*] Premi invio per continuare...")
        elif scelta == "7":
            print("[*] Database")
            print('\nSemplice schedazione di persone.' \
            '\nES:' \
            '\n[*] Voce = nome che vuoi dare alla voce/scheda' \
            '\n[*] Nome = Nome' \
            '\n[*] Cognome = Cognome' \
            '\n[*] Età = Età' \
            '\n[*] Data di nascita = Data di nascita' \
            '\n[*] Cittadinanza = Cittadinanza' \
            '\n[*] Stato di nascita = Stato di nascita' \
            '\n[*] Residenza = Residenza' \
            '\n[*] Codice fiscale = Codice fiscale' \
            '\n[*] Recapito = Recapito')
            print('\nLe informazioni posso essere trovate tramite ricerca per voce, oppure per nome e cognome.')
            print('\n!IL DOSSIERGAGGIO O LA RACCOLTA DI DATI SENSEBILI È ILLEGALE!')
            input('\n[+] Premi invio per continuare.')
        elif scelta == '8':
            print('[*] Uscita.')
            time.sleep(2)
            break

        else:
            print("[*] Operazione non valida!")
            time.sleep(1)

except KeyboardInterrupt:
    print("[*] Aborto")

