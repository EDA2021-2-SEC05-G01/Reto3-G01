"""
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

from time import strptime
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp

import datetime
from time import process_time
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
            str(mp.size(cont['cityIndex'])))
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
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])
                i += 1
            i = size - 2
            print("\n---------------------------------------------------------------------------\n")
            print("\nLos últimos 3 avistamientos en la ciudad " + city)
            while i <= size:
                ufo = lt.getElement(lst, i)
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])
                i += 1
        else:
            print("\nUna muestra de los avistamientos en este rango de fechas:")
            for ufo in lst:
                print("\n---------------------------------------------------------------------------\n")
                print("\nDatatime: " + str(ufo["datetime"]) + "\nCiudad: " + city + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo['shape'])

    else:
        print("\n---------------------------------------------------------------------------\n")
        print("La ciudad ingresada es inválida o no han habido avistamientos en dicha ciudad")


def printgetufosfromduration(cont, lst, lmtinf, lmtsup):
    print("\n---------------------------------------------------------------------------\n")
    print("Hay " + str(controller.indexSize(cont, "durationn")) + " duraciones en UFOS")
    print("\n---------------------------------------------------------------------------\n")
    print("La duración más larga de un avistamiento de UFOS:")
    m = str(controller.maxKey(cont, "durationn"))
    x = cont['durationn']
    g = om.get(x, float(m))
    print("\n" + m + ": "+ str(lt.size(((g['value'])['lstufos']))))
    size = lt.size(lst)
    print("\n---------------------------------------------------------------------------\n")
    print("Hay " + str(size) + " avistamientos que duran entre " + str(lmtinf) + " y " + str(lmtsup) + " segundos")
    print("\n---------------------------------------------------------------------------\n")
    if size:
        if size >6:
            i = 1
            l = lt.newList("ARRAY_LIST")
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
        else:
            print("\nUna muestra de los avistamientos en este rango de fechas:")
            for u in lt.iterator(lst):
                print("\nDatetime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                    + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])



def printgetuforbydate(cont,lst, lmtinf, lmtsup):
    print("\n---------------------------------------------------------------------------\n")
    print("Hay " + str(controller.indexSize(cont, "dates")) + " fechas [YYYY-MM-DD] diferentes en las que se han reportado ufos.")
    print("\n---------------------------------------------------------------------------\n")
    print("La fecha más antigua en la que se ha reportado un avistamiento es:\n" + str(controller.minKey(cont, "dates")) +
            ": " + str(lt.size(((om.get(cont["dates"], controller.minKey(cont, "dates")))['value'])['lstufos'])))
    size = lt.size(lst)
    if size:
        print("\n---------------------------------------------------------------------------\n")
        print("Hay " + str(size) + " UFOS reportados entre " + str(lmtinf) + " y " + str(lmtsup))
        print("\n---------------------------------------------------------------------------\n")
        if size >6:
            i = 1
            l = lt.newList("ARRAY_LIST")
            print("Los primeros tres avistamientos en este rango:")
            while i <= 3:
                ufo = lt.getElement(lst, i)
                print("\nDatetime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo["shape"])
                uf = lt.lastElement(lst)
                lt.removeLast(lst)
                lt.addFirst(l, uf)
                i += 1
            print("\n---------------------------------------------------------------------------\n")
            print("Los últimos tres avistamientos en este rango: ")
            for u in lt.iterator(l):
                print("\nDatetime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                        + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])
        else:
            print("\nUna muestra de los avistamientos en este rango de fechas:")
            for u in lt.iterator(lst):
                print("\nDatetime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                        + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])

        
def printgetufosbylocalitation(cont, lst):
    size = lt.size(lst)
    if size:
        print("\n---------------------------------------------------------------------------\n")
        print("Han habido " + str(size) + " avistamientos en esta área geográfica.")
        print("\n---------------------------------------------------------------------------\n")
        if size >10:
            i = 1
            l = lt.newList("ARRAY_LIST")
            print("Los primeros tres avistamientos en este rango:")
            while i <= 5:
                ufo = lt.getElement(lst, i)
                print("\nDatetime: " + str(ufo["datetime"]) + "\nCiudad: " + ufo["city"] + "\nPaís: " + ufo["country"]
                        + "\nDuración (segundos): " + str(ufo["duration (seconds)"]) + "\nForma del objeto: " + ufo["shape"])
                uf = lt.lastElement(lst)
                lt.removeLast(lst)
                lt.addFirst(l, uf)
                i += 1
            print("\n---------------------------------------------------------------------------\n")
            print("Los últimos tres avistamientos en este rango: ")
            for u in lt.iterator(l):
                print("\nDatetime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                        + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])
        else:
            print("\nUna muestra de los avistamientos en esta zona geográfica:")
            for u in lt.iterator(lst):
                print("\nDatetime: " + str(u["datetime"]) + "\nCiudad: " + u["city"] + "\nPaís: " + u["country"]
                        + "\nDuración (segundos): " + str(u["duration (seconds)"]) + "\nForma del objeto: " + u["shape"])
    else:
        print("No han habido avistamientos en esa localización geográfica dada.")



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

ufofile = 'UFOS-utf8-5pct.csv'
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
        #PRUEBA DE EJECUCIÓN
        start_time = process_time()

        controller.loadData(cont, ufofile)

        #PRUEBAS DE EJECUCIÓN
        stop_time = process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("tiempo de ejecución: " + str(elapsed_time_mseg))
        printcargadedatos(cont)

    elif int(inputs[0]) == 3:
        city = input('Ingrese la ciudad que desea consultar:\n>')
        #PRUEBA DE EJECUCIÓN
        start_time = process_time()

        lst = controller.getufosfromcity(cont, city)

        #PRUEBAS DE EJECUCIÓN
        stop_time = process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("tiempo de ejecución: " + str(elapsed_time_mseg))
        printgetufosfromcity(cont, lst, city)

    elif int(inputs[0]) == 4:
        lmtinf = float(input("Ingrese el límite inferior de duración:\n>"))
        lmtsup = float(input("Ingrese el límite superior de duración:\n>"))
        #PRUEBA DE EJECUCIÓN
        start_time = process_time()

        lst = controller.getufosfromduration(cont, lmtinf, lmtsup)

        #PRUEBAS DE EJECUCIÓN
        stop_time = process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("tiempo de ejecución: " + str(elapsed_time_mseg))
        printgetufosfromduration(cont, lst, lmtinf, lmtsup)

    elif int(inputs[0]) == 6:
        lmtinf = input("Ingrese el límite inferior del rango de fechas:\n>")
        lmtsup = input("Ingrese el límite superior del rango de fechas:\n>")
        #PRUEBA DE EJECUCIÓN
        start_time = process_time()

        lst = controller.getuforbydate(cont, lmtinf, lmtsup)

        #PRUEBAS DE EJECUCIÓN
        stop_time = process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("tiempo de ejecución: " + str(elapsed_time_mseg))
        printgetuforbydate(cont, lst, lmtinf, lmtsup)

    elif int(inputs[0]) == 7:
        lmtinf =  round(float(input("Ingrese el límite inferior del rango de latitudes:\n>")),2)
        lmtsup =  round(float(input("Ingrese el límite superior del rango de latitudes:\n>")),2)
        loninf =  round(float(input("Ingrese el límite inferior del rango de longitud:\n>")),2)
        lonsup =  round(float(input("Ingrese el límite superior del rango de longitud:\n>")),2)
        #PRUEBA DE EJECUCIÓN
        start_time = process_time()

        lst = (controller.getufosbylocalitation(cont, lmtinf, lmtsup, loninf, lonsup))

        #PRUEBAS DE EJECUCIÓN
        stop_time = process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("tiempo de ejecución: " + str(elapsed_time_mseg))
        printgetufosbylocalitation(cont, lst)

    else:
        sys.exit(0)
sys.exit(0)
