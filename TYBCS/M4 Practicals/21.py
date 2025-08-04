# Products of Graphs

import networkx as nx
import matplotlib.pyplot as plt

g1 = nx.Graph()
g1.add_edges_from([(1, 2), (2, 3)])
nx.draw(g1, with_labels=True, node_color='r')
plt.show()

g2 = nx.Graph()
g2.add_edges_from([("a", "b")])
nx.draw(g2, with_labels=True, node_color='m')
plt.show()

# cartesian product of g1 and g2
pr = nx.cartesian_product(g1, g2)
nx.draw(pr, with_labels=True)
plt.show()

# strong product of g1 and g2
pr1 = nx.strong_product(g1, g2)
nx.draw(pr1, with_labels=True)
plt.show()

# tensor product of g1 and g2
pr2 = nx.tensor_product(g1, g2)
nx.draw(pr2, with_labels=True)
plt.show()