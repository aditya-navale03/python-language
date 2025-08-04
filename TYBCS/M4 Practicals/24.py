import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Define the nodes (vertices) based on their positions in the image
# We can assign numerical labels to the nodes for simplicity
# Let's assume the top node is 0, the next layer from left to right is 1, 2, 3
# and the bottom two nodes are 4, 5

# Add nodes to the graph
G.add_nodes_from([0, 1, 2, 3, 4, 5])

# Add edges (lines) based on the connections in the image
G.add_edges_from([
    (0, 1), (0, 2), (0, 3),  # Top node connected to the middle three
    (1, 4), (1, 2),          # Left middle node connections
    (2, 3), (2, 5),          # Middle middle node connections
    (3, 5),                  # Right middle node connections
    (4, 5)                   # Bottom line
])

# Define positions for the nodes to resemble the image
# These are approximate coordinates, adjust as needed for visual accuracy
pos = {
    0: (0.5, 1.0),   # Top node
    1: (0.2, 0.6),   # Left middle
    2: (0.5, 0.6),   # Center middle
    3: (0.8, 0.6),   # Right middle
    4: (0.0, 0.0),   # Bottom left
    5: (1.0, 0.0)    # Bottom right
}

# Draw the graph
nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors='black', node_size=200)
nx.draw_networkx_edges(G, pos, edge_color='black')

# Optional: Add labels to nodes if desired
# nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

plt.title("Graph G₂")
plt.axis('off') # Turn off the axis
plt.show()