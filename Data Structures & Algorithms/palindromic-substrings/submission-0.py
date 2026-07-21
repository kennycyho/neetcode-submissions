class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)

        for i in range(len(s)): 
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l -= 1
                r += 1
        
        return count