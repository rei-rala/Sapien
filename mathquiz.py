import random
import time

print('\nBienvenido a Sapien, el juego de trivia matematica\n')

#from jug import Jugador
from gral import TABLA_OPERACIONES as TABLA, PLAYER_LIST as PL, Jugador
from game_conditions import Conditions, c, set_conditions


set_conditions()
This_Game = Conditions( int(c[0]) , int(c[1]) )
print(This_Game)


def Sapien(p):
    select = random.choice( list( TABLA.keys() ) )
    key_operation = str(select)
    
    print(f'\n\n\n\nRONDA *nro de ronda* \nJUGADOR {p.nombre},'), time.sleep(1), print(f'dada la siguiente operacion: ')
    print(f'{select}')
    #print( TABLA[select] ) # DEBUG -> arroja el resultado :D
    
    respuesta = input('\nIngrese respuesta en numeros enteros: ')   # respuesta del usuario tras seleccion de operacion matematica aleatoria
    
    time.sleep(0.5)
    
    try: 
        TABLA[select]  != int(respuesta)
    except:
        print('RESPUESTA INCORRECTA!\n\n\n')
        p.puntos -= 1
        p.errores.append(f' xxx {select} = {(respuesta)} xxx')   # aniade los errores a la clase para mostrarlos al decidir ganador
    else:
        if TABLA[select]  != int(respuesta):
            print('RESPUESTA INCORRECTA!\n\n\n')
            p.puntos -= 1
            p.errores.append(f' xxx {select} = {int(respuesta)} xxx')   # aniade los errores a la clase para mostrarlos al decidir ganador
            
        else:
            print('Correcto!\n\n\n')
            p.aciertos += 1
            p.puntos += 2

    #print( len(TABLA) )    # DEBUG de tamanio de tabla
    TABLA.pop( key_operation )  # Elimina la opcion elegida por el sistema para evitar que haya dos opciones iguales
    #print( len(TABLA) )    # DEBUG de tamanio de tabla (debe ser -1 a linea 33)


for i in range(This_Game.q_players):    # crea clases en funcion de la cantidad de jugadores declarados
    i = Jugador( input( f'\nIngrese nombre para jugador {i+1}: '), 0, 0, [] )   # DEBUG -> i = Jugador( nombre=f'JUGADOR {i+1}' ), puntos=0, aciertos=0, errores=[] ) / creacion de clases con nombre personalizado
    PL.append( i )  # aniade la clase creada a la lista de jugadores
    # DEBUG / test de clase creada para Jugador 'i' -> print(f'{i.nombre}, PUNTOS {i.puntos}, ACIERTOS {i.aciertos}')

def GAME():     # Tras definicion de cantidad de jugadores y de rondas, proceden a generarse cuanta instancia de juego sea necesaria
    k = 0
    
    for j in PL:
        for g in range(This_Game.q_rounds):
            Sapien(j)
    while k in range(This_Game.q_players):
        k = int(k)
        print( PL[k] )
        k += 1
GAME()

def AND_THE_WINNER_IS():
    def msj(ganador):
        if WINNER != 'EMPATE!':
            print(f'WINNER ---> {ganador.upper()} \n\n')
        else:
            print('HUBO UN EMPATE! \n\n')
    base = -999
    for i in PL:
        if i.puntos == base:
            WINNER = 'EMPATE!'
        elif i.puntos > base:
            base = i.puntos
            WINNER = i.nombre
    msj(WINNER)
AND_THE_WINNER_IS()

for i in PL:
    if i.errores == []:
        print(f'Jugador {i.nombre} no tuvo errores!')
    else:
        print(f'Errores de {i.nombre}: {i.errores}')

time.sleep(5)
input('\n\nJuego Finalizado. \nIngrese cualquier tecla para finalizar\n')

'''
if input('Ingrese "Y" para volver a jugar o cualquier tecla para cerrar: ').upper() == 'Y':
    PL.clear()
    players = 2# int(input(f'Ingrese cantidad de jugadores: ' ))  # o poner un valor fijo de tipo INT
    rounds =  1#int(input(f'Ingrese cantidad de rondas: ' ))  # o poner un valor fijo de tipo INT
    TABLA = RESTOCK
    GAME()
'''