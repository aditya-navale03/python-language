import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

v = [1,2,3,4]
e = [(1,3),(1,4),(1,2)]

g.add_nodes_from(v)
g.add_edges_from(e)

elabel = { (1,2) : 'e1' , (1,3) : 'e2' , (1,4) : 'e3' }

nx.draw_networkx_edge_labels(g,pos=nx.spring_layout(g),edge_labels=elabel)

nx.draw(g,with_labels=True,font_weight='bold',node_color='red',edge_color='k')

plt.show()