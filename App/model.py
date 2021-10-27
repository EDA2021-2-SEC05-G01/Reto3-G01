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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import name
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.Algorithms.Sorting import mergesort as mg
import datetime
from time import strptime
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'ufos': None,
                'dateIndex': None,
                'cityIndex': None,
                'duration': None,
                'lstdur': None
                }

    analyzer['ufos'] = lt.newList('SINGLE_LINKED')
    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    analyzer['cityIndex'] = om.newMap(omaptype='RBT',
                                        comparefunction=compareCities)
    analyzer['durationn'] = om.newMap(omaptype='RBT', 
                                        comparefunction=compareduration)
    analyzer['lstdur'] = lt.newList("ARRAY_LIST")
    return analyzer

# Funciones para agregar informacion al catalogo

def addCrime(analyzer, ufo):
    """
    """
    lt.addLast(analyzer['ufos'], ufo)
    updateDateIndex(analyzer['dateIndex'], ufo)
    updatecityIndex(analyzer['cityIndex'], ufo)
    updatedurationindex(analyzer['durationn'], ufo)
    if lt.isPresent(analyzer['lstdur'], ufo['duration (seconds)']) == 0:
        lt.addLast(analyzer['lstdur'], ufo['duration (seconds)'])
    return analyzer


def updateDateIndex(map, ufo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    datet = ufo['datetime']
    ufodate = datetime.datetime.strptime(datet, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, ufodate.date())
    if entry is None:
        datentry = newDataEntry(ufo)
        om.put(map, ufodate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, ufo)
    return map

def updatecityIndex(map, ufo):
    city = ufo["city"]
    entry = om.get(map, city)
    if entry is None:
        cityentry = newcityEntry(ufo)
        om.put(map, city, cityentry)
    else:
        cityentry = me.getValue(entry)
    addCityIndex(cityentry, ufo)
    return map

def updatedurationindex(map, ufo):
    duration = ufo["duration (seconds)"]
    entry = om.get(map, float(duration))
    if entry is None:
        duraentry = newdurationEntry(ufo)
        om.put(map, float(duration), duraentry)
    else:
        duraentry = me.getValue(entry)
    adddurationIndex(duraentry, ufo)
    return map


def addDateIndex(datentry, ufo):
    lst = datentry['lstufos']
    lt.addLast(lst, ufo)
    ufocity = datentry['ufocity']
    offentry = m.get(ufocity, ufo['city'])
    if (offentry is None):
        entry = newcityEntry(ufo)
        lt.addLast(entry['lstufos'], ufo)
        m.put(ufocity, ufo['city'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstufos'], ufo)
    return datentry

def addCityIndex(cityentry, ufo):
    lst = cityentry['lstufos']
    lt.addLast(lst, ufo)
    ufocity = cityentry['city']
    offentry = m.get(ufocity, ufo['city'])
    if (offentry is None):
        entry = newcityEntry(ufo)
        lt.addLast(entry['lstufos'], ufo)
        m.put(ufocity, ufo['city'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstufos'], ufo)
    return cityentry

def adddurationIndex(cityentry, ufo):
    lst = cityentry['lstufos']
    lt.addLast(lst, ufo)
    ufodur = cityentry['duration']
    offentry = m.get(ufodur, ufo['duration (seconds)'])
    if (offentry is None):
        entry = newdurationEntry(ufo)
        lt.addLast(entry['lstufos'], ufo)
        m.put(ufodur, ufo['duration (seconds)'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstufos'], ufo)
    return cityentry 

def newDataEntry(ufo):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'ufocity': None, 'lstufos': None}
    entry['ufocity'] = m.newMap(numelements=30,
                                     maptype='PROBING')
    entry['lstufos'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newcityEntry(ufo):
    """
    Crea una entrada en el indice por tipo de ufo, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'city': None, 'lstufos': None}
    ofentry['city'] = m.newMap(numelements=1000,
                                     maptype='PROBING')
    ofentry['lstufos'] = lt.newList('SINGLELINKED')
    return ofentry

def newdurationEntry(ufo):
    ofentry = {'duration': None, 'lstufos': None}
    ofentry['duration'] = m.newMap(numelements=1000,
                                     maptype='PROBING')
    ofentry['lstufos'] = lt.newList('SINGLELINKED')
    return ofentry

def cincomayores(analyzer):
    lst = analyzer['lstdur']
    l = lt.newList("ARRAY_LIST")
    compareduratio(lst)
    i = 1
    while i <= 5:
        mayor = lt.firstElement(lst)
        lt.addLast(l, mayor)
        lt.removeFirst(lst)
        i += 1
    return l

# ==============================
# Funciones de consulta
# ==============================

def getufosfromcity(analyzer, city):
    lst = (om.get(analyzer['cityIndex'], city)['value'])['lstufos']
    compareda(lst)
    return lst

def getufosfromduration(analyzer, lmtinf, lmtsup):
    lst = lt.newList("ARRAY_LIST")
    while lmtinf <= lmtsup:
        ufos = om.get(analyzer['durationn'], lmtinf)
        if ufos != None:
            ufos = (ufos['value'])['lstufos']
            for ufo in lt.iterator(ufos):
                lt.addLast(lst, ufo)
        lmtinf = float(lmtinf) + 1
    compared(lst)
    return lst


def UFOSSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['ufos'])


def indexHeight(analyzer, name):
    """
    Altura del arbol
    """
    return om.height(analyzer[name])


def indexSize(analyzer, name):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer[name])


def minKey(analyzer,name):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer[name])


def maxKey(analyzer, name):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer[name])


# ==============================
# Funciones de Comparacion
# ==============================


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareCities(city1, city2):
    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1

def compareduration(d1, d2):
    if (d1 == d2):
        return 0
    elif (d1 > d2):
        return 1
    else:
        return -1

def comparedat(ufo1, ufo2):
    date1 = ufo1['datetime']
    date2 = ufo2['datetime']
    date1 = strptime(date1, '%Y-%m-%d %H:%M:%S')
    date2 = strptime(date2, '%Y-%m-%d %H:%M:%S')
    return date1 < date2

def comparedur(dur1, dur2):
    return float(dur1) > float(dur2)

def comparedo(d1, d2):
    return float(d1['duration (seconds)']) < float(d2['duration (seconds)'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1

def compareda(lst):
    mg.sort(lst, comparedat)
    return lst

def compareduratio(lst):
    mg.sort(lst, comparedur)
    return lst

def compared(lst):
    mg.sort(lst, comparedo)
    return lst