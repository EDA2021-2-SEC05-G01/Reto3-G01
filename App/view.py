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
        print("\nCargando información de crimenes ....\n")
        controller.loadData(cont, ufofile)
        print('UFOS cargados: ' + str(controller.UFOSSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont, "dateIndex")))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont, "dateIndex")))
        print('Menor Llave: ' + str(controller.minKey(cont, "dateIndex")))
        print('Mayor Llave: ' + str(controller.maxKey(cont, "dateIndex")))

    elif int(inputs[0]) == 3:
        print('\nAltura del arbol: ' + str(controller.indexHeight(cont, "cityIndex")))
        print('\nElementos en el arbol: ' + str(controller.indexSize(cont, "cityIndex")))

    else:
        sys.exit(0)
sys.exit(0)
