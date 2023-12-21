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
        if(int(opcion)==1):
            clear()
            intento = False
            cr.inicio.iniciar()
        elif(int(opcion)==2):
            clear()
            intento = False
            dd.inicio.iniciar()
        elif(int(opcion)==3):
            clear()
            intento = False
            jv.inicio.iniciar()
        elif(int(opcion)==0):
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
            opcion = input("Opcion: ")
    else:
        clear()
        print("Selecciona a que quieres jugar:")
        print("1. Tres en raya")
        print("2. Dragones y mazmorras")
        print("3. El juego de la vida")
        print("0. Salir")
        opcion = input("Opcion: ")