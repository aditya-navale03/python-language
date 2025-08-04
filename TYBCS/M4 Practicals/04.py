import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

v = [1,2,3,4,5]
e = [(1,2),(2,3),(3,4),(4,1),(1,5)]

g.add_nodes_from(v)
g.add_edges_from(e)

nx.draw(g,with_labels=True,font_weight='bold',node_color='red',edge_color='green')

plt.show()