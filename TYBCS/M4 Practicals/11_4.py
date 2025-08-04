import networkx as nx

g = nx.Graph()

g.add_nodes_from([1, 2, 3, 4 , 5 ,6 ])
g.add_edges_from([(1, 3), (1, 2), (3,4), (5, 6),(4,5),(3,6),(3,5)])
g.adj

print(nx.adjacency_matrix(g).todense())
print(nx.incidence_matrix(g).todense())