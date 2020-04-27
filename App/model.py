"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import dfs as dfs
from DataStructures import bfs as bfs
from datetime import datetime
from DataStructures import bfs 
from DataStructures import dfs

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(111353,compareByKey)
    catalog = {'reviewGraph':rgraph}    
    return catalog


def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['reviewGraph'], row['SOURCE']):
        g.insertVertex (catalog['reviewGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['reviewGraph'], row['DEST']):
        g.insertVertex (catalog['reviewGraph'], row['DEST'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    g.addEdge (catalog['reviewGraph'], row['SOURCE'], row['DEST'], row['ARRIVAL_DELAY'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de revisiones
    """
    nodes = g.numVertex(catalog['reviewGraph'])
    edges = g.numEdges(catalog['reviewGraph'])

    return nodes,edges

def getPath (catalog, source, dest, strct):
    """
    Retorna el camino, si existe, entre vertice origen y destino
    """
    path = None
    if g.containsVertex(catalog['reviewGraph'],source) and g.containsVertex(catalog['reviewGraph'],dest):
        #print("vertices: ",source,", ", dest)
        if strct == 'dfs':
            search = dfs.newDFS(catalog['reviewGraph'],source)
            path = dfs.pathTo(search,dest)
        if strct == 'bfs':
            search = bfs.newBFS(catalog['reviewGraph'],source)
            path = bfs.pathTo(search, dest)
    # ejecutar dfs desde source
    # obtener el camino hasta dst
    # retornar el camino

    return path
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

