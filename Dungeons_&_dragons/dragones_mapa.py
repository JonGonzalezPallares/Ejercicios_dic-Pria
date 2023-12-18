import numpy as np
import random as rd
import os

def clear(): return os.system('clear')

class MapGrid:
    def __init__(self):
        self.width = 10
        self.heigth = 10
        self.dificil = 0
        self.grafico = ""
        self.dragon = 0

    #Funcion para generar el grafico por defecto
    def draw_grid(self):
        self.grafico = np.full((self.heigth, self.width), fill_value=".  ")

    #Funcion para generar los muros
    def get_walls(self, porcentaje=0.3):
        #Segun el nivel de dificultad, habra mas o menos muros
        if(self.dificil == '2'):
            porcentaje = 0.4
        elif(self.dificil == '3'):
            numerosRan = [[]]*4
            porcentaje = 0.5
        elif(self.dificil == '1'):
            porcentaje = 0.2
        else:
            porcentaje=0.3
        num = round((self.width*self.heigth*porcentaje)/2)
        numerosRan = [[]]*num

        #Bucle para saber la posicion de los muros
        for paso in range(num):
            prob = True
            while prob:
                dif = 0

                #Posicion aleatoria para las casillas de muros
                ancho = rd.randint(0, self.width-2)
                alto = rd.randint(1, self.heigth-1)
                ar = [alto, ancho]
                #Si los numeros aleatorios no son ni el inicio, ni el final, ni las casillas adyacentes del final
                if(ar != [0,0] and ar != [self.width-1, self.heigth-1] and ar != [self.width-2, self.heigth-1] and ar != [self.width-1, self.heigth-2]):
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
                    
            #Añadimos el emoji de muro en las posiciones
            self.grafico[alto][ancho] = "🧱 "

        #Seccion para generar los fuegos, solo cuando la dificultad sea 3
        if(self.dificil == "3"):
            for paso in range(4):
                prob = True
                while prob:
                    dif = 0

                    #Posicion aleatoria para las casillas de muros
                    ancho = rd.randint(0, self.width-2)
                    alto = rd.randint(1, self.heigth-1)
                    ar = [alto, ancho]

                    #Si los numeros aleatorios no son ni el inicio, ni el final, ni las casillas adyacentes del final
                    if(ar != [0,0] and ar != [self.width-1, self.heigth-1] and ar != [self.width-2, self.heigth-1] and ar != [self.width-1, self.heigth-2]):
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
                        
                #Añadimos el emoji de fuego en las posiciones
                self.grafico[alto][ancho] = "🔥 "

        #Colocamos al jugador y el final de la mazmorra
        self.grafico[0][0]="🧙 "
        self.grafico[self.heigth-2][self.width-1]="🐉 "
        self.grafico[self.heigth-1][self.width-1]="👸 "

        #Para printar el grafico
        for alto in range(self.heigth):
            print("\n")
            for ancho in range(self.width):
                if(self.grafico[alto][ancho]=="🧙 "):
                    print(f"{self.grafico[alto][ancho]}", end=" ")
                elif(self.grafico[alto][ancho]=="🧱 "):
                    print(f"{self.grafico[alto][ancho]}", end=" ")
                elif(self.grafico[alto][ancho]=="🐉 "):
                    print(f"{self.grafico[alto][ancho]}", end=" ")
                else:
                    print(self.grafico[alto][ancho], end=" ")
        print("\n")

    #Funcion para mover al dragon
    def dragonMov(self):
        movimiento = rd.randint(1,4)
        pos = [0,0]
        antiguo = [0,0]
        posible = True
        while posible:
            #Guardamos la antigua posicion del dragon antes de moverse
            antiguo = [self.dragon[0], self.dragon[1]]

            #Segun que valor haya salido, se mueve en una posicion u otra
            if(movimiento==1):
                pos = [self.dragon[0]-1, self.dragon[1]]
            elif(movimiento==2):
                pos = [self.dragon[0], self.dragon[1]-1]
            elif(movimiento==3):
                pos = [self.dragon[0]+1, self.dragon[1]]
            else:
                pos = [self.dragon[0], self.dragon[1]+1]

            #Comprobaciones de que no se salga, ni se choque contra un muro
            if(pos[0]<self.heigth and pos[1]<self.width and pos[0]>-1 and pos[1]>-1 and self.grafico[pos[0]][pos[1]]!="🧱 " and self.grafico[pos[0]][pos[1]]!="🐉 "):
                #Para colocar los emojis correctos
                if(self.grafico[self.dragon[0]][self.dragon[1]]!="🧙 "):
                    self.grafico[self.dragon[0]][self.dragon[1]] = ".  "
                if(self.grafico[self.heigth-1][self.width-1] != "🧙 "):
                    self.grafico[self.heigth-1][self.width-1] = "👸 "
                if(self.grafico[0][0]!="🧙 "):
                    self.grafico[0][0] = "🏰 "

                posible = False

                #Comprobacion que el dragon se a movido al jugador
                if(self.grafico[pos[0]][pos[1]]=="🧙 "):
                    self.dragon[0] = pos[0]
                    self.dragon[1] = pos[1]
                    self.grafico[self.dragon[0]][self.dragon[1]] = "🐉 "
                    #Para printar el grafico
                    clear()
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="🧙 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🧱 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🐉 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
                    print("Has muerto")
                    exit()
                #Comprobacion si el jugador se ha movido a donde estaba el dragon
                elif(self.grafico[antiguo[0]][antiguo[1]]=="🧙 "):
                    self.grafico[self.dragon[0]][self.dragon[1]] = "🐉 "
                    #Para printar el grafico
                    clear()
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="🧙 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🧱 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🐉 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
                    print("Has muerto")
                    exit()
                else:
                    self.dragon[0] = pos[0]
                    self.dragon[1] = pos[1]
                    self.grafico[self.dragon[0]][self.dragon[1]] = "🐉 "
                    #Para printar el grafico
                    clear()
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="🧙 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🧱 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            elif(self.grafico[alto][ancho]=="🐉 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\n")
            else:
                movimiento = rd.randint(1,4)
             
           

    #Funcion para mover al personaje
    def move_player(self):
        #El primero es el movimiento hacia abajo/arriba, el segundo hacia la derecha e izquierda
        self.dragon = [self.heigth-2, self.width-1]
        self.dragon2 = [self.heigth-1, self.width-2]

        inicio = [0,0]
        movimiento = True
        while movimiento:
            casilla = input("Movimiento: w, a, s, d:\n¿Abandonar?\n")

            #Si hemos pulsado para ir a la derecha
            if(casilla.lower() == "d"):
                if(inicio[1]+1<self.width and self.grafico[inicio[0]][inicio[1]+1]!="🧱 "):
                    #Si hemos llegado al final
                    if(self.grafico[inicio[0]][inicio[1]+1] == "👸 "):
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="🧙 "):
                                    print(".  ", end=" ")
                                elif(self.grafico[alto][ancho]=="👸 "):
                                    print("🎆", end=" ")
                                elif(self.grafico[alto][ancho]=="🧱 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")  
                        print("MAZMORRA COMPLETADA")
                        exit()
                    #Si nos hemos chocado contra un muro
                    elif(self.grafico[inicio[0]][inicio[1]+1]=="🧱 "):
                        self.dragonMov(self)
                        print("Hay un muro")
                    #Si nos hemos chocado contra fuego
                    elif(self.grafico[inicio[0]][inicio[1]+1]=="🔥 "):
                        self.grafico[inicio[0]][inicio[1]] = ".  "
                        self.grafico[0][0] = "🏰 "
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="🧙 "):
                                    print(".  ", end=" ")
                                elif(self.grafico[alto][ancho]=="👸 "):
                                    print("🎆", end=" ")
                                elif(self.grafico[alto][ancho]=="🧱 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\nHas muerto quemado")
                        exit()
                    #Si nos movemos
                    else:
                        self.grafico[inicio[0]][inicio[1]] = ".  "
                        self.grafico[0][0] = "🏰 "
                        inicio[1] = inicio[1]+1
                        self.grafico[inicio[0]][inicio[1]] = "🧙 "
                        self.dragonMov(self)
                #Si no nos movemos: al pulsar enter, intentar salirse del mapa, andar contra un muro
                else:
                    self.dragonMov(self)


            #Si hemos pulsado para ir a la izquierda
            elif(casilla.lower() == "a"):
                if(inicio[1]-1>=0 and self.grafico[inicio[0]][inicio[1]-1]!="🧱 "):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    inicio[1] = inicio[1]-1
                    self.grafico[inicio[0]][inicio[1]] = "🧙 "
                    clear()
                    self.dragonMov(self)
                #Si nos hemos chocado contra un muro
                elif(self.grafico[inicio[0]][inicio[1]-1]=="🧱 "):
                    clear()
                    self.dragonMov(self)
                    print("Hay un muro")
                #Si nos hemos chocado contra fuego
                elif(self.grafico[inicio[0]][inicio[1]-1]=="🔥 "):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    self.grafico[0][0] = "🏰 "
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="🧙 "):
                                print(".  ", end=" ")
                            elif(self.grafico[alto][ancho]=="👸 "):
                                print("🎆", end=" ")
                            elif(self.grafico[alto][ancho]=="🧱 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\nHas muerto quemado")
                    exit()
                #Si nos movemos a la casilla de inicio
                elif(inicio[0]==1 and inicio[1]==0):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    inicio[0] = inicio[0]-1
                    self.grafico[inicio[0]][inicio[1]] = "🧙 "
                    self.dragonMov(self)
                #Si no nos movemos: al pulsar enter, intentar salirse del mapa, andar contra un muro
                else:
                    self.dragonMov(self)


            #Si hemos pulsado para ir hacia arriba
            elif(casilla.lower() == "w"):
                if(inicio[0]-1>=0 and self.grafico[inicio[0]-1][inicio[1]]!="🧱 "):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    inicio[0] = inicio[0]-1
                    self.grafico[inicio[0]][inicio[1]] = "🧙 "
                    self.dragonMov(self)
                #Si nos hemos chocado contra un muro
                elif(self.grafico[inicio[0]-1][inicio[1]]=="🧱 "):
                    clear()
                    self.dragonMov(self)
                    print("Hay un muro")
                #Si nos hemos chocado contra fuego
                elif(self.grafico[inicio[0]-1][inicio[1]]=="🔥 "):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    self.grafico[0][0] = "🏰 "
                    clear()
                    #Para printar el grafico
                    for alto in range(self.heigth):
                        print("\n")
                        for ancho in range(self.width):
                            if(self.grafico[alto][ancho]=="🧙 "):
                                print(".  ", end=" ")
                            elif(self.grafico[alto][ancho]=="👸 "):
                                print("🎆", end=" ")
                            elif(self.grafico[alto][ancho]=="🧱 "):
                                print(f"{self.grafico[alto][ancho]}", end=" ")
                            else:
                                print(self.grafico[alto][ancho], end=" ")
                    print("\nHas muerto quemado")
                    exit()
                #Si nos movemos a la casilla de inicio
                elif(inicio[0]==1 and inicio[1]==0):
                    self.grafico[inicio[0]][inicio[1]] = ".  "
                    inicio[0] = inicio[0]-1
                    self.grafico[inicio[0]][inicio[1]] = "🧙 "
                    self.dragonMov(self)
                #Si no nos movemos: al pulsar enter, intentar salirse del mapa, andar contra un muro
                else:
                    self.dragonMov(self)
                    

            #Si hemos pulsado para ir abajo            
            elif(casilla.lower() == "s"):
                if(inicio[0]+1<self.heigth and self.grafico[inicio[0]+1][inicio[1]]!="🧱 "):
                    #Si hemos llegado al final
                    if(self.grafico[inicio[0]+1][inicio[1]] == "👸 "):
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="🧙 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                elif(self.grafico[alto][ancho]=="🧱 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                elif(self.grafico[alto][ancho]=="🐉 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\n")  
                        print("MAZMORRA COMPLETADA")
                        exit()
                    #Si nos hemos chocado contra un muro
                    elif(self.grafico[inicio[0]+1][inicio[1]]=="🧱 "):
                        clear()
                        self.dragonMov(self)
                        print("Hay un muro")
                    #Si nos hemos chocado contra fuego
                    elif(self.grafico[inicio[0]+1][inicio[1]]=="🔥 "):
                        self.grafico[inicio[0]][inicio[1]] = ".  "
                        self.grafico[0][0] = "🏰 "
                        clear()
                        #Para printar el grafico
                        for alto in range(self.heigth):
                            print("\n")
                            for ancho in range(self.width):
                                if(self.grafico[alto][ancho]=="🧙 "):
                                    print(".  ", end=" ")
                                elif(self.grafico[alto][ancho]=="👸 "):
                                    print("🎆", end=" ")
                                elif(self.grafico[alto][ancho]=="🧱 "):
                                    print(f"{self.grafico[alto][ancho]}", end=" ")
                                else:
                                    print(self.grafico[alto][ancho], end=" ")
                        print("\nHas muerto quemado")
                        exit()
                    #Si nos movemos
                    else:
                        self.grafico[inicio[0]][inicio[1]] = ".  "
                        self.grafico[0][0] = "🏰 "
                        inicio[0] = inicio[0]+1
                        self.grafico[inicio[0]][inicio[1]] = "🧙 "
                        clear()
                        self.dragonMov(self)
                #Si no nos movemos: al pulsar enter, intentar salirse del mapa, andar contra un muro
                else:
                    self.dragonMov(self)

            #Si el jugador decide abandonar por que no se puede completar o no puede
            elif(casilla.lower() == "abandonar"):
                print("Has abandonado la mazmorra")
                exit()

            else:
                self.dragonMov(self)