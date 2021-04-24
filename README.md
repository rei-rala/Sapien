"# Sapien" 

Juego donde X cantidad de juegadores en Y rondas (editable por usuario al principio de ejecucion) se ponen a prueba para responder operaciones matematicas simples (sean +, -, / o *) de 2 terminos. 


Changelog:

v1.0.0:  
        Creacion del juego 'mathquiz.py',  
        Clases para jugadores 'jug.py'  
          


v1.1.0:  
        Modulo 'gral.py' para algunas condiciones como la tabla de operaciones,  
        Ampliacion de tabla de operaciones (seleccion de operaciones a evaluar),  
        Tras finalizar cada ronda, se elimina la operacion evaluada de la tabla de operaciones,  
        Aniadido 'mathquiz_t.py' como dummy de versiones de pruebas  

  

v1.1.1:  
Aniadido caso de juego terminado en EMPATE (solo apto 2 jugadores)  

  
  
v1.1.2:  
Aniadido .gitignore  
  


v1.1.3:  
Se traslado la clase Jugador al modulo gral.py y se elimino el modulo jug.py,   
Se corrigio errores al hacer input de valores invalidos (jugadores, rounds y respuesta a operaciones)  
          


v1.1.4:  
        codigo simplificado,  
        aniadido contador de rounds,  
        aniadido clear() de terminal para claridad,  
        incorporacion y aumento de diferentes timers,  
        incorporacion de color de fuente,  
        cambios en modulos: tabla.py solo almacenta diccionario de operaciones, gral.py almacena diferentes variables y metodos de flujo,  
        Correcion de errores menores  
          



16/04/2021  
v1.1.5:   
        Incorporacion de logger (ingresar debug o si al principio de la ejecucion),  
        Mensajes debug/info,  
        mathquiz.py reducido,  
        Codigo simplificado,  
        Correcion de errores menores  
          
  

24/04/2021  
v1.2b:  
        Incorporado GUI inicial con Pygame  (Homescreen beta)  

v1.2.1b:  

        Relocalizacion de variables varias (materials)

# incoming: 
##               Falta dialogo de confirmacion de seteo de jugadores/rounds
##               Agregar funcionalidad para comenzar un nuevo juego tras finalizar