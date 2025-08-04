import networkx as nx

g = nx.Graph()

g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edges_from([(1, 2), (3, 4), (4, 5), (2, 3), (4,3)])
g.adj

print(nx.adjacency_matrix(g).todense())
print(nx.incidence_matrix(g).todense())