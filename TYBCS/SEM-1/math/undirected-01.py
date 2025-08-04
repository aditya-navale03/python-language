import networkx as nx

v=[1,2,3,4]
e=[(1,2),(1,3),(1,4)]

g1=nx.Graph()
g1.add_nodes_from(v)
g1.add_edges_from(e)

 
import matplotlib.pyplot as plt
nx.draw(g1)
plt.show()
