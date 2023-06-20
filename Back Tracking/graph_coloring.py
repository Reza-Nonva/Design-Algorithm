def is_valid(G,answer, k, color):
    for neighbor in G[k]:
        if answer[neighbor] == color:
            return False
    return True
 
def graph_coloring(G, m):
    n = len(G)
    colors = [i for i in range(m)]
    answer = [-1 for i in range (n)]
    k = 0
    bt_graph_coloring(G, answer, colors, k)

def bt_graph_coloring(G, answer, colors, k):
    n = len(G)
    if k == n:
        print(answer)
        return
    for color in colors:
        if(is_valid(G, answer,  k, color)):
            answer[k] = color
            bt_graph_coloring(G, answer, colors, k+1)
            answer[k] = -1

#example
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
graph_coloring(G= graph, m=3)