import dragones_mapa as dm
import os
import time

def clear(): return os.system('clear')
clear()

class inicio:
    def iniciar():

        verdad = True
        #Pasamos el alto y ancho de la mazmorra
        dm.MapGrid.heigth = input('Alto de la mazmorra: ')
        dm.MapGrid.width = input('Ancho de la mazmorra: ')
        dm.MapGrid.dificil = input('Selecciona la dificultad (1, 2, 3): ')

        while verdad:
            if(dm.MapGrid.heigth.isdigit() and dm.MapGrid.width.isdigit()):
                verdad=False
                #Mensaje de creacion
                clear()
                print("Generando mazmorra...")
                time.sleep(2)
                clear()

                #Convertimos los valores string a int
                alto = dm.MapGrid.heigth
                dm.MapGrid.heigth = int(alto)
                ancho = dm.MapGrid.width
                dm.MapGrid.width = int(ancho)

                #Dibujamos el mapa
                dm.MapGrid.draw_grid(dm.MapGrid)
                dm.MapGrid.get_walls(dm.MapGrid)

                #Para moverse por el mapa
                dm.MapGrid.move_player(dm.MapGrid)
            #Si el ancho y alto lo hemos introducido como no numerico
            else:
                clear()
                print("Introduce un valor numerico")
                time.sleep(1)
                clear()
                print("La dificultad es: ", dm.MapGrid.dificil)
                dm.MapGrid.heigth = input('Alto de la mazmorra: ')
                dm.MapGrid.width = input('Ancho de la mazmorra: ')