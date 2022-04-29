import csv
from ctypes import POINTER
from claseViajero import ViajeroFrecuente
from menu import Menu

if __name__ == '__main__':
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=',')
    lista = []
    cabecera = True
    for comp in reader:
        if cabecera:
            cabecera = not cabecera
        else: 
            nuevoViajero = ViajeroFrecuente(int(comp[0]), int(comp[1]), comp[2], comp[3], int(comp[4]))
            lista.append(nuevoViajero)
    archivo.close()
    print("Lista de viajeros registrados")
    for i in range(len(lista)):      
        print(" {} ".format(lista[i]))
    num = int(input("ingrese numero de viajero a buscar"))
    for i, viaj in enumerate(lista):
        if viaj.get_numeroViajero() == num:
            viajeroBuscado = lista[i]
    m = Menu()
    m.opciones(viajeroBuscado)
