import juego_vida_mapa as JV
import os
import time

def clear(): return os.system('clear')

clear()

JV.LifeGame.heigth = int(input("Alto del campo para el juego de la vida: "))
JV.LifeGame.width = int(input("Ancho del campo para el juego de la vida: "))

#Dibujamos el grafico con las casillas vivas
JV.LifeGame.dib_grafico(JV.LifeGame)

for paso in range(2):
    JV.LifeGame.get_vivas(JV.LifeGame)
    JV.LifeGame.comprobacion(JV.LifeGame)

    time.sleep(2)
    paso=paso+1

#<2 muere, 2-3 vive, >3 muere; muerta=> 3 vivas revive