import os
import time
import Funcion_raya as funR

#Funcion para limpiar la pantalla
clear = lambda: os.system('clear')
clear()

class inicio:
    def iniciar():
        funR.Jugar
        #Array con diferentes posibilidades de aceptacion
        posibilidad = ["si", "true", "verdad", "vamos", "ok"]

        jugar = input("¿Quieres jugar al 3 en raya?\n")

        #Comprobamos si el texto introducido esta en las posibilidades
        if(posibilidad.count(jugar.lower())>=1):
            continuar = True
            while continuar:
                time.sleep(1)
                clear()
                jugar = input("¿Contra maquina o persona?\n")

                #Si queremos jugar contra la maquina
                if(jugar.lower() == "maquina"):
                    funR.Jugar().partidaMaquina()
                    continuar=False

                #Si queremos jugar contra otra persona
                elif(jugar.lower() == "persona"):
                    funR.Jugar().partidaPersona()
                    continuar=False

                #Si queremos salir
                elif(jugar.lower() == "salir"):
                    print("Adios")
                    continuar=False
                    time.sleep(1)
                    clear()
                    exit()
                
                #Si hemos introducido un texto diferente volvemos
                else:
                    print("Introduce otra opcion")
        else:
            print("Ok")
            time.sleep(1)
            clear()
            exit()