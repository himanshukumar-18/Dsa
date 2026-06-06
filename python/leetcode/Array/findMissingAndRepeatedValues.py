#Find Missing And Repeated Values -> https://leetcode.com/problems/find-missing-and-repeated-values/

#Time Complexity: O(n)
#Space Complexity: O(1)

def findMissingAndRepeatedValues(grid):
    # find total length
    n = len(grid)
    
    # square store
    N = n * n
    
    # find sum and square
    sum_actual = 0
    sqr_actual = 0
    
    for row in grid:
        for val in row:
            sum_actual += val
            sqr_actual += val * val
    
    # expected value
    S = N * (N + 1) // 2
    Sqr = N * (N + 1) * (2 * N + 1) // 6
    
    #equation
    sum_diff = sum_actual - S
    sqr_diff = sqr_actual - Sqr
    
    # x + y
    sum_xy = sqr_diff // sum_diff
    
    #find x and y
    x = (sum_diff + sum_xy) // 2
    y = x - sum_diff
    
    return [x, y]

grid = [[1, 3],[2, 2]]
result = findMissingAndRepeatedValues(grid)
print(result)