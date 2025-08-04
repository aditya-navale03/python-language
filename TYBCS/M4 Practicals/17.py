# verify isomorphic graphs
import networkx as nx
import matplotlib.pyplot as plt

g = nx.star_graph(5)
nx.draw(g)
plt.show()

k = nx.complement(g)
nx.draw(k)
plt.show()

nx.is_isomorphic(g, k)
# False

e = nx.empty_graph(5)
g1 = nx.complement(e)
g2 = nx.complete_graph(5)
nx.is_isomorphic(g1, g2)
# True