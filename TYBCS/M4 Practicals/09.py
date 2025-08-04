import networkx as nx
import matplotlib.pyplot as plt

d1 = nx.DiGraph()

v = ["a",2,"b",4]
e = [("a",2),(2,"b"),(2,4),(2,"a"),("a","a")]

d1.add_nodes_from(v)
d1.add_edges_from(e)

nx.draw(d1,with_labels=True,node_color='r')

plt.show()

g = nx.to_undirected(d1)

nx.draw(g,with_labels=True,node_color='g')

plt.show()