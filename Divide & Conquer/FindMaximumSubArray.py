
# find maximum subarray using divide and conquer algorithm
#time copmlexity: O(n * log n)
def maxCrossingSum(arr, low, mid, high):
	
    sum = 0
    left_sum = float('-inf')

    for i in range(mid, low-1, -1):
        sum = sum + arr[i]
	
        if (sum > left_sum):
            left_sum = sum

    sum = 0
    right_sum = float('-inf')
    for i in range(mid, high + 1):
        sum = sum + arr[i]
	
        if (sum > right_sum):
            right_sum = sum
            
    return max(left_sum + right_sum - arr[mid], left_sum, right_sum)

def maxSubArraySum(arr, low, high):
    if (low > high):
        return -10000
    if (low == high):
        return arr[low]
    
    mid = (low + high) // 2
    return max(maxSubArraySum(arr, low, mid-1),
			maxSubArraySum(arr, mid+1, high),
			maxCrossingSum(arr, low, mid, high))


#example 
arr = [-2, 1, -3, 4, -1, 2, 1, 5, 4]
n = len(arr)


print(maxSubArraySum(arr, 0, n-1))

