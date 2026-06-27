# setZeroes - [https://leetcode.com/problems/set-matrix-zeroes/]

# ⏱ Complexity
# Time: O(m × n)
# Space: O(1)

def setZeroes(matrix):
    m = len(matrix) # col
    n = len(matrix[0]) # row
    
    firstRowZero = False
    firstColZero = False
    
    for j in range(n):
        if matrix[0][j] == 0:
            firstRowZero = True
    
    for i in range(m):
        if matrix[i][0] == 0:
            firstColZero = True
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if firstRowZero:
        for j in range(n):
            matrix[0][j] = 0
    
    if firstColZero:
        for i in range(m):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)