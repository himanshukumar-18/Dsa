# find second largest
# input: nums[10, 45, 2, 78, 34]
# output: 45

def findSecondLargest(nums):
    largest = float('-inf')
    secondLargest = float('-inf')

    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif largest > num > secondLargest:
            secondLargest = num

    return secondLargest

nums = [10, 45, 2, 78, 34]
print(findSecondLargest(nums))