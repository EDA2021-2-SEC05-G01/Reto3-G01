﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


# ___________________________________________________
#  Funciones de print
# ___________________________________________________


def printcargadedatos(cont):
    print("\n---------------------------------------------------------------------------\n")
    print("El total de avistamientos de UFOS cargados es: " + str(controller.UFOSSize(cont)))
    print("\n---------------------------------------------------------------------------\n")
    i = 1
    l = lt.newList("ARRAY_LIST")
    lst = cont['ufos']
    print("Los primeros cinco avistamientos: ")
    while i <= 5:
        ufo = lt.getElement(lst, i)
        print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nPaís: " + ufo["country"]
                + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo["shape"])
        uf = lt.lastElement(lst)
        lt.removeLast(lst)
        lt.addFirst(l, uf)
        i += 1
    print("\n---------------------------------------------------------------------------\n")
    print("Los últimos cinco avistamientos: ")
    for u in lt.iterator(l):
        print("\nDatatime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])



def printgetufosfromcity(cont, lst, city):
    print("\n---------------------------------------------------------------------------\n")
    print("El total de ciudades donde han habido avistamientos de UFOS es: " + 
            str(controller.indexSize(cont, "cityIndex")))
    size = lt.size(lst)
    if size:
        print("\n---------------------------------------------------------------------------\n")
        print("Han sido registrados " + str(size) + " UFOS en la ciudad " + city)
        print("\n---------------------------------------------------------------------------\n")
        print("Los primeros 3 avistamientos en la ciudad " + city)
        if size > 6:
            i = 1
            while i <= 3:
                ufo = lt.getElement(lst, i)
                print("\n---------------------------------------------------------------------------\n")
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])
                i += 1
            i = size - 2
            print("\n---------------------------------------------------------------------------\n")
            print("\nLos últimos 3 avistamientos en la ciudad " + city)
            while i <= size:
                ufo = lt.getElement(lst, i)
                print("\n---------------------------------------------------------------------------\n")
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])
                i += 1
        else:
            for ufo in lst:
                print("\n---------------------------------------------------------------------------\n")
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])

    else:
        print("\n---------------------------------------------------------------------------\n")
        print("La ciudad ingresada es inválida o no han habido avistamientos en dicha ciudad")


def printgetufosfromduration(cont, mayores, lst, lmtinf, lmtsup):
    print("\n---------------------------------------------------------------------------\n")
    print("Hay " + str(controller.indexSize(cont, "durationn")) + " duraciones en UFOS")
    print("\n---------------------------------------------------------------------------\n")
    print("Las 5 duraciones más largas de avistamientos de UFOS:")
    for m in lt.iterator(mayores):
        x = cont['durationn']
        g = om.get(x, float(m))
        print("\n" + m + ": "+ str(lt.size(((g['value'])['lstufos']))))
    size = lt.size(lst)
    print("\n---------------------------------------------------------------------------\n")
    print("Hay " + str(size) + " avistamientos que duran entre " + str(lmtinf) + " y " + str(lmtsup) + " segundos")
    if size:
        i = 1
        l = lt.newList("ARRAY_LIST")
        print("\n---------------------------------------------------------------------------\n")
        print("Los primeros tres avistamientos en este rango:")
        while i <= 3:
            ufo = lt.getElement(lst, i)
            print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nPaís: " + ufo["country"]
                    + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo["shape"])
            uf = lt.lastElement(lst)
            lt.removeLast(lst)
            lt.addFirst(l, uf)
            i += 1
        print("\n---------------------------------------------------------------------------\n")
        print("Los últimos tres avistamientos en este rango: ")
        for u in lt.iterator(l):
            print("\nDatatime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                    + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])








# ___________________________________________________
#  Menú
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de UFOS")
    print("3- Consultar los avistamientos de una ciudad y el total de ciudades donde han habido avistamientos")
    print("4- Consultar la cantidad de avistamientos que duran un rango específico de tiempo")
    print("5- Consultar la cantidad de avistamientos ocurridos en un rango de horas")
    print("6- Consultar los avistamientos en un rango de fechas")
    print("7- Consultar los avistamientos en una Zona Geográfica")
    print("0- Cerrar la aplicación")
    print("*******************************************")

ufofile = 'UFOS-utf8-small.csv'
cont = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n> ')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de UFOS ....\n")
        controller.loadData(cont, ufofile)
        printcargadedatos(cont)

    elif int(inputs[0]) == 3:
        city = input('Ingrese la ciudad que desea consultar:\n>')
        lst = controller.getufosfromcity(cont, city)
        printgetufosfromcity(cont, lst, city)

    elif int(inputs[0]) == 4:
        lmtinf = float(input("Ingrese el límite inferior de duración:\n>"))
        lmtsup = float(input("Ingrese el límite superior de duración:\n>"))
        print('Altura del arbol: ' + str(controller.indexHeight(cont, "durationn")))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont, "durationn")))
        print('Menor Llave: ' + str(controller.minKey(cont, "durationn")))
        print('Mayor Llave: ' + str(controller.maxKey(cont, "durationn")))
        mayores = (controller.cincomayores(cont))
        lst = controller.getufosfromduration(cont, lmtinf, lmtsup)
        printgetufosfromduration(cont, mayores, lst, lmtinf, lmtsup)

    else:
        sys.exit(0)
sys.exit(0)
