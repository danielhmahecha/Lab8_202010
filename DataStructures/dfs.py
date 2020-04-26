from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from ADT import stack as stk


def newDFS_2(grafo, source,revisados):
    """
    Crea una busqueda DFS para un grafo y un vertice origen
    """
    map.put(revisados,source,{'marked':True , 'edgeTo' : None})
    dfs_2(grafo, source,revisados)
    

def dfs_2 (grafo, v, revisados) :
    adjs = g.adjacents(grafo,v)
    adjs_iter = it.newIterator (adjs)
    while (it.hasNext(adjs_iter)):
        w = it.next (adjs_iter)
        visited_w = map.contains(revisados, w)
        if visited_w == False :
            map.put(revisados, w, {'marked':True, 'edgeTo': v })
            dfs_2(grafo, w,revisados)

def hasPathTo_2(graph, v):
    element = map.get(graph,v)
    if element and element['value']['marked']==True:
        return True
    return False           
