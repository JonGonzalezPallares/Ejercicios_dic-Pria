import numpy as np
import random as rd

class MapGrid:
    def __init__(self):
        self.width = 10
        self.heigth = 10
        self.grafico = ""

    def draw_grid(self):
        #for _ in range(self.heigth):
            #print(". " * self.width)

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

                if(ar != [0,0] and ar != [self.width-1, self.heigth-1]):
                    for paso2 in range(len(numerosRan)):
                        if(numerosRan[paso2] != ar):
                            dif = dif + 1

                    #print(len(numerosRan), " ", dif)
                    if(dif==len(numerosRan)):
                        numerosRan[paso] = ar
                        prob=False
                    else:
                        prob=True
            #print("\n")
                    
            self.grafico[alto][ancho] = "#"
        #print(numerosRan)

        for alto in range(self.heigth):
            print("\n")
            for ancho in range(self.width):
                print(self.grafico[alto][ancho], end=" ")
        print("\n")