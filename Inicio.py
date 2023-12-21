import Carpeta_raya.Tres_en_raya as cr
import Dungeons_and_dragons.dragones_juego as dd
import Juego_de_la_vida.juego_vida as jv
import os

print("¡Bienvenido!")

print("Selecciona a que quieres jugar:")
print("1. Tres en raya")
print("2. Dragones y mazmorras")
print("3. El juego de la vida")
print("0. Salir")

opcion = input("Opcion: ")
intento = True

#Funcion para limpiar la pantalla
def clear(): return os.system('clear')

while intento:
    if(opcion.isdigit()):
        if(opcion==1):
            intento = False
            cr.inicio()
        elif(opcion==2):
            intento = False
            dd.inicio()
        elif(opcion==3):
            intento = False
            jv.inicio()
        elif(opcion==0):
            intento = False
            clear()
            print("Adios")
            exit()
        else:
            clear()
            print("Selecciona a que quieres jugar:")
            print("1. Tres en raya")
            print("2. Dragones y mazmorras")
            print("3. El juego de la vida")
            print("0. Salir")
    else:
        clear()
        print("Selecciona a que quieres jugar:")
        print("1. Tres en raya")
        print("2. Dragones y mazmorras")
        print("3. El juego de la vida")
        print("0. Salir")