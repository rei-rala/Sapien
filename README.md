"# Sapien" 

Si alguien esta leyendo esto, que sepa que no tengo idea de como hice algunas cosas en su momento (no imité ningun proyecto!!!), pero me agrada volver a ver lo que codeé tras conocer solo fundamentos de python. Claramente no voy a actualizar este jueguito para seguir analizando mi cabeza y como soy al encarar los problemas e implementar ideas que me fueron surgiendo (al menos 3 meses despues, todavía tengo los recuerdos frescos, mas aún de todo eso que no sé como hice funcionar y aquello que me rompió la cabeza al intentar realizar) . 
Puede que no sea la gran cosa, pero si lo fue para mi :)
-tener en cuenta que pygame solo aporta facilidades para crear la ventana, administrar eventos y realizar el render de 'cosas' en la misma.

Juego donde X cantidad de juegadores en Y rondas (editable por usuario al principio de ejecucion) se ponen a prueba para responder operaciones matematicas simples (sean +, -, / o *) de 2 terminos. 

# Ejecutar desde game.py :)

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
v1.2a:  
        Incorporado GUI inicial con Pygame  (Homescreen beta)  

v1.2.1a:  

        Relocalizacion de variables varias (materials)


v1.2.1a:  

        Renombrada versiones a alpha.
        Homescreen incluye sonidos, comportamiento de botones  
          
            
25/04/2021  
v1.2.2a:  

        Aniadido Sapien GUI hasta segmento de seleccion de cantidad de jugadores y rounds (inestable)  
          
            
27/04/2021  
v1.2.35a:  
        Mejorada estabilidad en seteo de cantidad de jugadores y cantidad de rounds  
        Sonidos aniadidos  
        Creadas funciones para animaciones in/out  
        Aniadido juego hasta creacion de nombres de jugadores (falta GUI)  

v1.2.5a:  
        Aniadido juego hasta segmento de pregunta-respuesta    
          
            
28/04/2021  
v1.5:  
        Juego completado!
        Esferas de respuesta randomizadas
        Factor aleatorio ajustado


# incoming:               
##               Cada jugador debe escojer un boton para su fondo mientras le toca turno
##               Agregar funcionalidad para comenzar un nuevo juego tras finalizar
##               Mucho lugar a mejora respecto a lo visual
##               
##               La aplicacion es inestable
##               Error conocido: puede haber dos jugadores con mismo nombre
##               Error conocido: ejecucion desordenada de sonidos
##               Error conocido: interrumpir animaciones hace la aplicacion inestable
