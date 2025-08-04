# operation of deletion of vertices and edges in a graph

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
v = [1,2,3,"a","b"]

g.add_nodes_from(v)
g.add_edges_from([(1, 2), (2, 3), (1, "a"), ("a", "b"),("b", 2)])

nx.draw(g, with_labels=True, node_color='g')
plt.show()

# deletion of vertices
g.remove_nodes_from(["a", "b"])
nx.draw(g, with_labels=True, node_color='m')
plt.show()

# deletion of edges
g.remove_edges_from([(2,3),("b","a")])
nx.draw(g, with_labels=True, node_color='cyan')
plt.show()

