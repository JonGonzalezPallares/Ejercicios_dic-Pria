# Archivo => Inicio.py
Para que se pueda jugar a cualquier juego, hay que arrancar este, ya que es un menu desde el que se puede acceder al resto de juegos. Si se intenta iniciar algun juego por si mismo no va a funcionar (seguramente)

# Ejercicios varios
Ejercicios realizados en python para entrenar con arrays y diferentes apartados


# Carpeta_raya
El juego de tres en raya. Contiene dos archivos python diferentes

- Tres_en_raya.py
  Mostrar el menu de seleccion, teniendo la posibilidad de salir, jugar contra otro jugador o jugar contra el ordenador
  
- Funcion_raya.py
  Genera la tabla para poder ver mejor el tablero
  Tambien contiene una funcion para limpiar la consola cada vez que se toma una decision, para que no se llene toda la consola
  Luego tiene las funciones de comprobacion, para saber quien gana, y la parte de el ordenador


# Dungeons_and_dragons
El juego de dragones y mazmorras, dungeons & dragons o D&D, como se prefiera llamar. Contiene dos archivos python diferentes

- dragones_juego.py
  Genera el mapa con el alto y ancho proporcionado
  Segun la dificultad que se le haya especificado se generaran mas peligros o menos
  
- dragones_mapa.py
  Contiene una funcion para generar los muros, segun la dificultad habra mas o menos
  Si la dificultad seleccionada es 3, se generaran llamas a lo largo del campo para complicar las cosas
  Contiene una funcion para mover al dragon por el tablero cada vez que nosotros nos movamos
  * Posible mejora: que el dragon se este moviendo siempre y no solo cuando nosotros lo hagamos
  Contiene una funcion para mover al personaje por el tablero
  * Posible mejora: que el personaje se mueva automaticamente al introducir la tecla, por que por ahora hay que introducir y pulsar enter
  Se cambian las imagenes de: el dragon, el personaje, la princesa, el castillo, el fuego, la victoria y el muro
    Asi pasando de ser caracteres a emoticonos


# Juego_de_la_vida
El juego de la vida del matematico John Horton Conway, contiene dos archivos python

- juego_vida.py
  Se solicita el tamaño del tablero para el juego
  Se dibuja el grafico siempre que se pueda
  
- juego_vida_mapa.py
  Generamos el grafico y obtenemos, sabiendo el tamaño de la caja, cuantas celulas vivas va a haber al empezar. Despues se añaden a la caja en posiciones aleatorias
  Contiene una funcion que va a estar comprobando los alrededores de las celulas vivas, para ver si mueren o continuan. Si la caja ha estado dos "pasadas" igual, el juego
    para por que ha llegado un momento en el que no va a haber mas cambios, a menos que entren nuevas celulas


