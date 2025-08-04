import networkx as nx
import matplotlib.pyplot as plt

g = nx.MultiGraph()

v = [1,2,3,4]
e = [(1,2),(2,3),(3,2),(2,3),(2,4)]
# e = [(2,1),(2,3),(2,4)]

g.add_nodes_from(v)
g.add_edges_from(e)

nx.draw(g,with_labels=True)

plt.show()

print("Number of edges = ",g.number_of_edges())
print("Vertex set = ",g.nodes())
print("Edge set = ",g.edges())