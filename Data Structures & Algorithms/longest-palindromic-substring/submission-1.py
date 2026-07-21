class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(substr):
            l, r = 0, len(substr) - 1
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for i in reversed(range(len(s)+1)):
            l, r = 0, i
            while r <= len(s):
                if isPalindrome(s[l:r]):
                    return s[l:r]
                l += 1
                r += 1