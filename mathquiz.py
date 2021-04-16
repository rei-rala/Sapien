import random
import time


from tabla import TABLA_OPERACIONES
from gral import *


def Welcome():
    print(f'\nBienvenido a Sapien, el juego de trivia matematica\n')
    time.sleep(2.50)
    change_conditions()

if __name__ == '__main__':
    Welcome()

This_Game = Conditions(int(c[0]), int(c[1]))

print('\n', This_Game, '\n\n')


def Sapien(p):
    clear()  # blanqueo de terminal
    select = random.choice(list(TABLA_OPERACIONES.keys()))
    key_operation = str(select)

    time.sleep(0.75)
    p.round += 1
    print(
        f'RONDA {p.round} \n\nJUGADOR {bcolors.WARNING} {p.nombre}{bcolors.ENDC},')
    time.sleep(2.5)
    print(f'Dada la siguiente operacion:\n')
    time.sleep(2.5)
    print(f'{bcolors.FAIL} {select} {bcolors.ENDC}')
    # print( TABLA[select] ) # DEBUG? -> arroja el resultado :D

    time.sleep(0.75)
    print('\nIngrese respuesta en numeros enteros: ')
    # respuesta del usuario tras seleccion de operacion matematica aleatoria
    respuesta = input('--> ')

    time.sleep(1.5)

    try:
        TABLA_OPERACIONES[select] != int(respuesta)
    except:
        print(
            f'\n\n\n{bcolors.WARNING}RESPUESTA INCORRECTA!{bcolors.ENDC}\n\n\n')
        p.puntos -= 1
        # aniade los errores a la clase para mostrarlos al decidir ganador
        p.errores.append(f'Round {p.round} -> {select} = {str(respuesta)}')
    else:
        if TABLA_OPERACIONES[select] != int(respuesta):
            print(
                f'\n\n\n{bcolors.WARNING}RESPUESTA INCORRECTA!{bcolors.ENDC}\n\n\n')
            p.puntos -= 1
            # aniade los errores a la clase para mostrarlos al decidir ganador
            p.errores.append(f'Round {p.round} -> {select} = {str(respuesta)}')

        else:
            print(f'\n\n\n{bcolors.OKCYAN}Correcto!{bcolors.ENDC}\n\n\n')
            p.aciertos += 1
            p.puntos += 2

    # print( len(TABLA) )    # DEBUG de tamanio de tabla
    # Elimina la opcion elegida por el sistema para evitar que haya dos opciones iguales
    TABLA_OPERACIONES.pop(key_operation)
    # print( len(TABLA) )    # DEBUG de tamanio de tabla (debe ser -1 a linea 33)
    time.sleep(3)


# crea clases en funcion de la cantidad de jugadores declarados
for i in range(This_Game.q_players):
    time.sleep(1)
    # DEBUG -> i = Jugador( nombre=f'JUGADOR {i+1}' ), puntos=0, aciertos=0, errores=[] ) / creacion de clases con nombre personalizado
    i = Jugador(input(
        f'{bcolors.OKGREEN}Ingrese nombre para jugador {i+1}: {bcolors.ENDC}'), 0, 0, [], 0)
    PLAYER_LIST.append(i)  # aniade la clase creada a la lista de jugadores
    # print(f'{i.nombre}, PUNTOS {i.puntos}, ACIERTOS {i.aciertos}, ERRORES {i.errores}') # DEBUG / test de clase creada para Jugador 'i' ->


def GAME():     # Tras definicion de cantidad de jugadores y de rondas, proceden a generarse cuanta instancia de juego sea necesaria
    for j in PLAYER_LIST:
        for g in range(This_Game.q_rounds):
            Sapien(j)


time.sleep(0.5)
print('\nPreparados')
time.sleep(1)
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
GAME()

AND_THE_WINNER_IS()


time.sleep(5)
input(f'{bcolors.OKGREEN}\n\nJuego Finalizado.{bcolors.ENDC}\nIngrese cualquier tecla para finalizar\n')

'''
if input('Ingrese "Y" para volver a jugar o cualquier tecla para cerrar: ').upper() == 'Y':
    PL.clear()
    players = 2# int(input(f'Ingrese cantidad de jugadores: ' ))  # o poner un valor fijo de tipo INT
    rounds =  1#int(input(f'Ingrese cantidad de rondas: ' ))  # o poner un valor fijo de tipo INT
    TABLA = RESTOCK
    GAME()
'''