class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        maxL = 0
        l = 0

        for r in range(len(s)):
            ch = s[r]
            freq[ord(ch) - ord("A")] += 1
            while r-l+1 - max(freq) > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
            maxL = max(r - l + 1, maxL)

        return maxL