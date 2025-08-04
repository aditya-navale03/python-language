# subgraph 

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
e = [("a", "b"), ("c", 2), (2, 3), (1, 2), ("b", 3)]
g.add_edges_from(e)
nx.draw(g, with_labels=True, font_weight='bold')
plt.show()

g1 = g.subgraph(["a", "b", 1])
nx.draw(g1, with_labels=True, node_color="r")
plt.show()