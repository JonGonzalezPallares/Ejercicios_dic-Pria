import numpy as np
import random as rd
import os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def clear(): return os.system('clear')

class MapGrid:
    def __init__(self):
        self.width = 10
        self.heigth = 10
        self.grafico = ""

    def draw_grid(self):
        self.grafico = np.full((self.heigth, self.width), fill_value=".")

    def get_walls(self, porcentaje=0.3):
        num = round((self.width*self.heigth*porcentaje)/2)
        numerosRan = [[]]*num
        for paso in range(num):
            prob = True
            while prob:
                dif = 0
                ancho = rd.randint(0, self.width-1)
                alto = rd.randint(0, self.heigth-1)
                ar = [alto, ancho]

                #Si los numeros aleatorios no son ni el inicio ni el final
                if(ar != [0,0] and ar != [self.width-1, self.heigth-1]):
                    #Contador para saber si la posicion del random no esta en el array
                    for paso2 in range(len(numerosRan)):
                        if(numerosRan[paso2] != ar):
                            dif = dif + 1

                    #Si no esta en el array lo introduce, si no, vuelve a generar otra posicion
                    if(dif==len(numerosRan)):
                        numerosRan[paso] = ar
                        prob=False
                    else:
                        prob=True
                    
            self.grafico[alto][ancho] = "#"
        #Colocamos al jugador y el final de la mazmorra
        self.grafico[0][0]="$"
        self.grafico[self.heigth-1][self.width-1]=">"

        #Para printar el grafico
        for alto in range(self.heigth):
            print("\n")
            for ancho in range(self.width):
                if(self.grafico[alto][ancho]=="$"):
                    print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                elif(self.grafico[alto][ancho]=="#"):
                    print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                else:
                    print(self.grafico[alto][ancho], end=" ")
        print("\n")

    def move_player(self):
        #El primero es el movimiento hacia abajo/arriba, el segundo hacia la derecha e izquierda
        inicio = [0,0]
        movimiento = True
        while movimiento:
            casilla = input("Movimiento: w, a, s, d:\n")

            #Si hemos pulsado para ir a la derecha
            if(casilla == "d"):
                if(inicio[1]+1!=self.width and self.grafico[inicio[0]][inicio[1]+1]!="#"):
                    if(self.grafico[inicio[0]][inicio[1]+1] == ">"):
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="$"):
                                    print(".", end=" ")
                                elif(self.grafico[alto][ancho]==">"):
                                    print(f"{Fore.GREEN}${Style.RESET_ALL}", end=" ")
                                elif(self.grafico[alto][ancho]=="#"):
                                    print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")  
                        print("MAZMORRA COMPLETADA")
                        exit()
                    else:
                        self.grafico[inicio[0]][inicio[1]] = "."
                        self.grafico[0][0] = "<"
                        inicio[1] = inicio[1]+1
                        self.grafico[inicio[0]][inicio[1]] = "$"
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="$"):
                                    print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                elif(self.grafico[alto][ancho]=="#"):
                                    print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")
                else:
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")


            #Si hemos pulsado para ir a la izquierda
            elif(casilla == "a"):
                if(inicio[1]-1>=0 and self.grafico[inicio[0]][inicio[1]-1]!="#"):
                    self.grafico[inicio[0]][inicio[1]] = "."
                    inicio[1] = inicio[1]-1
                    self.grafico[inicio[0]][inicio[1]] = "$"
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
                else:
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")


            #Si hemos pulsado para ir hacia arriba
            elif(casilla == "w"):
                if(inicio[0]-1>=0 and self.grafico[inicio[0]-1][inicio[1]]!="#"):
                    self.grafico[inicio[0]][inicio[1]] = "."
                    inicio[0] = inicio[0]-1
                    self.grafico[inicio[0]][inicio[1]] = "$"
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
                else:
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
                    

            #Si hemos pulsado para ir abajo            
            elif(casilla == "s"):
                if(inicio[0]+1!=self.heigth and self.grafico[inicio[0]+1][inicio[1]]!="#"):
                    if(self.grafico[inicio[0]+1][inicio[1]] == ">"):
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="$"):
                                    print(".", end=" ")
                                elif(self.grafico[alto][ancho]==">"):
                                    print(f"{Fore.GREEN}${Style.RESET_ALL}", end=" ")
                                elif(self.grafico[alto][ancho]=="#"):
                                    print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")  
                        print("MAZMORRA COMPLETADA")
                        exit()
                    else:
                        self.grafico[inicio[0]][inicio[1]] = "."
                        self.grafico[0][0] = "<"
                        inicio[0] = inicio[0]+1
                        self.grafico[inicio[0]][inicio[1]] = "$"
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="$"):
                                    print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                elif(self.grafico[alto][ancho]=="#"):
                                    print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")  
                else:
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="$"):
                                print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            elif(self.grafico[alto][ancho]=="#"):
                                print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")


            else:
                clear()
                #Para printar el grafico
                for alto in range(self.heigth):
                    print("\n")
                    for ancho in range(self.width):
                        if(self.grafico[alto][ancho]=="$"):
                            print(f"{Fore.GREEN}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                        elif(self.grafico[alto][ancho]=="#"):
                            print(f"{Fore.BLUE}{self.grafico[alto][ancho]}{Style.RESET_ALL}", end=" ")
                        else:
                            print(self.grafico[alto][ancho], end=" ")
                print("\n")  

            print(inicio)