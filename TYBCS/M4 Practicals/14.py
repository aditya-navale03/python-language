import networkx as nx
import matplotlib.pyplot as plt

g = nx.random_regular_graph(2, 5)
nx.draw(g)
plt.show()

g1 = nx.random_regular_graph(3, 8)
nx.draw(g1)
plt.show()

p = nx.petersen_graph()
nx.draw(p)
plt.show()