class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        l = 0
        for r, c in enumerate(s2):
            s2_count[c] = s2_count.get(c, 0) + 1
            if (r - l + 1 > len(s1)):
                s2_count[s2[l]] = s2_count[s2[l]] - 1
                if s2_count[s2[l]] == 0:
                    s2_count.pop(s2[l])
                l += 1
            if s1_count == s2_count:
                return True
        return False