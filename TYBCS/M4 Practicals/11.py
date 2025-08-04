import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

a = np.array([[0,1,0],[1,1,1],[0,1,0]])
g = nx.from_numpy_matrix(a)
nx.draw(g)
plt.show()