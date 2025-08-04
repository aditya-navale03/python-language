# Graph Operations

import networkx as nx
import matplotlib.pyplot as plt

g1 = nx.Graph()
v = [1, 2, 3, 4]
g1.add_nodes_from(v)
g1.add_edges_from([(1, 2), (2, 3), (2, 4), (2, 1)])
nx.draw(g1, with_labels=True, node_color='r')
plt.show()

g2 = nx.Graph()
v1 = ["a", "b", 1, 2, 3, 5]
e1 = [("a", "b"), ("b", 2), (5, 3), (1, 2), ("b", 5)]
g2.add_nodes_from(v1)
g2.add_edges_from(e1)
nx.draw(g2, with_labels=True, node_color='m')
plt.show()

# intersection of g1 and g2
ginter = nx.intersection(g1, g2)
nx.draw(ginter, with_labels=True)
plt.show()

# union of g1 and g2
union = nx.compose(g1, g2)
nx.draw(union, with_labels=True)
plt.show()

# disjoint union of g1 and g2
dis_uni = nx.disjoint_union(g1, g2)
nx.draw(dis_uni, with_labels=True)  
plt.show()

# # union with renaming
guni = nx.union(g1, g2, rename=("g1", "g2"))
nx.draw(guni, with_labels=True)
plt.show()

