import config
import math
from DataStructures import adjlist as g
from DataStructures import listiterator as it
from ADT import queue as q
from ADT import map as map
from DataStructures import edge as e
from ADT import stack as stk
from ADT import list as lt




def newDFS(graph, source):
    """
    Crea una busqueda DFS para un grafo y un vertice origen
    """
    prime = nextPrime (g.numVertex(graph) * 2)
    search={'graph':graph, 's':source, 'visitedMap':None}   
    search['visitedMap'] = map.newMap(capacity=prime, maptype='PROBING', comparefunction=graph['comparefunction'])
    map.put(search['visitedMap'],source, {'marked':True,'edgeTo':None})
    dfs(search, source)
    return search

def dfs (search, v):
    adjs = g.adjacents(search['graph'],v)
    adjs_iter = it.newIterator (adjs)
    while (it.hasNext(adjs_iter)):
        w = it.next (adjs_iter)
        visited_w = map.get(search['visitedMap'], w)
        if visited_w == None:
            map.put(search['visitedMap'], w, {'marked':True, 'edgeTo':v})
            dfs(search, w)