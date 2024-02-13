"""  
Rachael Savage
CSC382: Data Structure & Algorithm
Dr. Jill Coddington
2/7/2024

"""

""" *********************Overview of the graph *************************
- This project using  the networkX lib package to demonstrate  graph algorithms on a custom graph with weighted edges.
- Part I: Create the graph
- Part II: using Dijkstra's algorithm to find the shortest path between 2 specific nodes (cities)
- Part III: Using Prim's algorithm to generate a mimi spanning tree (MST) of the graph. The MST is used for finding the most efficient way to connect all nodes in a graph at the lowest cost
- Part VI: Using Breadth-First Search (BFS) to explore all the nodes reachable from the starting point city (VB) & connect all the paths that BFS traverse first
- Part V: DFS to explore the depth search, exploring all nodes.
- Part VI: Bellman-Ford works for graphs with both pos and neg weights

"""


# -----------------------------------------------------------------------PART I: setup the graph---------------------------


import networkx as nx #
import matplotlib.pyplot as plt

# create a new graph object
graph = nx.Graph()

# create edges between cities and distances as weights using tupples data type to store each edge (random made up cities and distance/weight)
edges = [
    # Format: ("Node1", "Node2", Weight)
    ("Virginia Beach", "Washington DC", 198),
    ("Virginia Beach", "Houston", 675),
    ("Washington DC", "New York", 225),
    ("New York", "Boston", 210),
    ("Boston", "Detroit", 613),
    ("Detroit", "Chicago", 283),
    ("Chicago", "Kansas City", 510),
    ("Kansas City", "Denver", 557),
    ("Denver", "Salt Lake City", 371),
    ("Salt Lake City", "Las Vegas", 421),
    ("Las Vegas", "Los Angeles", 272),
    ("Los Angeles", "San Francisco", 383),
    ("San Francisco", "Portland", 635),
    ("Portland", "Seattle", 174),
    ("Seattle", "Boise", 504),
    ("Boise", "Salt Lake City", 340),
    ("Denver", "Phoenix", 586),
    ("Phoenix", "Houston", 1175),
    ("Houston", "Dallas", 239),
    ("Dallas", "Atlanta", 721),
    ("Atlanta", "Denver", 600),
    ("Virginia Beach", "Portland", 205),
    ("Virginia", "Seatle", 391),
    ("Washinton DC", "Houston", 140),
    ("Houston", "Seatle", 174),
    ("Seatle", "Houston", 495),
    ("Seatle", "Phoenix", 890),
    ("Atlanta", "Kansas", 321),
    ("Dallas", "Boston", 100),
]


# add all the edges to the graph to make it as a flying map/path
graph.add_weighted_edges_from(edges, weight='distance')


# -------------------------------------------------------------PART II: Finding the shortest path using Dijkstra----------------------------------------
""" 
Dijkstra's algorithm finds the shortest path from non-negative edge weights graph
"""
# decllare start and end cities
start_city = "Virginia Beach"
end_city = "Denver"

# using Dijkstra's algorithm to find the shortest route between 2 cities
shortest_path = nx.dijkstra_path(
    graph, source=start_city, target=end_city, weight='distance')

# print the shortest route
print(
    f"Shortest rout from{start_city} to {end_city}: {' -> ' .join(shortest_path)}")

# ------------------------------------------------------------PART III: Prim's algorithm-minimum spanning tree-----------------------------------------
""" 
Prim's algorithm generates a minimum spanning tree (MST) for a weighted undirected graph.
It make sure the tree includes all nodes while minimizing the total edge weight
"""
# using prim's algorithm to find the minimum spanning tree of the gragh
# mst short for minimum spanning tree
# creating an object using networkX library
mst = nx.minimum_spanning_tree(graph, weight='distance')

# print the egdes in the MST
print("Edges in the MST: ")
for edge in mst.edges(data=True):
    print(edge)


# ------------------------------------------------------------------ PART IV: Breadth-First Search to explore the graph-------------------------------------
""" 
Breadth-First Search (BFS) explores the graph level by level from a start node. (It likely best to use with unweighted graph)
"""


# Perform BFS traversal from the start node & returns a list of nodes discovered during BFS
bfs_tree = nx.bfs_tree(graph, source=start_city)



#---------------------------------------------------PART V: Depth-First Search (DFS) to explore the graph-----------------------------------------------------
""" 
DFS algorithm explores the tree as far as possible along each branch before backtrack
It's primary used to search all the nodes in  graph
DFS explore deep into one path fully before exploring another, while BFS visit all nearby nodes first.
It's particularly useful for scenarios that need to explore all possible solutions and for problems where you need to visit every node in the graph. 
DFS can be implemented using recursion or a stack, and it's efficient for traversing large graphs. 
It can be used to solve puzzles, navigate mazes, check connectivity, and find connected components in a graph.
"""


#perform DFS traversal from the start node and return the DFS tree
dfs_tree = nx.dfs_tree(graph, source=start_city)


#-------------------------------------------------PART VI: Bellman-Ford to find shortest path-------------------------------------------------------------------
""" 
This algorithm may be slower then Dijkstra to find the shortest path, however, it can handle both neg weights
"""
# Using Bellman-Ford's algorithm to find the shortest route
shortest_path_bf = nx.bellman_ford_path(graph, source=start_city, target=end_city, weight='distance')
#get the length
path_length_bf = nx.bellman_ford_path_length(graph, source=start_city, target=end_city, weight='distance' )
#print the shortest path and its length
print(f"Shortest path from {start_city} to {end_city} using Bellman-Ford: {' -> '.join(shortest_path_bf)}")
print(f"Total distance: {path_length_bf}")



#*********************************************************************Ploting**************************************************************************
#******************************************************************************************************************************************************

# uisng math plotlib for visualization
position = nx.spring_layout(graph)  # for a consistent display

# drawing the original graph using subtle color

plt.figure(figsize=(12, 8))
nx.draw(graph, position, with_labels=True, edge_color='gray',
        node_color='blue', alpha=0.5, font_weight='bold')
edge_labels = dict([((u, v,), d['distance'])
                   for u, v, d in graph.edges(data=True)])
nx.draw_networkx_edge_labels(graph, position, edge_labels=edge_labels)

plt.figtext(0.5, 0.01, 'Original Fly Network of Cities', ha='center', fontsize=20, color='red', fontweight='bold')


plt.show()


# Visualize the shortest path found by Dijkstra's algorithm
plt.figure(figsize=(12, 8))
# Draw the entire graph with a subtle color first
nx.draw(graph, position, with_labels=True, edge_color='lightgray',
        node_color='lightblue', alpha=0.6, font_weight='bold')
# Highlight the nodes in the shortest path
nx.draw_networkx_nodes(graph, position, nodelist=shortest_path,
                       node_color='red', node_size=900)
# Highlight the edges in the shortest path
path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
nx.draw_networkx_edges(graph, position, edgelist=path_edges,
                       edge_color='red', width=5)
# Draw edge labels to show distances
shortest_path_edge_labels = {(u, v): d for u, v, d in graph.edges(
    data='distance') if (u, v) in path_edges or (v, u) in path_edges}
nx.draw_networkx_edge_labels(
    graph, position, edge_labels=shortest_path_edge_labels)
plt.figtext(0.5, 0.01, 'Dijkstra: Shortest path', ha='center', fontsize=20, color='red', fontweight='bold')

plt.show()


# Visualize the MST generated by Prim's algorithm
plt.figure(figsize=(12, 8))
# Draw the MST with distinct colors
nx.draw(mst, position, with_labels=True,
        node_color='orange', edge_color='green', width=7)
#  create edge labels to show distances in the MST
mst_edge_labels = nx.get_edge_attributes(mst, 'distance')
nx.draw_networkx_edge_labels(mst, position, edge_labels=mst_edge_labels)

plt.figtext(0.5, 0.01, 'Minimum Spanning Tree: Prim algorithm ', ha='center', fontsize=20, color='red', fontweight='bold')
plt.show()


# Visualize the BFS traversal
plt.figure(figsize=(12, 8))
nx.draw(graph, position, with_labels=True, edge_color='lightgray',
        node_color='lightblue', alpha=0.5, font_weight='bold')
# Highlight the BFS tree
nx.draw_networkx_edges(bfs_tree, position, edge_color='purple', width=2)
nx.draw_networkx_nodes(bfs_tree, position, node_color='yellow', node_size=500)

# Highlight the start node
nx.draw_networkx_nodes(graph, position, nodelist=[
                       start_city], node_color='red', node_size=700)

plt.figtext(0.5, 0.01, 'Breadth First Search', ha='center', fontsize=20, color='red', fontweight='bold')

plt.show()



#visual for DFS traversal
plt.figure(figsize=(12, 8)) 
nx.draw(graph, position, with_labels=True, edge_color='lightgray', node_color='lightblue', alpha=0.7, font_weight='bold')
# highlight the DFS edges
nx.draw_networkx_edges(dfs_tree, position, edge_color='blue', width=5)
#highlight the DFS nodes
nx.draw_networkx_nodes(dfs_tree, position, node_color='lime', node_size=700)
#highlight the start nodes
nx.draw_networkx_nodes(graph, position, nodelist=[start_city], node_color='deeppink', node_size=800)

plt.figtext(0.5, 0.01, 'Depth First Search', ha='center', fontsize=20, color='red', fontweight='bold')

plt.show()



#Visual for Bellman Ford
plt.figure(figsize=(12,8))
#subtile colors for the whole graph
nx.draw(graph, position, with_labels=True, node_color='lightblue', edge_color='gray', alpha=0.5)
#highlight the shortest path
path_edges = list(zip(shortest_path_bf, shortest_path_bf[1:]))
nx.draw_networkx_nodes(graph, position, nodelist=shortest_path_bf, node_color='brown')
nx.draw_networkx_edges(graph, position, edgelist=path_edges, edge_color='red', width=5)

plt.figtext(0.5, 0.01, 'Bellman Ford: Shortest path', ha='center', fontsize=20, color='red', fontweight='bold')

plt.show()


""" -------------------------------SUMMARY----------------------
1.Dijkstra's Algorithm: Efficiently finds the shortest path between two nodes in graphs with non-negative weights.
2.Prim's Algorithm: Generates a Minimum Spanning Tree (MST) for a connected, undirected graph with weighted edges.
3.Breadth-First Search (BFS): Explores the graph level by level from a start node.
4.Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
5.Bellman-Ford Algorithm: Unlike Dijkstra's, Bellman-Ford can handle graphs with negative weights and detects negative cycles.

---------------------------------COMPARISONS-----------------------------
- Dijkstra's is generally faster for weighted graphs without negative weights.
-Prim's is for connecting all nodes minimally (not find path).
-BFS offers the simplest form of traversal to give a broad overview of the graph's structure.
-DFS provides deep exploration, beneficial for analyzing complex/layered networks.
-Bellman-Ford offers a robust solution for complex graphs, include negative weights, with the cost of higher computational time.
"""










""" References
https://www.youtube.com/watch?v=VetBkjcm9Go
https://stackoverflow.com/questions/25416232/bellman-ford-negative-weight-networkx
https://github.com/topics/bellman-ford-algorithm?l=python&o=desc&s=forks
https://github.com/topics/bellman-ford-algorithm?l=python&o=desc&s=forks
https://github.com/MUSoC/Visualization-of-popular-algorithms-in-Python/blob/master/BellmanFord/BellmanFord.py
https://github.com/topics/bellman-ford-algorithm?l=python&o=desc&s=forks
https://reintech.io/blog/python-and-bellman-ford-algorithm-a-comprehensive-guide

"""