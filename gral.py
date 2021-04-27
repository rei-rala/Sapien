import time


import os
# creacion de methodo cls() para blanqueo de la terminal
def clear(): return os.system('cls')

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

cant_jugadores, cant_rounds = list(), list()
PLAYER_LIST = []
This_Game = ''


class Conditions():
    def __init__(self, jugadores, rounds):
        self.q_players = int(jugadores)
        self.q_rounds = int(rounds)
    def __str__(self):
        return 'Cantidad de jugadores: ' + str(self.q_players) + ', cantidad de rounds: ' + str(self.q_rounds)


class Jugador:
    def __init__(self, nombre, puntos=0, aciertos=0, errores=[], round=0):
        self.nombre = nombre
        self.puntos = puntos
        self.aciertos = aciertos
        self.errores = errores
        self.round = round
    def __str__(self):
        return f' {self.nombre}: puntos {self.puntos} - aciertos {self.aciertos}'


def q_cond(p):
    print(f'Ingrese valor para cantidad de {p}:')
    try:
        # debera ser un numero mayor a 0 o forzara un error
        q = int(input('--> '))
        if q <= 0:  
            0/0
    except Exception:
        time.sleep(0.5)
        print(f'\n{bcolors.FAIL}Valor ingresado para ',
              {p}, f' no valido {bcolors.ENDC}')
        time.sleep(0.5)
        q_cond(p)
    else:
        q = int(q)
        if p == 'JUGADORES':
            cant_jugadores.append(q)
        elif p == 'ROUNDS':
            cant_rounds.append(q)
        print()


# change_conditions ejecuta dos veces q_cond, la primera para fijar cantidad de jugadores y la segunda para cantidad de rounds
def change_conditions():  
    q_cond('JUGADORES')
    q_cond('ROUNDS')
    clear()

def countdown():
    time.sleep(0.5)
    print('\nPreparados')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)


def AND_THE_WINNER_IS():
    clear()

    def msj(ganador):
        if WINNER != 'EMPATE!':
            time.sleep(1)
            print(f'y el ganador es...')
            time.sleep(1)
            print(
                f'\ncon {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos: \n')
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
        print(f'Puntos de {i.nombre}: {i.puntos}')
        if i.errores == []:
            print(f'Jugador {i.nombre} no tuvo errores!')
        else:
            print(f'Errores de {i.nombre}: {i.errores}')
