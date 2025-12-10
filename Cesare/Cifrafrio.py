###CIFRARIO DI CESARE

import time 
import os 
import string 

os.system('color 3')
os.system('cls')

def head():
    print('-' * 40)
    print('               CIFRARIO')
    print('-' * 40)
def operazioni():
    print('[1] Cifra' \
    '\n[2] Decifra' \
    '\n[3] Info' \
    '\n[4] Exit')
    print('-' * 40)
class cifrario:
    def __init__(self, frase, chiave):
        self.chiave = chiave
        self.frase = frase
        self.alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.list = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_","`", "{", "|", "}", "~", '0', '1', '2', '3', '3', '4', '5', '6', '7', '8', '9']
    def cifra(self):
        cifrata = []
        parola = []
        x = self.frase.upper()
        for i in range(len(x)):
            parola.append(x[i])
        for i in range(len(parola)):
            Trovato = False
            Speciale = False
            for j in range(len(self.alfabeto)):
                try: 
                    if parola[i] == self.alfabeto[j]:
                        alfa2 = self.alfabeto * 2
                        cifrata.append(alfa2[j + self.chiave])
                        Trovato = True
                        break
                except Exception as e:
                    print('[*] Chiave troppo elevata!')
            if not Trovato:
                for k in range(len(self.list)):
                    if parola[i] == self.list[k]:
                        cifrata.append(parola[i])
                        Speciale = True
                        break
        print('[*] Frase cifrata: ', end='') 
        for k in range(len(cifrata)): 
            print(cifrata[k], end='')   
    def decifra(self):
        decifrata = []
        parola = []
        x = self.frase.upper()
        for i in range(len(x)):
            parola.append(x[i])
        for i in range(len(parola)):
            Trovato = False
            Speciale = False
            for j in range(len(self.alfabeto)):
                try: 
                    if parola[i] == self.alfabeto[j]:
                        alfa2 = alfabeto * 2
                        decifrata.append(alfa2[j - self.chiave])
                        Trovato = True
                        break
                except Exception as e:
                    print('[*] Chiave troppo elevata!')
                    break
            if not Trovato:
                for k in range(len(self.list)):
                    if parola[i] == self.list[k]:
                        decifrata.append(parola[i])
                        Speciale = True
                        break
        print('[*] Frase cifrata: ', end='') 
        for k in range(len(decifrata)): 
            print(decifrata[k], end='')   
    
    
            
            
try: 
   while True:
        os.system('cls')
        head()
        operazioni()
        scelta = input('[+] Operazione: ')
        print('-' * 40)
        if scelta == str('1'):
            a = cifrario(None, None)
            alfabeto = a.alfabeto
            print('[*] Alfabeto: ', end='')
            for i in range(len(alfabeto)):
                print(alfabeto[i],'', end='')
            frase = input('\n[+] Frase da cifrare: ')
            chiave = int(input('[+] Chiave: '))
            a = cifrario(frase, chiave)
            a.cifra()
            input('\n[*] Premi invio per continuare.')
        elif scelta == str('2'):
            a = cifrario(None, None)
            alfabeto = a.alfabeto
            print('[*] Alfabeto: ', end='')
            for i in range(len(alfabeto)):
                print(alfabeto[i], '', end='')
            frase = input('\n[+] Frase da decifrare: ')
            chiave = int(input('[+] Chiave: '))
            a = cifrario(frase, chiave)
            a.decifra()
            input('\n[*] Premi invio per continuare.')
        elif scelta == str('3'):
            print('[*] Cifrario di cesare')
            print('\nIl cifrario di Cesare è uno dei più antichi e semplici algoritmi crittografici.' \
            '\nOgni lettera viene spostata avanti di un numero fisso di posti (la chiave). Se la chiave è 3, la A diventa D, la B diventa E, e così via.')
            input('\n[+] Premi invio per continuare.')
        elif scelta == str('4'):
            print('[*] Uscita...')
            time.sleep(2)
        else:
            print('[*] Operazione non valida!')
            time.sleep(1)
            continue 
except KeyboardInterrupt:
    print('\n[*] Aborto')