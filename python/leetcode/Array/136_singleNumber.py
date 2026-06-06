#Single Number -> https://leetcode.com/problems/single-number/

# Time Complexity: O(n)
# Space Complexity: O(1)

def singleNumber(nums):
   ans = 0
   
   for val in nums:
       ans = ans ^ val
           
   return ans

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))