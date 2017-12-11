from graph import Graph
from dfs import *
from bfs import *

def graph_from_edgelist(E, org, des, directed=False):
    g = Graph(directed)

    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])
        
    verts = {}
    for v in V:
        verts[v] = g.insert_vertex(v)

    for e in E:
        src = e[0]
        dest = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(verts[src], verts[dest], element)
        
    print("\n\nAll vertices\n")
    for vertex in g.vertices():
        print(vertex) 
        
    print("\n\nincoming to destination edges\n")
    for e in g.incident_edges(verts[des], False):
        print(e)
    
    print("\n\noutgoing from origin edges\n")
    for e in g.incident_edges(verts[org], True):
        print(e)
    
    # DFS
    dfstree = {verts[org] : None}
    DFS(g, verts[org], dfstree)
    print ("\n\nDFS from origin visited nodes\n")
    for key in dfstree.keys():
        print(key)
        
    print ("\n\nDFS from origin to destination\n")    
    path = construct_path(verts[org], verts[des], dfstree)
    for stop in path:
        print(stop)
        
        
    # BFS    
    bfstree = {verts[org] : None}
    BFS(g, verts[org], bfstree)
    print ("\n\nBFS from origin visited nodes\n")
    for key in bfstree.keys():
        print(key)
        
    print ("\n\nBFS from origin to destination\n")
    path = construct_path(verts[org], verts[des], bfstree)
    for stop in path:
        print(stop)
    return g 
    
    
def graph_traversal():    
    E = (
    ('A','B'), ('A','E'), ('A','F'), ('B','C'), ('B','F'),
    ('C','D'), ('C','G'), ('D','G'), ('D','H'), ('E','F'),
    ('E','I'), ('F' 'I'), ('G','J'), ('G','K'), ('G','L'),
    ('H','L'), ('I','J'), ('I','M'), ('I','N'), ('J','K'),
    ('K','N'), ('K','O'), ('L','P'), ('M','N'),
        )
        
    return graph_from_edgelist(E,'A', 'N', True)
    
   
graph_traversal()
