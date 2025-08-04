import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

v = [1,2,3,4]
e = [(1,2),(1,3),(1,4)]

g.add_nodes_from(v)
g.add_edges_from(e)

nx.draw(g)
plt.show()  