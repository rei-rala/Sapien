import time

import os
clear = lambda: os.system('cls') # creacion de methodo cls() para blanqueo de la terminal

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

playerZ, roundZ = 'Not defined' , 'Not defined'
c = list()
PLAYER_LIST = []
This_Game = ''

class Conditions():
    def __init__(self, jugadores, rounds):
        self.q_players = int(jugadores)
        self.q_rounds = int(rounds)
    
    def __str__(self):
        return 'Cantidad de jugadores: ' + str(self.q_players) + ', cantidad de rounds: '  + str(self.q_rounds)

class Jugador:
    def __init__(self, nombre, puntos, aciertos, errores, round):
        self.nombre = nombre
        self.puntos = puntos
        self.aciertos = aciertos
        self.errores = errores
        
        self.round = round
    
    def __str__(self):
        return f' {self.nombre}, puntos {self.puntos} con {self.aciertos} aciertos'

def q_cond(p):
    print(f'Ingrese valor para ' , {str(p)} , ':' )
    try:
        q = int(input('--> '))
        if q <= 0: # en caso SER numerico, verifica qe sea mayor a 0
            0/0
    except Exception:
        time.sleep(0.5)
        print(f'\n{bcolors.FAIL}Valor ingresado para ' , {str(p)} , f' no valido {bcolors.ENDC}')
        time.sleep(0.5)
        q_cond(p)
    else:
        q = int(q)
        c.append(int(q))

def change_conditions(): # Se ejecuta dos veces, la primera para cantidad de jugadores, la segunda para cantidad de rounds
    time.sleep(0.5)
    q_cond('JUGADORES')
    print()
    
    time.sleep(0.5)
    q_cond('ROUNDS')
    
    clear()

def AND_THE_WINNER_IS():
    clear()
    def msj(ganador):
        if WINNER != 'EMPATE!':
            time.sleep(1)
            print(f'y el ganador es...')
            time.sleep(1)
            print(f'\ncon {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos: \n')
            time.sleep(2)
            print(f'\n{bcolors.WARNING}{ganador.nombre}!!!{bcolors.ENDC}\n')
        else:
            print('HUBO UN EMPATE! \n\n')
    base = -999
    for i in PLAYER_LIST:
        if i.puntos == base:
            WINNER = 'EMPATE!'
        elif i.puntos > base:
            base = i.puntos
            WINNER = i
    msj(WINNER)
    time.sleep(1.5)
    for i in PLAYER_LIST:
        if i.errores == []:
            print(f'Jugador {i.nombre} no tuvo errores!')
        else:
            print(f'Errores de {i.nombre}: {i.errores}')