import os
import time
import numpy as np
import Funcion_raya as funR

clear = lambda: os.system('clear')
clear()

class inicio:
    def iniciar():
        posibilidad = ["si", "true", "verdad", "vamos", "ok"]

        jugar = input("¿Quieres jugar al 3 en raya?\n")
        if(posibilidad.count(jugar.lower())>=1):
            continuar = True
            while continuar:
                time.sleep(1)
                clear()
                jugar = input("¿Contra maquina o persona?\n")
                if(jugar.lower() == "maquina"):
                    funR.Jugar().partidaMaquina()
                    continuar=False
                elif(jugar.lower() == "persona"):
                    funR.Jugar().partidaPersona()
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

inicio.iniciar()