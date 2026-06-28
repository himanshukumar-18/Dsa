# subarraySum - [https://leetcode.com/problems/subarray-sum-equals-k/]

#TC - [O(n)]
#SC - [O(1)]

def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    hasmap = {0:1}
    
    for num in nums:
        prefix_sum += num
        
        if (prefix_sum - k) in hasmap:
            count += hasmap[prefix_sum -  k]
            
        hasmap[prefix_sum] = hasmap.get(prefix_sum, 0) + 1
    
    return count

nums = [1,1,1]
k = 2
print(subarraySum(nums, k))