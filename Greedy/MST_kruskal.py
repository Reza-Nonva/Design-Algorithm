from typing import List, Tuple

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

    print(kruskal(num_nodes, edges)) #print the tree

    print(len(kruskal(num_nodes, edges)))  # print the depth of tree




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