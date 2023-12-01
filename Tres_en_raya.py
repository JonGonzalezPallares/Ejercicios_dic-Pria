import os
import time
import numpy as np
import Funcion_raya as fr

clear = lambda: os.system('clear')
clear()

partida = fr.Jugar()

#esquema = np.array([["1","2","3"],["4","5","6"],["7","8","9"]])
esquema = np.array(["-","-","-","-","-","-","-","-","-"])
posibilidad = ["si", "true", "verdad", "vamos", "ok"]

jugar = input("¿Quieres jugar al 3 en raya?\n")
if(posibilidad.count(jugar.lower())>=1):
    continuar = True
    while continuar:
        time.sleep(1)
        clear()
        jugar = input("¿Contra maquina o persona?\n")
        if(jugar.lower() == "maquina"):
            partida.partidaMaquina(graficoP=esquema)
            continuar=False
        elif(jugar.lower() == "persona"):
            partida.partidaPersona(graficoP=esquema)
            continuar=False
        elif(jugar.lower() == "salir"):
            print("Adios")
            continuar=False
            time.sleep(1)
            clear()
            exit()
        else:
            print("Introduce otra opcion")
else:
    print("Ok")
    time.sleep(1)
    clear()
    exit()