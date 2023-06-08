def bellman_ford(G, source):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[source] = 0
    
    for i in range(n-1):
        for u in range (n):
            for v in range(n):
                if distance[u] != float("inf"):
                    if (distance[u] + G[u][v] < distance[v]):
                        distance[v] = distance[u] + G[u][v]
    #Check graph
    for u in range (n):
        for v in range(n):
            if(distance[u] != float("inf")):
                if(distance[u] + G[u][v] < distance[v]):
                    print("graph with negative cycle")
    print(distance)


# Read adjacency matrix
x = int(input())
G = [[0 for _ in range(x)] for _ in range(x)]
for i in range(x):
    y = input().split()
    for j in range (x):
        if y[j] == "-":
            G[i][j] = float("inf")
        else:
            G[i][j] = int(y[j])
bellman_ford(G, 0)