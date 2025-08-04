import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
G2 = nx.Graph()

G1.add_nodes_from([0, 1, 2, 3, 4, 5])


G1.add_edges_from([
    (0, 1),     
    (1, 2),        
    (1, 3),    
    (3, 4),            
    (4, 5), (4,0), 
    (2, 3), (2,5),    
    (5,0) 
])

pos = {
    2: (0, 2),      # top
    1: (2, 1),      # upper right
    3: (-2, 1),     # upper left
    0: (2, -1),     # lower right
    4: (-2, -1),    # lower left
    5: (0, -2)      # bottom
}
    
plt.figure()
nx.draw(G1, pos=pos, with_labels=True)
plt.title('Graph G₁')
plt.axis('equal')
plt.show()

# Create G2 (Triangle within triangle)
G2.add_nodes_from([0, 1, 2, 3, 4, 5])  # 0,1,2 for outer triangle, 3,4,5 for inner triangle
G2.add_edges_from([
    # Outer triangle edges
    (0, 1), (1, 2), (2, 0),
    # Inner triangle edges
    (3, 4), (4, 5), (5, 3),
    # Connecting edges between triangles
    (0, 3), (1, 4), (2, 5)
])

# Position nodes for G2 in concentric triangles
outer_radius = 2
inner_radius = 1

pos_g2 = {
    # Outer triangle vertices
    0: (0, outer_radius),                                    # top
    1: (-outer_radius * 0.866, -outer_radius * 0.5),        # bottom left
    2: (outer_radius * 0.866, -outer_radius * 0.5),         # bottom right
    # Inner triangle vertices
    3: (0, inner_radius),                                    # top
    4: (-inner_radius * 0.866, -inner_radius * 0.5),        # bottom left
    5: (inner_radius * 0.866, -inner_radius * 0.5)          # bottom right
}

# Draw G2
plt.figure(figsize=(8, 8))
nx.draw(G2, pos=pos_g2, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=16, font_weight='bold', 
        edge_color='black', width=2)
plt.title('Graph G₂')
plt.axis('equal')
plt.show()

print(nx.is_isomorphic(G1,G2))