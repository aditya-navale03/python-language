import networkx as nx
import matplotlib.pyplot as plt

d1 = nx.DiGraph()

v = [1,2,3,4]
e = [(1,2),(2,3),(2,4),(2,1)]

d1.add_nodes_from(v)
d1.add_edges_from(e)

nx.draw(d1,with_labels=True,node_color='red')

plt.show()

print("Number of edges = ",d1.number_of_edges())
print("Number of vertices = ",d1.number_of_nodes())
print("Vertex set = ",d1.nodes())
print("Edge set = ",d1.edges())
print("in degree of vertices = ",d1.in_degree())
print("out degree of vertices = ",d1.out_degree())