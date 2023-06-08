def floyd(G, path):
    n = len(G)

    for i in range(n):
        for k in range(n):
            for j in range(n):
                if(G[i][k] + G[k][j] < G[i][j]):
                    G[i][j] = G[i][k] + G[k][j]
                    path[i][j] = k



def print_path(path, i, j):
    if(path[i][j] == -1):
        return
    print_path(path, i, path[i][j])
    print(path[i][j],"=>", end = "")
    print_path(path, path[i][j], j)


def print_all(path):
    n = len(path)
    for i in range(n):
        for j in range(n):
            print(i,"to",j)
            print(i,"=>", end = "")
            print_path(path, i, j)
            print(j)





# Read adjacency matrix and run floyd algorithm
x = int(input())
G = [[0 for _ in range(x)] for _ in range(x)]
path = [[-1 for i in range(x)] for i in range(x)]
for i in range(x):
    y = input().split()
    for j in range (x):
        if y[j] == "-":
            G[i][j] = float("inf")
        else:
            G[i][j] = int(y[j])

#print ("enter source and distance vertex number: i j")
#x = input().split()

floyd(G, path)
print_all(path)