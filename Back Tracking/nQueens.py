import time
start = time.time()

def nQueens(n):
    answer = [0 for i in range (n+1)]
    exist = [i for i in range(1, n +1)]
    k = 1
    bt_nQueens(answer, exist, n, k)


def bt_nQueens(answer, exist, n, k):
    exist_2 = exist.copy()

    if k == n + 1:
        print (answer)
        return
    #print(exist)
    for i in exist:
        if(bQueens(answer, k, i)):
            answer[k] = i
            exist.remove(i)
            exist_2.remove(i)
            bt_nQueens(answer, exist_2, n, k+1)
            exist_2.append(i)
def bQueens(answer, k, i):
    for j in range(1, k):
        
        if(answer[j] == i or k - i == j - answer[j] or
           k + i == j + answer[j] ):
            return False
    return True




n = int(input())
nQueens(n)


stop = time.time()
print(stop - start)






