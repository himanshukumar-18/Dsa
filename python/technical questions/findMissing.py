# find missing number in array
# input: arr = [1, 2, 3, 5] n = 5
# output: 4

def findMissing(arr, n):
    total = int((n * (n + 1) / 2))
    sum = 0
    
    for nums in arr:
        sum += nums
    
    return total - sum

print(findMissing([1, 2, 3, 5], 5))