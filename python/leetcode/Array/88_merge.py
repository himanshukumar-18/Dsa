#Merge to array without extra space -> https://leetcode.com/problems/merge-sorted-array/

# Time Complexity: O(m+n)
# Space Complexity: O(1)

def merge(nums1, m, nums2, n):
    idx = m + n - 1
    i = m - 1
    j = n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1
        idx -= 1
    
    while j >= 0:
        nums1[idx] = nums2[j]
        j -= 1
        idx -= 1

arr_1 = [1, 2, 3, 0, 0, 0]
m = 3

arr_2 = [2, 5, 6]
n = 3

merge(arr_1, m, arr_2, n)
print(arr_1)