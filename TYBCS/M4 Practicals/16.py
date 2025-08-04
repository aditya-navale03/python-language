import networkx as nx

s = nx.star_graph(6)
n = nx.empty_graph(4)
c = nx.complement(n)

print(s.is_directed())
print(s.is_multigraph())
print(nx.is_directed(c))
print(nx.is_bipartite(s))
print(nx.is_bipartite(c))
print(nx.is_connected(s))
print(nx.is_connected(n))
print(nx.is_k_regular(c, 3))
print(nx.is_k_regular(n, 0))