class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l = r = 0
        while r < len(s) and l < len(s):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            res = max(res, len(seen))
            r += 1
        return res