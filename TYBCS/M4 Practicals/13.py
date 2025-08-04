import networkx as nx
import matplotlib.pyplot as plt

w1 = nx.wheel_graph(10)
nx.draw(w1)
plt.show()

k4_7 = nx.complete_bipartite_graph(4, 7)
nx.draw(k4_7)
plt.show()

s = nx.star_graph(10)
nx.draw(s)
plt.show()