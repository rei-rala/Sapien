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