import random
import time
from jug import Jugador

print('\nBienvenido a Sapien, el juego matematico\n')
players = int(input(f'Ingrese cantidad de jugadores: ' )) # o poner un valor fijo de tipo INT
PLAYER_LIST = []
rounds = int(input(f'Ingrese cantidad de rondas: ' )) # o poner un valor fijo de tipo INT
round = 0
def Sapien(p):
    TABLA_OPERACIONES = {
    '3+436'   : 3+436,
    '3+1'     : 3+1,
    '12*2'    : 12*2,
    '436/2'   : 436/2,
    '3849+1'  : 3849+1,
    '98+888'  : 98+888,
    '88+22+1' : 88+22+1,
    '13/13'   : 13/13,
    '1+1'     : 1+1,
    '33+36'   : 33+36,
    '100-9'   : 100-9 ,
    '123+66'  : 123+66 ,
    '456+1'   : 456+1 ,
    '555+55'  : 555+55 ,
    '321-123' : 321-123 ,
    '5*25'    : 5*25 ,
    '99+4'    : 99+4 ,
    '1+9999'  : 1+9999 ,
    '32*4'    : 32*4 ,
    '5*22'    : 5*22 ,
    '1*121'   : 1*121 ,
    '66+0'    : 66+0 ,
    '3*11'    : 3*11 ,
    '99/3'    : 99/3 ,
    '100/20'  : 100/20 ,
    '33/33'   : 33/33 ,
    '1000-2'  : 1000-2     
    }
    
    select = random.choice( list( TABLA_OPERACIONES.keys() ) )
    
    print(f'\n\n\n\nJUGADOR {p.nombre},'), time.sleep(1), print(f'dada la siguiente operacion: ')
    print(f'\n{select}')
    #print( TABLA_OPERACIONES[select] ) # CHEAT, arroja el resultado :D
    
    respuesta = input('\nIngrese respuesta en numeros enteros: ') # respuesta del usuario tras seleccion de operacion matematica aleatoria
    
    if TABLA_OPERACIONES[select]  != int(respuesta) :
        print('RESPUESTA INCORRECTA!\n\n\n')
        p.puntos -= 1
        p.errores.append(f' xxx {select} = {int(respuesta)} xxx') # aniade los errores a la clase para mostrarlos al decidir ganador
    else:
        print('Correcto!\n\n\n')
        p.aciertos += 1
        p.puntos += 2
    TABLA_OPERACIONES.pop(select)
    round += 1


for i in range(players):                                                      # crea clases en funcion de la cantidad de jugadores declarados
    i = Jugador( input( f'\nIngrese nombre para jugador {i+1}: '), 0, 0, [] ) # creacion de clases con nombre personalizado
    PLAYER_LIST.append( i )                                                   # aniade la clase creada a la lista de jugadores
    # print(f'{i.nombre}, PUNTOS {i.puntos}, ACIERTOS {i.aciertos}')          # verifica creacion de clase con nombre de jugador X

def GAME():
    k = 0
    
    for j in PLAYER_LIST:
        for g in range(int(rounds)):
            round = 0
            Sapien(j)
    while k in range(players):
        k = int(k)
        print( PLAYER_LIST[k] )
        k += 1
GAME()

def AND_THE_WINNER_IS():
    def msj(ganador):
        print(f'WINNER ---> {ganador}\n')
    base = -999
    for i in PLAYER_LIST:
        if i.puntos > base:
            base = i.puntos
            WINNER = i.nombre
    msj(WINNER)
AND_THE_WINNER_IS()

for i in PLAYER_LIST:
    if i.errores == []:
        print(f'Jugador {i.nombre} no tuvo errores!')
    else:
        print(f'Errores de {i.nombre}: {i.errores}')


input('Ingrese cualquier tecla para cerrar: ')
