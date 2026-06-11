# search a 2D matrix - [https://leetcode.com/problems/search-a-2d-matrix/description/]

#Time complexity: O(log(m*n)) where m is the number of rows and n is the number of columns
#Space complexity: O(1)

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    
    left = 0
    right = m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        row = mid // n
        col = mid % n
        
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target =  3
print(searchMatrix(matrix, target))