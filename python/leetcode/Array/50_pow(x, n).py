# Pow(x, n) -> [https://leetcode.com/problems/powx-n/description/]

def myPow(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    
    while n > 0:
        if n % 2 == 1:
            result = result * x
        
        x = x * x
        n = n // 2
    
    return result

output = myPow(2.0000, 10)
print(output)