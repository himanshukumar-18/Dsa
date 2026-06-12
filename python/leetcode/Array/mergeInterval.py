#Merge Intervals - [https://leetcode.com/problems/merge-intervals/description/]

#Time complexity - [O(n log n)]
#space complexity - [O(n)]

def merge(intervals):

    intervals.sort()
    merged = []

    for interval in intervals:

        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[1,4],[4,5]]
print(merge(intervals))