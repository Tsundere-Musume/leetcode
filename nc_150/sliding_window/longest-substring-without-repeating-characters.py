#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        result = 0
        l, r  = 0, 0
        while r < len(s):
            c = s[r]
            if c in count and count[c] >= l:
                l = count[c] + 1
            result = max(result, r - l + 1)
            count[c] = r
            r += 1
        return result
