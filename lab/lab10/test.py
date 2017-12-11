# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:18:05 2017

@author: bryna
"""




input = "'MIA'\r\n'ORD'\r\n'BOS' 'SFO'\r\n'BOS' 'JFK'\r\n'BOS' 'MIA'\r\n'JFK' 'BOS'\r\n'JFK' 'DFW'\r\n'JFK' 'MIA'\r\n'JFK' 'SFO'\r\n'ORD' 'DFW'\r\n'ORD' 'MIA'\r\n'LAX' 'ORD'\r\n'DFW' 'SFO'\r\n'DFW' 'ORD'\r\n'DFW' 'LAX'\r\n'MIA' 'DFW'\r\n'MIA' 'LAX'"

#input =  "'A'\r\n'N'\r\n'A' 'B'\r\n'A' 'E'\r\n'A' 'F'\r\n'B' 'C'\r\n'B' 'F'\r\n'C' 'D'\r\n'C' 'G'\r\n'D' 'G'\r\n'D' 'H'\r\n'E' 'F'\r\n'E' 'I'\r\n'F' 'I'\r\n'G' 'J'\r\n'G' 'K'\r\n'G' 'L'\r\n'H' 'L'\r\n'I' 'J'\r\n'I' 'M'\r\n'I' 'N'\r\n'J' 'K'\r\n'K' 'N'\r\n'K' 'O'\r\n'L' 'P'\r\n'M' 'N'"
inputlist = input.split('\r\n')
origin = inputlist[0]
destination = inputlist[1]
inputlist = inputlist[2:]
edges = list()
# line = "'A' 'B'"
for line in inputlist:
    linelist = line.split(' ')
    ele1 = linelist[0]
    ele2 = linelist[1]
    t = ele1, ele2
    edges.append(t)
print(edges)
print(origin)
print(destination)

graph_from_edgelist(edges, origin, destination, True)

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
        
    # print("\n\nAll vertices\n")
    # for vertex in g.vertices():
        # print(vertex) 
        
    # print("\n\nincoming to destination edges\n")
    # for e in g.incident_edges(verts[des], False):
        # print(e)
    
    # print("\n\noutgoing from origin edges\n")
    # for e in g.incident_edges(verts[org], True):
        # print(e)
    
    # DFS
    dfstree = {verts[org] : None}
    DFS(g, verts[org], dfstree)
    # print ("\n\nDFS from origin visited nodes\n")
    # for key in dfstree.keys():
        # print(key)
        
    print ("\n\nDFS from origin to destination\n")    
    path = construct_path(verts[org], verts[des], dfstree)
    for stop in path:
        print(stop)
        
        
    # BFS    
    bfstree = {verts[org] : None}
    BFS(g, verts[org], bfstree)
    # print ("\n\nBFS from origin visited nodes\n")
    # for key in bfstree.keys():
        # print(key)
        
    print ("\n\nBFS from origin to destination\n")
    path = construct_path(verts[org], verts[des], bfstree)
    for stop in path:
        print(stop)
    return g 