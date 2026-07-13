class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxS = max(maxS, len(window))
        return maxS