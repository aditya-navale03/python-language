import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

v = [1,2,3]
e = [(1,2),(2,3)]

g.add_nodes_from(v)
g.add_edges_from(e)

nx.draw(g,with_labels=True)

plt.show()

g.add_node(5)
g.add_edge(2,5)

nx.draw(g,with_labels=True,node_color='red',edge_color='g')

plt.show()