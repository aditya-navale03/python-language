import networkx as nx
import matplotlib.pyplot as plt

g = nx.empty_graph(4)
nx.draw(g)
plt.show()

g1 = nx.complete_graph(5)
nx.draw(g1)
plt.show()

c1 = nx.cycle_graph(10)
nx.draw(c1)
plt.show()