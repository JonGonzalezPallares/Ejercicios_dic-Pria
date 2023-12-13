import dragones_mapa as dm
import os
import time

def clear(): return os.system('clear')
clear()

#Pasamos el alto y ancho de la mazmorra
dm.MapGrid.heigth = int(input('Alto de la mazmorra: '))
dm.MapGrid.width = int(input('Ancho de la mazmorra: '))
dm.MapGrid.dificil = input('Selecciona la dificultad (1, 2, 3): ')

#Mensaje de creacion
clear()
print("Generando mazmorra...")
time.sleep(2)
clear()

#Dibujamos el mapa
dm.MapGrid.draw_grid(dm.MapGrid)
dm.MapGrid.get_walls(dm.MapGrid)

#Para moverse por el mapa
dm.MapGrid.move_player(dm.MapGrid)