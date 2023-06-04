def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for i in range (n+1)] for i in range(n+1)]
    s = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        m[i][i] = 0
    
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + (p[i-1] * p[k] * p[j])
                if q<m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    #print("m: ", m)
    #print ("s: ", s)
    print_optimal_parens(s, 1, n)





def print_optimal_parens(s, i, j):
    if i == j:  
        print("A{}".format(i), end="")
    else:
        print("(" ,end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")






n = int(input())
p = []
first = input().split()
p.append(int(first[0]))
p.append(int(first[1]))
for _ in range(n-1):
    x = input().split()
    p.append(int(x[1]))

    
matrix_chain_order(p)
