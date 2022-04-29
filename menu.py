from re import X
from tkinter import N


class Menu:
    __salir = True
    __op = 0
    def __init__(self,salir = True,op = 0):
        self.__salir = salir
        self.__op = op
    def opciones (self,v):
        while self.__salir:
            print("// MENU DE OPCIONES //")
            print("Opcion 1: consutar millas")
            print("Opcion 2: acumular millas")
            print("Opcion 3: canjear millas")
            print("Opcion 4: salir")
            self.__op = int(input('ingrese opcion a ejecutar'))
            if (self.__op== 1):
                x = v.cantidadTotalMillas()
                print("cantidad de millas acumuladas: {}".format(x))
            elif (self.__op== 2):
                m = int(input("ingrese cantidad de millas a acumular"))
                v.acumularMilas(m)
                x = v.cantidadTotalMillas()
                print("millas acumuladas : {}".format(x))
            elif (self.__op  == 3):
                c = int(input("ingrese millas a canjear"))
                n = v.canjearMillas(c)
                print("cantidad de millas acumuladas luego del canje {}".format(n))
            elif(self.__op == 4):
                self.__salir = not self.__salir
