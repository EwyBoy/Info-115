import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,11),(1,12),(1,13),(1,14),(1,18),(1,20),(1,22),(1,32)])
G.add_edges_from([(2,1),(2,3),(2,4),(2,8),(2,14),(2,18),(2,20),(2,22),(2,31)])
G.add_edges_from([(3,1),(3,2),(3,4),(3,8),(3,9),(3,10),(3,14),(3,28),(3,29),(3,33)])
G.add_edges_from([(4,1),(4,2),(4,3),(4,8),(4,13),(4,14)])
G.add_edges_from([(5,1),(5,7),(5,11)])
G.add_edges_from([(6,1),(6,7),(6,11),(6,17)])
G.add_edges_from([(7,1),(7,5),(7,6),(7,17)])
G.add_edges_from([(8,1),(8,2),(8,3),(8,4)])
G.add_edges_from([(9,1),(9,3),(9,31),(9,33),(9,34)])
G.add_edges_from([(10,3),(10,34)])
G.add_edges_from([(11,1),(11,5),(11,6)])
G.add_edges_from([(12,1)])
G.add_edges_from([(13,1),(13,4)])
G.add_edges_from([(14,1),(14,2),(14,3),(14,4),(14,34)])
G.add_edges_from([(15,33),(15,34)])
G.add_edges_from([(16,33),(16,34)])
G.add_edges_from([(17,6),(17,7)])
G.add_edges_from([(18,1),(18,2)])
G.add_edges_from([(19,33),(19,34)])
G.add_edges_from([(20,1),(20,2),(20,34)])
G.add_edges_from([(21,33),(21,34)])
G.add_edges_from([(22,1),(22,2)])
G.add_edges_from([(23,33)])
G.add_edges_from([(24,26),(24,28),(24,30),(24,33),(24,34)])
G.add_edges_from([(25,26),(25,28),(25,32)])
G.add_edges_from([(26,24),(26,25),(26,32)])
G.add_edges_from([(27,30),(27,34)])
G.add_edges_from([(28,3),(28,24),(28,25),(28,34)])
G.add_edges_from([(29,3),(29,34),(29,32)])
G.add_edges_from([(30,24),(30,27),(30,33),(30,34)])
G.add_edges_from([(31,2),(31,9),(31,33),(31,34)])
G.add_edges_from([(32,1),(32,25),(32,26),(32,29)])
G.add_edges_from([(33,3),(33,9),(33,15),(33,16),(33,19),(33,21),(33,23),(33,24),(33,30),(33,31),(33,32),(33,34)])
G.add_edges_from([(34,9),(34,10),(34,14),(34,15),(34,16),(34,19),(34,20),(34,21),(34,23),(34,24),(34,27),(34,28),(34,29),(34,30),(34,31),(34,32),(34,33)])

print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))
print(nx.average_clustering(G))
print(nx.connectivity.local_edge_connectivity(G, 1, 34))

options = {
    'node_color': 'black',
    'node_size': 50,
    'width': 1,
}

nx.draw_circular(G, **options)

plt.show()