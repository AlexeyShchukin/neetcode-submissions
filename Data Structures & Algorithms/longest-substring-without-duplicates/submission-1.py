class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        hashmap = {}
        for right, c in enumerate(s):
            if c in hashmap:
                left = max(hashmap[c] + 1, left)
            hashmap[c] = right
            res = max(res, right - left + 1)
        return res
            
                