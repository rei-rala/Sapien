# RESTOCK y TABLA_OPERACIONES DEBEN MODIFICARSE EN SIMULTANEO
TABLA_OPERACIONES = {'3+436'   : 3+436,
'3+1'     : 3+1 ,
'12*2'    : 12*2 ,
'436/2'   : 436/2 ,
'3849+1'  : 3849+1 ,
'98+888'  : 98+888 ,
'88+22+1' : 88+22+1 ,
'13/13'   : 13/13 ,
'1+1'     : 1+1 ,
'33+36'   : 33+36 ,
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
'1000-2'  : 1000-2 ,
'31+99'   : 31+99 ,
'50-42'   : 50-42,
'1000/5 ' : 1000/5 ,
'3*21'    : 3*21  ,
'66/11'   : 66/11 ,
'115+115' : 115+115 ,
'31-15'   : 31-15 ,
'55*3'    : 55*3 ,
'120/3'   : 120/3 ,
'1234+766': 1234+766 ,
'0*400'   : 0*400 ,
'225/25'  : 225/25,
'100-31'  : 100-31,
}

# RESTOCK y TABLA_OPERACIONES DEBEN MODIFICARSE EN SIMULTANEO
RESTOCK = {'3+436'   : 3+436,
'3+1'     : 3+1 ,
'12*2'    : 12*2 ,
'436/2'   : 436/2 ,
'3849+1'  : 3849+1 ,
'98+888'  : 98+888 ,
'88+22+1' : 88+22+1 ,
'13/13'   : 13/13 ,
'1+1'     : 1+1 ,
'33+36'   : 33+36 ,
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
'1000-2'  : 1000-2 ,
'31+99'   : 31+99 ,
'50-42'   : 50-42,
'1000/5 ' : 1000/5 ,
'3*21'    : 3*21  ,
'66/11'   : 66/11 ,
'115+115' : 115+115 ,
'31-15'   : 31-15 ,
'55*3'    : 55*3 ,
'120/3'   : 120/3 ,
'1234+766': 1234+766 ,
'0*400'   : 0*400 ,
'225/25'  : 225/25,
'100-31'  : 100-31,
}


PLAYER_LIST = []
CURRENTLY_PLAYING = ''
ROUND = 1

class Jugador:
    def __init__(self, nombre, puntos, aciertos, errores):
        self.nombre = nombre
        self.puntos = puntos
        self.aciertos = aciertos
        self.errores = errores
    
    def __str__(self):
        return f' {self.nombre}, puntos {self.puntos} con {self.aciertos} aciertos'



# TESTEO DE CLASE Jugador
'''
j1 = Jugador('mamerto', -10,2, [] )
j2 = Jugador('lalarto', -100,1,[] )
j3 = Jugador('soreto', -3,3, [])

l1 = [ j1 , j2 , j3 ]

base = -999
for i in l1:
    if i.puntos > base:
        base = i.puntos
        WINNER = i.nombre

j3.errores.append('rip')
j3.errores.append('ah por que veia esto')

for i in l1:
    print(f'Errores de {i.nombre} {i.errores}')


print(WINNER)

#print( l1[2].nombre)  # seleccion de nombre especifico dentro de la lista donde [VALOR] referiria al valor de iteracion
'''