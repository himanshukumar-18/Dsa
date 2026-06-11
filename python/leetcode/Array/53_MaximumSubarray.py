#maximum sub array -> [https://leetcode.com/problems/maximum-subarray/description/]

#time complexity - [O(n)]
#space complexity - [O(1)]

def maxSubArray(nums):
    currentSum = 0
    maxSum = float('-inf')
    
    for val in nums:
        currentSum = currentSum + val
        maxSum = max(currentSum, maxSum)
        
        if currentSum < 0:
            currentSum = 0
            
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubArray(nums)
print(result)