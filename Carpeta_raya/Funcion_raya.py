import os
import time
import random
import numpy as np
import Carpeta_raya.Tres_en_raya as tresRaya

clear = lambda: os.system('clear')
clear()

class Jugar:
    def __init__(self):
        self.victorias1 = 0
        self.victorias2 = 0
        self.grafico = 0
        pass

    def partidaPersona(self, graficoP):
        time.sleep(1)
        clear()
        print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
        print("___________")
        print("")
        print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
        print("___________")
        print("")
        print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
        turnos = 0
        correcto = True
        pieza1 = ""
        pieza2 = ""
        while correcto:
            pieza = input("Pieza del primer jugador: X o 0\n")
            if(pieza=="X" or pieza=="0"):
                pieza1 = pieza
                if(pieza=="X"):
                    pieza2 = "0"
                else:
                    pieza2 = "X"
                correcto=False
            else:
                print("Pieza incorrecta")
        while turnos<9:
            valor1 = input("Selecciona la posicion del jugador 1:\n")
            if(valor1.isnumeric()):
                valor1Int = int(valor1)
                valorCam = valor1Int
                valor1Int = Jugar.cambio(valor1Int)
                if(valorCam>9 or valorCam<1):
                    print("No puedes salirte del cuadrado")
                elif(graficoP[valor1Int]=="X" or graficoP[valor1Int]=="0"):
                    print("Selecciona un espacio vacio")
                    time.sleep(1)
                    clear()
                else:
                    graficoP[valor1Int] = "a"
                    graficoP[np.where(graficoP=="a")[0]] = pieza1
                    time.sleep(1)
                    clear()
                    print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                    print("___________")
                    print("")
                    print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                    print("___________")
                    print("")
                    print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
                    victoria = Jugar.victoria(graficoP, ficha=pieza1)
                    if(victoria=="Victoria"):
                        print("El jugador 1 ha ganado, despues de ",turnos+1," turnos")
                        val = input("¿Quieres jugar otra partida?\n")
                        if(val.lower()=="si"):
                            self.victorias1 = self.victorias1+1
                            tresRaya.inicio
                        exit()
            elif(valor1.lower() == "tablas"):
                print("Tablas solicitadas...")
                aceptar=input("¿Aceptar tablas?\n")
                posibilidad = ["si", "true", "verdad", "por supuesto"]
                if(posibilidad.count(aceptar.lower())):
                    print("Tablas aceptadas, empate")
                    exit()
                else:
                    print("Tablas no aceptadas")
                    time.sleep(1)
                    clear()
                    print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                    print("___________")
                    print("")
                    print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                    print("___________")
                    print("")
                    print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
            else:
                time.sleep(1)
                clear()
                print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                print("___________")
                print("")
                print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                print("___________")
                print("")
                print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
            
            valor2 = input("Selecciona la posicion del jugador 2:\n")
            if(valor2.isnumeric()):
                valor2Int = int(valor2)
                valorCam = valor2Int
                valor2Int = Jugar.cambio(valor2Int)
                if(valorCam>9 or valorCam<1):
                    print("No puedes salirte del cuadrado")
                elif(graficoP[valor2Int]=="X" or graficoP[valor2Int]=="0"):
                    print("Selecciona un espacio vacio")
                    time.sleep(1)
                    clear()
                else:
                    graficoP[valor2Int] = "a"
                    graficoP[np.where(graficoP=="a")[0]] = pieza2
                    time.sleep(1)
                    clear()
                    print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                    print("___________")
                    print("")
                    print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                    print("___________")
                    print("")
                    print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
                    victoria = Jugar.victoria(graficoP, ficha=pieza2)
                    if(victoria=="Victoria"):
                        print("El jugador 2 ha ganado, despues de ",turnos+1," turnos")
                        self.victorias2 = self.victorias2+1
                        exit()
            elif(valor1.lower() == "tablas"):
                print("Tablas solicitadas...")
                aceptar=input("¿Aceptar tablas?\n")
                posibilidad = ["si", "true", "verdad", "por supuesto"]
                if(posibilidad.count(aceptar.lower())):
                    print("Tablas aceptadas, empate")
                    exit()
                else:
                    print("Tablas no aceptadas")
                    time.sleep(1)
                    clear()
                    print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                    print("___________")
                    print("")
                    print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                    print("___________")
                    print("")
                    print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
            else:
                time.sleep(1)
                clear()
                print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                print("___________")
                print("")
                print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                print("___________")
                print("")
                print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")

            turnos+=1

    def cambio(posicion):
        if(posicion==7):
            return 0
        elif(posicion==8):
            return 1
        elif(posicion==9):
            return 2
        elif(posicion==4):
            return 3
        elif(posicion==5):
            return 4
        elif(posicion==6):
            return 5
        elif(posicion==1):
            return 6
        elif(posicion==2):
            return 7
        elif(posicion==3):
            return 8
        

    def victoria(grafico, ficha):
        fin = "no"
        if(grafico[0]==ficha and grafico[3]==ficha and grafico[6]==ficha):
            fin="Victoria"
        elif(grafico[1]==ficha and grafico[4]==ficha and grafico[7]==ficha):
            fin="Victoria"
        elif(grafico[2]==ficha and grafico[5]==ficha and grafico[8]==ficha):
            fin="Victoria"
        elif(grafico[0]==ficha and grafico[1]==ficha and grafico[2]==ficha):
            fin="Victoria"
        elif(grafico[3]==ficha and grafico[4]==ficha and grafico[5]==ficha):
            fin="Victoria"
        elif(grafico[6]==ficha and grafico[7]==ficha and grafico[8]==ficha):
            fin="Victoria"
        elif(grafico[0]==ficha and grafico[4]==ficha and grafico[8]==ficha):
            fin="Victoria"
        elif(grafico[6]==ficha and grafico[4]==ficha and grafico[2]==ficha):
            fin="Victoria"
        return fin

    def partidaMaquina(self, graficoP):
        turnos = 0
        while turnos<9:
            time.sleep(1)
            clear()
            print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
            print("___________")
            print("")
            print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
            print("___________")
            print("")
            print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
            valorC = input("Selecciona la posicion:\n")
            if(valorC.isnumeric()):
                valorCInt = int(valorC)
                valorCam = valorCInt
                valorCInt = Jugar.cambio(valorCInt)
                if(valorCam>9 or valorCam<1):
                    print("No puedes salirte del cuadrado")
                elif(graficoP[valorCInt]=="X" or graficoP[valorCInt]=="0"):
                    print("Selecciona un espacio vacio")
                    time.sleep(1)
                    clear()
                else:
                    graficoP[valorCInt] = "a"
                    graficoP[np.where(graficoP=="a")[0]] = "X"
                    time.sleep(1)
                    clear()
                    print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                    print("___________")
                    print("")
                    print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                    print("___________")
                    print("")
                    print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
                    victoria = Jugar.victoria(graficoP, ficha="X")
                    turnos+=1

                    if(victoria=="no"):
                        aceptado = True
                        while aceptado:
                            bot = random.randint(0,8)
                            if(graficoP[bot]=="X" or graficoP[bot]=="0"):
                                bot = random.randint(0,8)
                            else:
                                aceptado=False
                        graficoP[bot] = "0"
                        time.sleep(1)
                        clear()
                        print("",graficoP[0],"|",graficoP[1],"|",graficoP[2],"")
                        print("___________")
                        print("")
                        print("",graficoP[3],"|",graficoP[4],"|",graficoP[5],"")
                        print("___________")
                        print("")
                        print("",graficoP[6],"|",graficoP[7],"|",graficoP[8],"")
                        victoria = Jugar.victoria(graficoP, ficha="0")
                        turnos+=1
                        if(victoria=="Victoria"):
                            print("Has perdido, despues de ",turnos+1," turnos")
                            break
                    else:
                        print("Has ganado, despues de ",turnos+1," turnos")
                        break
            elif(valorC.lower() == "tablas"):
                print("Tablas solicitadas...")
                time.sleep(1)
                clear()
                posible = random.randint(0,1)
                if(posible==1):
                    print("Tablas aceptadas, empate")
                    exit()
                else:
                    print("Tablas no aceptadas")
            else:
                time.sleep(1)
                clear()