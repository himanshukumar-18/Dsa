# lengthOfLongestSubstring - [https://leetcode.com/problems/longest-substring-without-repeating-characters/]

# Time complexity - [O(n)]
# Space complexity - [O(n)]

def lengthOfLongestSubstring(s):
    
    charSet = set()
    left = 0
    length = 0
    
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        
        charSet.add(s[right])
        length = max(length, right - left + 1)
    
    return length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))