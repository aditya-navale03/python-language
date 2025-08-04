import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

v = ['a','b','c']
e = [('a','b'),('b','c'),('c','a'),('b','b')]

g.add_nodes_from(v)
g.add_edges_from(e)

elabel = { ('a','b') : 'e1' , ('b','c') : 'e2' , ('a','c') : 'e3' , ('b','b') : 'e4' }

nx.draw_networkx_edge_labels(g,pos=nx.spring_layout(g),edge_labels=elabel)

nx.draw(g,with_labels=True,font_weight='bold',node_color='red',edge_color='m')

plt.show()

print("Number of vertices = ",g.number_of_nodes())
print("Number of edges = ",g.number_of_edges())
print("Vertex set = ",g.nodes())
print("Edge set = ",g.edges())
print("Degree of vertices = ",g.degree())