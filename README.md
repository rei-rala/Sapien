"# Sapien" 

Juego donde X cantidad de juegadores en Y rondas (editable por usuario al principio de ejecucion) se ponen a prueba para responder operaciones matematicas simples (sean +, -, / o *) de 2 terminos. 

Changelog:
v1.0.0: Creacion del juego 'mathquiz.py'
        Clases para jugadores 'jug.py'

v1.1.0: Modulo 'gral.py' para algunas condiciones como la tabla de operaciones
        Ampliacion de tabla de operaciones (seleccion de operaciones a evaluar)
        Tras finalizar cada ronda, se elimina la operacion evaluada de la tabla de operaciones
        Aniadido 'mathquiz_t.py' como dummy de versiones de pruebas

v1.1.1: Aniadido caso de juego terminado en EMPATE (solo apto 2 jugadores)

v1.1.2: Aniadido .gitignore

v1.1.3: Se traslado la clase Jugador al modulo gral.py y se elimino el modulo jug.py
        Se corrigio errores al hacer input de valores invalidos (jugadores, rounds y respuesta a operaciones)

# incoming: 
#            inicializa y setea una variable con la clase del jugador, se evalua si el valor de jugador de la ronda ACTUAL es el mismo que la ultima vez, 
#                -en caso negativo: setea una variable de ROUND en 0
#                -en caso positivo, ROUND +=1

