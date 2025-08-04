# Finding adjacency_matrix and incidence_matrix of a graph:

import networkx as nx

g = nx.Graph()

g.add_nodes_from([1, 2, 3, 4])
g.add_edges_from([(1, 2), (1, 4), (3, 4)])
g.adj

print(nx.adjacency_matrix(g).todense())
print(nx.incidence_matrix(g).todense())