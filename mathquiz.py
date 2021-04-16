import random
import time


from tabla import TABLA_OPERACIONES
from gral import *
from logger import logger


def Welcome():
    print(f'\nBienvenido a Sapien, el juego de trivia matematica\n')
    time.sleep(2.50)
    change_conditions()

if __name__ == '__main__':
    Welcome()

This_Game = Conditions( int(cant_jugadores[0]) , int(cant_rounds[0]) )
print(f'''
{This_Game}

''')


def Sapien(p):
    clear()

    time.sleep(0.75)
    p.round += 1
    select = random.choice(list(TABLA_OPERACIONES.keys()))
    key_operation = str(select)
    logger.debug(f'Jugador {p.nombre}, round {p.round} => Operacion aleatoria seleccionada \'{select}\' respuesta: {int(TABLA_OPERACIONES[select])}')

    print(f'RONDA {p.round} \n\nJUGADOR {bcolors.WARNING} {p.nombre}{bcolors.ENDC},')
    time.sleep(2.5)
    print(f'Dada la siguiente operacion:\n')
    time.sleep(2.5)
    print(f'{bcolors.FAIL} {select} {bcolors.ENDC}')

    time.sleep(0.75)
    print('\nIngrese respuesta en numeros enteros: ')

    # respuesta del usuario tras seleccion de operacion matematica aleatoria
    respuesta = input('--> ')

    time.sleep(1.5)

    try:
        TABLA_OPERACIONES[select] != int(respuesta)
    except:
        print(f'\n\n\n{bcolors.WARNING}RESPUESTA INCORRECTA!{bcolors.ENDC}\n\n\n')
        p.puntos -= 1
        p.errores.append(f'Round {p.round} -> {select} = {str(respuesta)}')
        logger.info(f'Anadido error Nro {len(p.errores)} en round {p.round} para jugador {p.nombre}: {select} = {str(respuesta)}')
        logger.info(f'Jugador {p.nombre} -1 puntos ({p.puntos}), total errores: {len(p.errores)}')
    else:
        if TABLA_OPERACIONES[select] != int(respuesta):
            print(f'\n\n\n{bcolors.WARNING}RESPUESTA INCORRECTA!{bcolors.ENDC}\n\n\n')
            p.puntos -= 1
            p.errores.append(f'En round {p.round} -> {select} = {str(respuesta)}')
            logger.info(f'Anadido error Nro {len(p.errores)} en round {p.round} para jugador {p.nombre}: {select} = {str(respuesta)}')
            logger.info(f'Jugador {p.nombre} -1 puntos ({p.puntos}), total errores: {len(p.errores)}')

        else:
            print(f'\n\n\n{bcolors.OKCYAN}Correcto!{bcolors.ENDC}\n\n\n')
            p.aciertos += 1
            p.puntos += 2
            logger.info(f'Jugador {p.nombre} +1 acierto ({p.aciertos}), +2 puntos ({p.puntos})')

    
    # Elimina la opcion elegida por el sistema para evitar que haya dos juegos iguales
    TABLA_OPERACIONES.pop(key_operation)

    logger.debug( f'Eliminado de la tabla: {key_operation}, tamano actual: {len(TABLA_OPERACIONES)}' )
    time.sleep(3)



# creacion de clases Jugador en funcion de la cantidad seleccionada
for i in range(This_Game.q_players):
    time.sleep(1)

    # DEBUG -> i = Jugador( nombre=f'JUGADOR {i+1}' ), puntos=0, aciertos=0, errores=[] ) / creacion de clases con nombre personalizado
    i = Jugador(input(f'{bcolors.OKGREEN}Ingrese nombre para jugador {i+1}: {bcolors.ENDC}'))

    # aniade la clase creada a la lista de jugadores
    PLAYER_LIST.append(i)
    logger.debug(f'Inicializado jugador{i}')


# Tras definicion de cantidad de jugadores y de rondas, proceden a generarse cuanta instancia de juego sea necesaria
def GAME():
    for p in PLAYER_LIST:
        for g in range(This_Game.q_rounds):
            Sapien(p)


countdown()
GAME()

AND_THE_WINNER_IS()


time.sleep(3)
input(f'{bcolors.OKGREEN}\n\nJuego Finalizado.{bcolors.ENDC}\nIngrese cualquier tecla para finalizar\n')

'''
if input('Ingrese "Y" para volver a jugar o cualquier tecla para cerrar: ').upper() == 'Y':
    PL.clear()
    players = 2# int(input(f'Ingrese cantidad de jugadores: ' ))  # o poner un valor fijo de tipo INT
    rounds =  1#int(input(f'Ingrese cantidad de rondas: ' ))  # o poner un valor fijo de tipo INT
    TABLA = RESTOCK
    GAME()
'''