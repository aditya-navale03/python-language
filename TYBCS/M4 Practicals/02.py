import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from([(1,"b"),("b",2),("a",3)])

nx.draw(g,with_labels=True,font_weight='bold',node_color='yellow',edge_color='purple')

plt.show()