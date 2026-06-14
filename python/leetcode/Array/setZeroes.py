# setZeroes - [https://leetcode.com/problems/set-matrix-zeroes/]

# ⏱ Complexity
# Time: O(m × n)
# Space: O(1)

def setZeroes(matrix):
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # Step 1: check first row
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        # Step 2: check first column
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        # Step 3: mark rows & cols
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: fill matrix based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: update first row
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 6: update first column
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
                
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)