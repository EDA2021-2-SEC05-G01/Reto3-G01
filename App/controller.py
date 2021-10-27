"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, ufosfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ufofile = cf.data_dir + ufosfile
    input_file = csv.DictReader(open(ufofile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addCrime(analyzer, ufo)
    model.compareda(analyzer['ufos'])
    return analyzer

# Funciones de ordenamiento

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getufosfromduration(analyzer, lmtinf, lmtsup):
    return model.getufosfromduration(analyzer, lmtinf, lmtsup)


def getufosfromcity(analyzer, city):
    return model.getufosfromcity(analyzer, city)

def UFOSSize(analyzer):
    """
    Numero de UFOS leidos
    """
    return model.UFOSSize(analyzer)


def indexHeight(analyzer, name):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer, name)


def indexSize(analyzer, name):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer, name)


def minKey(analyzer, name):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer, name)


def maxKey(analyzer, name):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer, name)


def cincomayores(mapa):
    return model.cincomayores(mapa)
