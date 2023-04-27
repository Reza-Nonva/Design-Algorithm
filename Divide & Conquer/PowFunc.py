# Implementation of power function using Divide and Conquer algorithm

def pow(x, n):   # x^n
    if( n == 0):
        return 1
    if ( x == 0):
        return 0
    
    result = pow(x, n//2)

    if( x % 2 == 0):
        return result * result
    
    else:
        return result*result*x


#example:

print(pow(3, 7))
