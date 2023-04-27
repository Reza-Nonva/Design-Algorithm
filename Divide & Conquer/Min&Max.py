# Implementation of Min and Max function find minimun and maximum numbers in array using Divide and Conquer algorithm
#time complexity: O(n*log n)

def M_M(list):
    if(len(list) <= 3):

        answer = [list[0], list[0]]         #[Min, Max]

        for i in range(len(list)):
            if(list[i] < answer[0]):
                answer[0] = list[i]
            
            if (list[i] > answer[1]):
                answer[1] = list[i]
        return answer

    mid = len(list) // 2

    L_answer = M_M(list[:mid])
    R_answer = M_M(list[mid:])
    
    answer = R_answer

    if(L_answer[0]  < R_answer[0]):
        answer[0] = L_answer[0]
    
    if(L_answer[1] > R_answer[1]):
        answer[1] = L_answer[1]
    
    return answer

#exmaple

list = [7, 2, -9, 3, 1, 36, 7, 81, -4]

print(M_M(list))