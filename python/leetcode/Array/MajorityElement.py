#majorityElement -> https://leetcode.com/problems/majority-element/

#Time Complexity: O(n)
#Space Complexity: O(1)

def majorityEl(nums):
    freq = 0
    ans = 0
    
    for i in range(len(nums)):
        if freq == 0:
            ans = nums[i]
        
        if ans == nums[i]:
            freq = freq + 1
        else:
            freq = freq - 1
            
    return ans

nums = [3, 2, 3]
result = majorityEl(nums)
print(result)