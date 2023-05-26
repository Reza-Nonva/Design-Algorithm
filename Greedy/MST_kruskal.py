import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Tuple

def draw(edges):
    G = nx.Graph()
    for i in edges:
        G.add_edge(i[0], i[1], weight = i[2])

    edge = [(u, v) for (u, v, d) in G.edges(data=True)]

    pos = nx.spring_layout(G, seed=7)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=edge, width=6)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def read_grph_by_adjacency_matrix(num_nodes, edges):
    for i in range(num_nodes):
        read_line = input().split()
        row_i = [int(x) for x in read_line]
        for j in range(i):
            if row_i[j] != 0:
                edges.append((i, j, row_i[j]))

def read_by_edges(edges):
    # if you want to input graph with (source, distance, weight) structures use these function
    # in main func instead of read_grph_by_adjacency_matrix
    num_edges = int(input())
    for _ in range(num_edges): 
        node1, node2, cost = [int(x) for x in input().strip().split()]
        edges.append((node1, node2, cost))
        


def kruskal(num_nodes: int, edges: List[Tuple[int, int, int]]) -> int:
    
    edges = sorted(edges, key=lambda edge: edge[2])

    parent = list(range(num_nodes))

    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []

    for edge in edges:
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            minimum_spanning_tree.append(edge)
            parent[parent_a] = parent_b

    return minimum_spanning_tree


if __name__ == "__main__":
    num_nodes = int(input())
    edges = []
    read_grph_by_adjacency_matrix(num_nodes, edges)

    answer = kruskal(num_nodes, edges)

    print(answer) #print the tree
    print(len(answer))  # print the depth of tree
    
    draw(answer)

"""
    example for read graph by edges: 

    >>> kruskal(4, 3, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
    [(2, 3, 1), (0, 1, 3), (1, 2, 5)]

    >>> kruskal(4, 5, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
    [(2, 3, 1), (0, 2, 1), (0, 1, 3)]

    >>> kruskal(4, 6, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
    ... (2, 1, 1)])
    [(2, 3, 1), (0, 2, 1), (2, 1, 1)]


    example for read graph by adjacency matrix:
    >>> 4  
        0 1 4 2
        1 0 0 2
        4 0 0 3
        2 2 3 0
        [(1, 0, 1), (3, 0, 2), (3, 2, 3)]
"""