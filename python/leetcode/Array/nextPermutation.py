# nextPermutation - [https://leetcode.com/problems/next-permutation/]
# time complexity -[O(n)]
# space complexity - [O(1)]

def nextPermutation(nums):
    
    n = len(nums)
    
    # find break down
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # swap greater
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # rev els
    nums[i + 1:] = reversed(nums[i + 1:])

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)