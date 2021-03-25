import random
import time

from jug import Jugador
from gral import TABLA_OPERACIONES as TABLA
from gral import PLAYER_LIST as PL

print('\nBienvenido a Sapien, el juego matematico\n')
players =  int(input(f'Ingrese cantidad de jugadores: ' )) # o poner un valor fijo de tipo INT
rounds =  int(input(f'Ingrese cantidad de rondas: ' )) # o poner un valor fijo de tipo INT
# round = 0 # NO OPERATIVO, contador de rounds

def Sapien(p):
    select = random.choice( list( TABLA.keys() ) )
    key_operation = str(select)
    
    print(f'\n\n\n\nJUGADOR {p.nombre},'), time.sleep(1), print(f'dada la siguiente operacion: ')
    print(f'\n{select}')
    #print( TABLA[select] ) # CHEAT, arroja el resultado :D
    
    respuesta = input('\nIngrese respuesta en numeros enteros: ') # respuesta del usuario tras seleccion de operacion matematica aleatoria
    
    if TABLA[select]  != int(respuesta) :
        print('RESPUESTA INCORRECTA!\n\n\n')
        p.puntos -= 1
        p.errores.append(f' xxx {select} = {int(respuesta)} xxx') # aniade los errores a la clase para mostrarlos al decidir ganador
        
    else:
        print('Correcto!\n\n\n')
        p.aciertos += 1
        p.puntos += 2
        
    #print( len(TABLA) ) # CHECK de tamanio de tabla
    TABLA.pop( key_operation ) # Elimina la opcion elegida por el sistema para evitar que haya dos opciones iguales
    #print( len(TABLA) ) # CHECK de tamanio de tabla (debe ser -1 a linea 33)
    # round += 1  # NO OPERATIVO, contador de round


for i in range(players):                                                      # crea clases en funcion de la cantidad de jugadores declarados
    i = Jugador( input( f'\nIngrese nombre para jugador {i+1}: '), 0, 0, [] ) # funcional: i = Jugador( input( f'\nIngrese nombre para jugador {i+1}: '), 0, 0, [] ) / creacion de clases con nombre personalizado
    PL.append( i )                                                   # aniade la clase creada a la lista de jugadores
    # print(f'{i.nombre}, PUNTOS {i.puntos}, ACIERTOS {i.aciertos}')          # verifica creacion de clase con nombre de jugador X

def GAME():
    k = 0
    
    for j in PL:
        for g in range(int(rounds)):
            Sapien(j)
    while k in range(players):
        k = int(k)
        print( PL[k] )
        k += 1
GAME()

def AND_THE_WINNER_IS():
    def msj(ganador):
        print(f'WINNER ---> {ganador}\n')
    base = -999
    for i in PL:
        if i.puntos > base:
            base = i.puntos
            WINNER = i.nombre
    msj(WINNER)
AND_THE_WINNER_IS()

for i in PL:
    if i.errores == []:
        print(f'Jugador {i.nombre} no tuvo errores!')
    else:
        print(f'Errores de {i.nombre}: {i.errores}')


input('Ingrese cualquier tecla para cerrar: ')
