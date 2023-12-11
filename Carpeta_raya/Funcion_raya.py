import os
import time
import random
import numpy as np

#Funcion para limpiar la pantalla
def clear(): return os.system('clear')
clear()

class Jugar:
    def __init__(self):
        #Contador con las victorias del primer jugador
        self.victorias1 = 0
        #Contador con las victorias del segundo jugador
        self.victorias2 = 0
        #Para saber si hay que saltarse al primer jugador por texto incorrecto
        self.paso1 = False
        #Para saber si hay que saltarse al segundo jugador por texto incorrecto
        self.paso2 = False
        #Contador para la cantidad de tablas solicitadas
        self.countTabla = 0
        pass





    #Funcion para crear las tablas
    def crearTabla(graficoP):
        time.sleep(1)
        clear()
        print("", graficoP[0], "|", graficoP[1], "|", graficoP[2], "")
        print("___________")
        print("")
        print("", graficoP[3], "|", graficoP[4], "|", graficoP[5], "")
        print("___________")
        print("")
        print("", graficoP[6], "|", graficoP[7], "|", graficoP[8], "")





    #Funcion para jugar con otra persona
    def partidaPersona(self):
        #Array vacio para empezar
        graficoP = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"])
        #Contador de turnos
        turnos = 0
        correcto = True
        #Para saber las piezas de los jugadores
        pieza1 = ""
        pieza2 = ""

        Jugar.crearTabla(graficoP)
        
        #Para seleccionar la pieza del jugador
        while correcto:
            pieza = input("Pieza del primer jugador: X o 0\n")
            if (pieza.lower() == "x" or pieza == "0" or pieza.lower() == "o"):
                pieza1 = pieza
                if (pieza.lower() == "x" ):
                    pieza2 = "0"
                else:
                    pieza2 = "X"
                correcto = False
                Jugar.crearTabla(graficoP)
            else:
                Jugar.crearTabla(graficoP)
                print("Pieza incorrecta")
        
        #Mientras que tengamos turnos
        while turnos < 9:
            #Comprobamos si el otro jugador a metido mal para saltar el turno de este
            if (self.paso2 == True):
                self.paso2 = False
            else:
                valor1 = input("Selecciona la posicion del jugador 1 o solicita tablas:\n")
                #Si el texto es numerico
                if (valor1.isnumeric()):
                    valor1Int = int(valor1)
                    valorCam = valor1Int
                    valor1Int = Jugar.cambio(valor1Int)
                    #Comprobar que el valor no se sale del cuadrado
                    if (valorCam > 9 or valorCam < 1):
                        print("No puedes salirte del cuadrado")
                        self.paso1 = True
                    #Comprobamos si el espacio seleccionado esta vacio
                    elif (graficoP[valor1Int] == "X" or graficoP[valor1Int] == "0"):
                        self.paso1 = True
                        print("Selecciona un espacio vacio")
                        Jugar.crearTabla(graficoP)
                    else:
                        #Ponemos un valor por defecto para luego cambiarlo por la ficha del jugador
                        graficoP[valor1Int] = "a"
                        graficoP[np.where(graficoP == "a")[0]] = pieza1
                        Jugar.crearTabla(graficoP)
                        #Llamada a la funcion de comprobacion de victoria
                        victoria = Jugar.victoria(graficoP, ficha=pieza1)
                        #Si el jugador a ganado
                        if (victoria == "Victoria"):
                            print("El jugador 1 ha ganado, despues de ", turnos+1, " turnos")
                            val = input("¿Quieres jugar otra partida?\n")
                            self.victorias1 = self.victorias1+1
                            #Si se quiere volver a jugar o no
                            if (val.lower() == "si"):
                                self.countTabla = 0
                                self.partidaPersona()
                            else:
                                print("El jugador 1 ha ganado ", self.victorias1, " veces y el jugador 2 ", self.victorias2)
                                exit()
                #Comprobacion de tablas
                elif (valor1.lower() == "tablas"):
                    print("Tablas solicitadas...")
                    aceptar = input("¿Aceptar tablas?\n")
                    #Array con diferentes posibilidades de aceptacion
                    posibilidad = ["si", "true", "verdad", "por supuesto"]
                    #Comprobamos si el texto introducido esta en las posibilidades
                    if (posibilidad.count(aceptar.lower())):
                        print("Tablas aceptadas, empate")
                        exit()
                    #Si se solicitan demasiadas tablas
                    elif (self.countTabla == 2):
                        print("Demasiadas veces solicitadas tablas, el jugador 1 ha perdido")
                        exit()
                    else:
                        print("Tablas no aceptadas")
                        Jugar.crearTabla(graficoP)
                        self.countTabla = self.countTabla + 1
                else:
                    Jugar.crearTabla(graficoP)
                    self.paso1 = True
            


            #Comprobamos si el otro jugador a metido mal para saltar el turno de este
            if (self.paso1 == True):
                self.paso1 = False
            else:
                valor2 = input("Selecciona la posicion del jugador 2 o solicita tablas:\n")
                #Si el texto es numerico
                if (valor2.isnumeric()):
                    valor2Int = int(valor2)
                    valorCam = valor2Int
                    valor2Int = Jugar.cambio(valor2Int)
                    #Comprobar que el valor no se sale del cuadrado
                    if (valorCam > 9 or valorCam < 1):
                        print("No puedes salirte del cuadrado")
                        self.paso2 = True
                    #Comprobamos si el espacio seleccionado esta vacio
                    elif (graficoP[valor2Int] == "X" or graficoP[valor2Int] == "0"):
                        self.paso2 = True
                        print("Selecciona un espacio vacio")
                        Jugar.crearTabla(graficoP)
                    else:
                        #Ponemos un valor por defecto para luego cambiarlo por la ficha del jugador
                        graficoP[valor2Int] = "a"
                        graficoP[np.where(graficoP == "a")[0]] = pieza2
                        Jugar.crearTabla(graficoP)
                        #Llamada a la funcion de comprobacion de victoria
                        victoria = Jugar.victoria(graficoP, ficha=pieza2)
                        #Si el jugador a ganado
                        if (victoria == "Victoria"):
                            print("El jugador 2 ha ganado, despues de ", turnos+1, " turnos")
                            val = input("¿Quieres jugar otra partida?\n")
                            self.victorias2 = self.victorias2+1
                            #Si se quiere volver a jugar o no
                            if (val.lower() == "si"):
                                self.countTabla = 0
                                self.partidaPersona()
                            else:
                                print("El jugador 1 ha ganado ", self.victorias1, " veces y el jugador 2 ", self.victorias2)
                                exit()
                #Comprobacion de tablas
                elif (valor1.lower() == "tablas"):
                    print("Tablas solicitadas...")
                    aceptar = input("¿Aceptar tablas?\n")
                    #Array con diferentes posibilidades de aceptacion
                    posibilidad = ["si", "true", "verdad", "por supuesto"]
                    #Comprobamos si el texto introducido esta en las posibilidades
                    if (posibilidad.count(aceptar.lower())):
                        print("Tablas aceptadas, empate")
                        exit()
                    #Si se solicitan demasiadas tablas
                    elif (self.countTabla == 2):
                        print("Demasiadas veces solicitadas tablas, el jugador 1 ha perdido")
                        exit()
                    else:
                        print("Tablas no aceptadas")
                        Jugar.crearTabla(graficoP)
                        self.countTabla = self.countTabla + 1
                else:
                    Jugar.crearTabla(graficoP)
                    self.paso2 = True
            if (self.paso1 == False or self.paso2 == False):
                turnos += 1





    #Funcion para cambiar los valores del teclado numerico a la correspondiente del tres en raya
    def cambio(posicion):
        if (posicion == 7):
            return 0
        elif (posicion == 8):
            return 1
        elif (posicion == 9):
            return 2
        elif (posicion == 4):
            return 3
        elif (posicion == 5):
            return 4
        elif (posicion == 6):
            return 5
        elif (posicion == 1):
            return 6
        elif (posicion == 2):
            return 7
        elif (posicion == 3):
            return 8





    #Funcion con todas las posibilidades de victoria
    def victoria(grafico, ficha):
        fin = "no"
        if (grafico[0] == ficha and grafico[3] == ficha and grafico[6] == ficha):
            fin = "Victoria"
        elif (grafico[1] == ficha and grafico[4] == ficha and grafico[7] == ficha):
            fin = "Victoria"
        elif (grafico[2] == ficha and grafico[5] == ficha and grafico[8] == ficha):
            fin = "Victoria"
        elif (grafico[0] == ficha and grafico[1] == ficha and grafico[2] == ficha):
            fin = "Victoria"
        elif (grafico[3] == ficha and grafico[4] == ficha and grafico[5] == ficha):
            fin = "Victoria"
        elif (grafico[6] == ficha and grafico[7] == ficha and grafico[8] == ficha):
            fin = "Victoria"
        elif (grafico[0] == ficha and grafico[4] == ficha and grafico[8] == ficha):
            fin = "Victoria"
        elif (grafico[6] == ficha and grafico[4] == ficha and grafico[2] == ficha):
            fin = "Victoria"
        return fin





    #Si se quiere jugar contra la maquina
    def partidaMaquina(self):
        #Array vacio para empezar
        graficoP = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"])
        #Contador de turnos
        turnos = 0
        while turnos < 9:
            Jugar.crearTabla(graficoP)
            valorC = input("Selecciona la posicion o solicita tablas:\n")
            #Si el texto es numerico
            if (valorC.isnumeric()):
                valorCInt = int(valorC)
                valorCam = valorCInt
                valorCInt = Jugar.cambio(valorCInt)
                #Comprobar que el valor no se sale del cuadrado
                if (valorCam > 9 or valorCam < 1):
                    print("No puedes salirte del cuadrado")
                #Comprobamos si el espacio seleccionado esta vacio
                elif (graficoP[valorCInt] == "X" or graficoP[valorCInt] == "0"):
                    print("Selecciona un espacio vacio")
                    time.sleep(1)
                    clear()
                else:
                    #Ponemos un valor por defecto para luego cambiarlo por la ficha del jugador
                    graficoP[valorCInt] = "a"
                    graficoP[np.where(graficoP == "a")[0]] = "X"
                    Jugar.crearTabla(graficoP)
                    victoria = Jugar.victoria(graficoP, ficha="X")
                    turnos += 1

                    if (victoria == "no"):
                        aceptado = True
                        #Mientras que el espacio este ocupado
                        while aceptado:
                            #Selecciona un numero aleatorio
                            bot = random.randint(0, 8)
                            #Comprueba si ya hay algun caracter escrito
                            if (graficoP[bot] == "X" or graficoP[bot] == "0"):
                                bot = random.randint(0, 8)
                            else:
                                aceptado = False
                        graficoP[bot] = "0"
                        Jugar.crearTabla(graficoP)
                        victoria = Jugar.victoria(graficoP, ficha="0")
                        turnos += 1
                        #Mensaje de derrota del jugador
                        if (victoria == "Victoria"):
                            print("Has perdido, despues de ", turnos+1, " turnos")
                            val = input("¿Quieres volver a intentarlo?\n")
                            #Si queremos volver a jugar otra partida o salir directamente
                            if (val.lower() == "si"):
                                self.countTabla = 0
                                self.partidaPersona()
                            else:
                                exit()
                    else:
                        print("Has ganado, despues de ", turnos+1, " turnos")
                        break
            #Si se solicita tabla
            elif (valorC.lower() == "tablas"):
                print("Tablas solicitadas...")
                time.sleep(1)
                clear()
                posible = random.randint(0, 1)
                #Diferentes posibilidades al solicitar tablas a la maquina
                if (posible == 1):
                    print("Tablas aceptadas, empate")
                    exit()
                elif (self.countTabla == 2):
                    print("Demasiadas veces solicitadas tablas, has perdido")
                    exit()
                else:
                    print("Tablas no aceptadas")
                    self.countTabla = self.countTabla + 1
            else:
                time.sleep(1)
                clear()
