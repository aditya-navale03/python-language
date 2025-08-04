import networkx as nx

g = nx.Graph()

g.add_nodes_from([1, 2, 3, 4])
g.add_edges_from([(1, 3), (2, 3), (3,4), (2, 4)])
g.adj

print(nx.adjacency_matrix(g).todense())
print(nx.incidence_matrix(g).todense())