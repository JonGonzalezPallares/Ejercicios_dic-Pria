from Juego_de_la_vida import juego_vida_mapa as JV
import os
import time

def clear(): return os.system('clear')
clear()

class inicio:
    def iniciar():
        clear()

        JV.LifeGame.heigth = int(input("Alto del campo para el juego de la vida: "))
        JV.LifeGame.width = int(input("Ancho del campo para el juego de la vida: "))

        #Dibujamos el grafico con las casillas vivas
        JV.LifeGame.dib_grafico(JV.LifeGame)
        JV.LifeGame.get_vivas(JV.LifeGame)
        clear()

        while True:
            JV.LifeGame.pintar(JV.LifeGame)
            JV.LifeGame.comprobacion(JV.LifeGame)

            time.sleep(0.5)
            clear()