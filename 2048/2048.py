### PCTO 4E


import time
import os
import random 
import msvcrt

os.system('color 3')
os.system('cls')

class Gioco():
    def __init__(self):
        self.y = 4
        self.x = 4
        self.matr = []
        for i in range(self.x):
            n = []
            for j in range(self.y):
                self.p = '   |'
                n.insert(i, self.p)
            self.matr.append(n)          
    
    
    def popola(self):
        pos = []
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                cord = [i, j]
                pos.append(cord)
    
        self.posizione = random.choice(pos)
        self.posizione2 = random.choice(pos)
        while self.posizione == self.posizione2:
            self.posizione2 = random.choice(pos)
        self.numero1 = 2
        self.numero2 = 2
        self.x = self.posizione[0]
        self.y = self.posizione[1]
        self.x1 = self.posizione2[0]
        self.y2 = self.posizione2[1]
        self.matr[self.x][self.y] = f' {self.numero1} |'
        self.matr[self.x1][self.y2] = f' {self.numero2} |'
        print(self.posizione, self.posizione2)
        print(pos)
    def sposta(self):
           pass
    def stampa(self):
        s = ''
        bordo = "+" + "---+" * 4                            
        for i in range(len(self.matr)):
            print(bordo)
            print("|", end='')
            for j in range(len(self.matr[i])):
                print(self.matr[i][j], end ='')
            print()
        print(bordo)
    def left(self):
        for i in range(4):
            lista = []
            for j in range(4):
                if self.matr[i][j] != self.p:
                    lista.append(self.matr[i][j])
            while len(lista) < 4:
                lista.append(self.p)
            self.matr[i] = lista
            os.system('cls')
            self.stampa()
    def right(self):
        for i in range(4):
            lista = []
            for j in range(4):
                while len(lista) < 4:
                    lista.append(self.p)
                ''''
                    for j in range(4):
                        if self.matr[i][j] != self.p:
                            lista.append(self.matr[i][j])
                    while len(lista) < 4:
                        lista.append(self.p)
                    '''
                for k in range(self.matr[i][j] != self.p):
                            print(k)
                            lista.remove(self.p)
                            lista.append(self.matr[i][j])
            self.matr[i] = lista
            os.system('cls')
            self.stampa() 
    def up(self):
        '''
        k = 0
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                if self.matr[i][j] != self.p:
                    k = k +1 
        for i in range(4)
        lista = []
            for j in range(4):
                lista.append(self.matr[i][j])
                if self.matr[i][j] != self.p:
                    for k in range(k):
                        self.matr[i] = lista
        self.stampa()
        '''
        for i in range(4):
            lista = []
            for j in range(4):
                if self.matr[j][i] != self.p:
                    lista.append(self.matr[j][i])
            while len(lista) < 4:
                lista.append(self.p)
            for j in range(4):
                self.matr[j][i] = lista[j]
        os.system('cls')
        self.stampa()
    def down(self):
        for i in range(4):
            lista = []
            for j in range(4):
                while len(lista) < 4:
                    lista.append(self.p)
                for k in range(self.matr[j][i] != self.p):
                            lista.remove(self.p)
                            lista.append(self.matr[j][i])
            for j in range(4):
                self.matr[j][i] = lista[j]
            os.system('cls')
            self.stampa() 
    def gioco(self):
        self.popola()
        self.stampa()
        try:
            while True:
                time.sleep(0.1)
                tasto = msvcrt.getch().decode('utf-8').lower()
                if tasto == 'a':
                    self.left()
                elif tasto == 'd':
                    self.right()
                elif tasto == 'w':
                    self.up()
                elif tasto == 's':
                    self.down()
                elif tasto == 'q':
                    break
        except KeyboardInterrupt:
            print('\n[*] ABORTO')

g = Gioco()
g.gioco()
