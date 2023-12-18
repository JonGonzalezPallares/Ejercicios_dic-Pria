import os
import numpy as np
import random as rd

def clear(): return os.system('clear')

class LifeGame:
    def __init__(self):
        self.width = 20
        self.heigth = 20
        self.grafico = 0
        self.antiguo = 0

    #Funcion para generar el grafico
    def dib_grafico(self):
        self.grafico = np.full((self.heigth, self.width), fill_value="🟥 ")
        self.antiguo = np.full((self.heigth, self.width), fill_value=". ")

    #Funcion para recoguer las vivas
    def get_vivas(self):
        #Para saber cuantas casillas vivas va a haber 
        vivx = round(((self.width)*(self.heigth))/4)

        bloques = [[]]*vivx
        for paso in range(vivx):
            prob = True
            while prob:
                dif=0

                #Posicion aleatoria para la casilla de "viva"
                ancho = rd.randint(0, self.width-1)
                alto = rd.randint(0, self.heigth-1)
                ar = [alto, ancho]

                #Contador para saber si la posicion del random no esta en el array
                for paso2 in range(len(bloques)):
                    if(bloques[paso2] != ar):
                        dif = dif+1

                #Si no esta en el array lo introduce, si no, vuelve a generar otra posicion
                if(dif==len(bloques)):
                    bloques[paso] = ar
                    prob=False
                    
            #Añadimos el emoji de muro en las posiciones
            self.grafico[alto][ancho] = "🟩 "

    #Funcion para dibujar el grafico
    def pintar(self):
        if((self.antiguo==self.grafico).all()):
            #Para printar el grafico
            for alto in range(self.heigth):
                print("\n")
                for ancho in range(self.width):
                    if(self.grafico[alto][ancho]=="🟩 "):
                        print(f"{self.grafico[alto][ancho]}", end=" ")
                    elif(self.grafico[alto][ancho]=="🟥 "):
                        print(f"{self.grafico[alto][ancho]}", end=" ")
                    else:
                        print(self.grafico[alto][ancho], end=" ")
            print("\n")
            exit()
        else:
            #Para printar el grafico
            for alto in range(self.heigth):
                print("\n")
                for ancho in range(self.width):
                    if(self.grafico[alto][ancho]=="🟩 "):
                        print(f"{self.grafico[alto][ancho]}", end=" ")
                    elif(self.grafico[alto][ancho]=="🟥 "):
                        print(f"{self.grafico[alto][ancho]}", end=" ")
                    else:
                        print(self.grafico[alto][ancho], end=" ")
            print("\n")

    #Funcion para saber si los de alrededor estan vivas
    def comprobacion(self):
        nuevoGraf = np.full((self.heigth, self.width), fill_value="🟥 ")
        for alto in range(self.heigth):
            for ancho in range(self.width):
                contador=0
                #print("Pos: ", alto, ancho)

                #Comprobacion de la caja de arriba a la izquierda
                if(ancho-1>=0):
                    if(alto-1>=0):
                        if(self.grafico[alto-1][ancho-1]=="🟩 "):
                            contador = contador + 1
                            #print("ArI VIVA")
                            #print(contador)
                        #print("Arriba izq, ancho:", ancho-1, "alto:", alto-1)
     
                #Comprobacion arriba medio
                if(alto-1>=0):
                    if(self.grafico[alto-1][ancho]=="🟩 "):
                        contador = contador + 1
                        #print("ArM VIVA")
                        #print(contador)
                    #print("Arriba med, ancho:", ancho, "alto:", alto+1)
    
                #Comprobacion arriba derecha
                if(ancho+1<self.width):
                    if(alto-1>=0):
                        if(self.grafico[alto-1][ancho+1]=="🟩 "):
                            contador = contador + 1
                            #print("ArD VIVA")
                            #print(contador)
                        #print("Arriba der, ancho:", ancho+1, "alto:", alto-1)

                #Comprobacion medio izquierda
                if(ancho-1>=0):
                    if(self.grafico[alto][ancho-1]=="🟩 "):
                        contador = contador + 1
                        #print("MeI VIVA")
                        #print(contador)
                    #print("Medio izq, ancho:", ancho-1, "alto:", alto)
                        
                #Comprobacion medio derecha
                if(ancho+1<self.width):
                    if(self.grafico[alto][ancho+1]=="🟩 "):
                        contador = contador + 1
                        #print("MeD VIVA")
                        #print(contador)
                    #print("Medio der, ancho:", ancho+1, "alto:", alto)
                        
                #Comprobacion de abajo izquierda
                if(ancho-1>=0):
                    if(alto+1<self.heigth):
                        if(self.grafico[alto+1][ancho-1]=="🟩 "):
                            contador = contador + 1
                            #print("AbI VIVA")
                            #print(contador)
                        #print("Abajo izq, ancho:", ancho-1, "alto:", alto+1)

                #Comprobacion abajo medio
                if(alto+1<self.heigth):
                    if(self.grafico[alto+1][ancho]=="🟩 "):
                        contador = contador + 1
                        #print("AbM VIVA")
                        #print(contador)
                    #print("Abajo medio, ancho:", ancho, "alto:", alto+1)

                #Comprobacion abajo derecha
                if(ancho+1<self.width):
                    if(alto+1<self.heigth):
                        if(self.grafico[alto+1][ancho+1]=="🟩 "):
                            contador = contador + 1
                            #print("AbD VIVA")
                            #print(contador)
                        #print("Abajo der, ancho:", ancho+1, "alto:", alto+1)  

                
                #Si el bloque en el que estamos esta vivo
                if(self.grafico[alto][ancho]=="🟩 "):
                    #Si tiene dos o menos vivas; o mas de tres, muere
                    if(contador<2 or contador>3):
                        #print("ha muerto")
                        nuevoGraf[alto][ancho]="🟥 "

                #Si el bloque en el que estamos esta muerto
                if(self.grafico[alto][ancho]=="🟥 "):
                    #Si tiene tres vivas, revive
                    if(contador>=3):
                        nuevoGraf[alto][ancho]="🟩 "

        for alto in range(self.heigth):
            for ancho in range(self.width):
                self.antiguo[alto][ancho]=self.grafico[alto][ancho]
                self.grafico[alto][ancho]=nuevoGraf[alto][ancho]