# remove duplication numbers of array with using Recursion algorithm
# time complexcity:  (n*log n) + d

k = 0
ind = -1 # to save the first index of duplicated element
first = True

def  delete(answer, arr, index, d):
    global k
    global ind
    global first
    if(index == 0): # base case
        answer[k] = arr[0]
        k +=1
        return 
    
    delete(answer, arr, index -1, d) #recursion

    if(arr[index] == arr[index -1] and first == True): #find the first+1 index of duplicated element
        first = False
        ind = index

    if(index <= ind-2 +d and first == False): 
        return
    
    answer[k] = arr[index]
    k+=1
    

        
        

def remove_duplicates_recursion(arr, d): # d variable save times of duplicated number
    arr.sort()
    answer = [0 for i in range(len(arr))]

    delete(answer, arr, len(arr) - 1, d) 

    return answer

#example: 
arr = [1, 2, 9, 2, 2, 2, 8, 2, 3, 7, 2, 6, 4, 5, 2]
arr = remove_duplicates_recursion(arr, 7)
print (arr)