#3 sum - [https://leetcode.com/problems/3sum/description/]
#time complexity: O(n^2)
#space complexity: O(n)

def threeSum(nums):
    nums.sort()
    result = []

    n = len(nums)

    for i in range(n):
        #skip dublicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        #first position
        left = i + 1
        #last position
        right = n - 1

        while left < right:
            #cal sum
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left +=1
            else:
                right -= 1
                
        return result

nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(result)