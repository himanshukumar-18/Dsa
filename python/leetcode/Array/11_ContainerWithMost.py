#Container with most water - [https://leetcode.com/problems/container-with-most-water/description/]

# time complexity - [O(n)]
# space complexity - [O(1)]

def maxArea(height):
    maxWater = 0
    lp = 0
    rp= len(height) - 1

    while lp < rp:
        w = rp - lp
        h = min(height[lp], height[rp])
        currWater = w * h
        maxWater = max(maxWater, currWater)

        if height[lp] < height[rp]:
            lp = lp + 1
        else:
            rp = rp - 1

    return maxWater

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))