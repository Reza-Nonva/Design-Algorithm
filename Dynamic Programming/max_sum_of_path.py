def max_sum_of_path(numbers):
    depth = len(numbers) - 1
    
    for l in range(depth-1 , -1, -1):
        for i in range(l+1):
            if (numbers[l][i] + numbers[l+1][i] > numbers[l][i] + numbers[l+1][i+1]):
                numbers[l][i] += numbers[l+1][i]
            else:
                numbers[l][i] += numbers[l+1][i+1]
    
    print_path(numbers)


def print_path(numbers):
    depth = len(numbers)

    for l in range (1, depth):
        print(max(numbers[l-1]) - max(numbers[l]))
    
    print(max(numbers[depth -1]))


# read 
x = int(input())
numbers = [[]for _ in range(x)]

for i in range(x):
    gham = input().split()

    for number in gham:
        numbers[i].append(int(number))

max_sum_of_path(numbers)