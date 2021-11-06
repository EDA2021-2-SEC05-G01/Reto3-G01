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
    analyzer = {'ufos':None,
                'cityIndex': None,
                'duration': None,
                'dates': None,
                'latitudes': None
                }
    analyzer['ufos'] = lt.newList("ARRAY_LIST")
    analyzer['cityIndex'] = m.newMap(numelements=805,
                                        maptype='CHAINING',
                                        loadfactor=2.0,)
    analyzer['durationn'] = om.newMap(omaptype='RBT', 
                                        comparefunction=compareduration)
    analyzer['dates'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    analyzer['latitudes'] = om.newMap(omaptype='RBT',
                                    comparefunction=comparelatitudes)
    return analyzer

# Funciones para agregar informacion al catalogo

def addCrime(analyzer, ufo):
    lt.addLast(analyzer['ufos'], ufo)
    updatecityIndex(analyzer['cityIndex'], ufo)
    updatedurationindex(analyzer['durationn'], ufo)
    updatedateIndex(analyzer['dates'], ufo)
    updatelatitudeIndex(analyzer['latitudes'], ufo)
    return analyzer

def updatecityIndex(map, ufo):
    city = ufo["city"]
    if m.contains(map, city):
        lst = (m.get(map, city))['value']
        lt.addLast(lst, ufo)
        m.put(map, city, lst)
    else:
        lst = lt.newList('SINGLE_LINKED')
        lt.addLast(lst, ufo)
        m.put(map, city, lst)
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

def updatedateIndex(map, ufo):
    datet = (ufo['datetime'])[:10]
    ufodate = datetime.datetime.strptime(datet, '%Y-%m-%d')
    entry = om.get(map, ufodate.date())
    if entry is None:
        datentry = newdataEntry(ufo)
        om.put(map, ufodate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, ufo)
    return map

def updatelatitudeIndex(map, ufo):
    lat = round(float(ufo['latitude']),2)
    entry = om.get(map, lat)
    if entry is None:
        datentry = newlatitudeEntry(ufo)
        om.put(map, lat, datentry)
    else:
        datentry = me.getValue(entry)
    addlatitudeIndex(datentry, ufo)
    return map


def addDateIndex(datentry, ufo):
    lst = datentry['lstufos']
    lt.addLast(lst, ufo)
    ufocity = datentry['ufocity']
    offentry = m.get(ufocity, ufo['city'])
    if (offentry is None):
        entry = newDataEntry(ufo)
        lt.addLast(entry['lstufos'], ufo)
        m.put(ufocity, ufo['city'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstufos'], ufo)
    return datentry

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


def addlatitudeIndex(cityentry, ufo):
    lst = cityentry['lstufos']
    lt.addLast(lst, ufo)
    ufodur = cityentry['latitude']
    offentry = m.get(ufodur, round(float(ufo['latitude']),2))
    if (offentry is None):
        entry = newlatitudeEntry(ufo)
        lt.addLast(entry['lstufos'], ufo)
        m.put(ufodur, round(float(ufo['latitude']),2), entry)
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
                                    maptype='CHAINING',
                                   loadfactor=2.0)
    entry['lstufos'] = lt.newList('SINGLE_LINKED')
    return entry


def newdataEntry(ufo):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'ufocity': None, 'lstufos': None}
    entry['ufocity'] = m.newMap(numelements=805,
                                    maptype='CHAINING',
                                   loadfactor=2.0)
    entry['lstufos'] = lt.newList('SINGLE_LINKED')
    return entry

def newdurationEntry(ufo):
    ofentry = {'duration': None, 'lstufos': None}
    ofentry['duration'] = m.newMap(numelements=60,
                                    maptype='CHAINING',
                                   loadfactor=2.0)
    ofentry['lstufos'] = lt.newList('SINGLE_LINKED')
    return ofentry


def newlatitudeEntry(ufo):
    ofentry = {'latitude': None, 'lstufos': None}
    ofentry['latitude'] = m.newMap(numelements=575,
                                    maptype='CHAINING',
                                   loadfactor=2.0)
    ofentry['lstufos'] = lt.newList('SINGLE_LINKED')
    return ofentry



# ==============================
# Funciones de consulta
# ==============================

def getufosfromcity(analyzer, city):
    lst = (m.get(analyzer['cityIndex'], city)['value'])
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

def getuforbydate(analyzer, lmtinf, lmtsup):
    dates = analyzer['dates']
    lstdates = om.keySet(dates)
    lista = lt.newList("ARRAY_LIST")
    lmtinf = datetime.datetime.strptime(lmtinf, '%Y-%m-%d')
    lmtsup = datetime.datetime.strptime(lmtsup, '%Y-%m-%d')
    posi = lt.isPresent(lstdates, om.ceiling(dates, lmtinf.date()))
    posf = lt.isPresent(lstdates, om.floor(dates, lmtsup.date()))
    while posi <= posf:
        elemento = (om.get(dates, lt.getElement(lstdates, posi))['value'])['lstufos']
        for e in lt.iterator(elemento):
            lt.addLast(lista, e)
        posi += 1
    return lista

def getufosbylocalitation(analyzer, lmtinf, lmtsup, loninf, lonsup):
    lmtinf = om.ceiling(analyzer['latitudes'], lmtinf)
    lmtsup = om.floor(analyzer['latitudes'], lmtsup)
    lista = lt.newList("ARRAY_LIST")
    lstlatitudes = om.keys(analyzer['latitudes'], lmtinf, lmtsup)
    for lat in lt.iterator(lstlatitudes):
        la = ((om.get(analyzer['latitudes'], lat)['value'])['lstufos'])
        for l in lt.iterator(la):
            if round(float(l['longitude']),2) >= loninf and round(float(l['longitude']),2) <= lonsup:
                lt.addLast(lista, l)
    compareda(lista)
    return lista


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

def comparelatitudes(l1, l2):
    if (l1 == l2):
        return 0
    elif (l1 > l2):
        return 1
    else:
        return -1

def comparedat(ufo1, ufo2):
    date1 = ufo1['datetime']
    date2 = ufo2['datetime']
    date1 = strptime(date1, '%Y-%m-%d %H:%M:%S')
    date2 = strptime(date2, '%Y-%m-%d %H:%M:%S')
    return date1 < date2

def comparefecha(ufo1, ufo2):
    date1 = ufo1['datetime']
    date2 = ufo2['datetime']
    date1 = strptime(date1, '%Y-%m-%d')
    date2 = strptime(date2, '%Y-%m-%d')
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

def compararfecha(lst):
    mg.sort(lst, comparefecha)
    return lst