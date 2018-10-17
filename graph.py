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

color_map_nodes=[]
color_map_edges=[]

for node in G:
    if node==1 or node==2 or node==4 or node==5 or node==6 or node==7 or node==8 or node==11 or node==12 or node==13 or  node==18 or  node==22:
        color_map_nodes.append('red')
    elif node==9 or node==14 or node==20 or node==32:
        color_map_nodes.append('green')
    elif node==34 or  node==10 or node==15 or node==16 or node==19 or node==21 or node==23 or node==24 or node==27 or node==28 or node==29 or node==30 or node==31 or node==33:
        color_map_nodes.append('blue')
    else:
        color_map_nodes.append('black')

for edge in G.edges:
    if edge[0]==1 or edge[1]==1:
        color_map_edges.append('red')
    elif (edge[0]==9 or edge[1]==9 or edge[0]==14 or edge[1]==14 or edge[0]==20 or edge[1]==20 or edge[0]==32 or edge[1]==32) and edge[0]!=1 and edge[0]!=34 and edge[1]!=1 and edge[1]!=34:
        color_map_edges.append('green')
    elif edge[0]==34 or edge[1]==34:
        color_map_edges.append('blue')
    else:
        color_map_edges.append('black')

options = {
    'font_size': 12,
    'font_color': 'white',
    'node_size': 200,
    'width': 2,
}

nx.draw_spring(G, node_color=color_map_nodes, edge_color=color_map_edges, with_labels=True, **options)

plt.show()