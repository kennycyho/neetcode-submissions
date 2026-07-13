class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def isValid(countW: dict, countT:  dict) -> bool:
            for char, count in countT.items():
                if char not in countW:
                    return False
                if countW[char] < count:
                    return False
            return True

        countT = defaultdict(int)
        for c in t:
            countT[c] += 1
        
        res = ""
        window = []
        countW = defaultdict(int)

        for r in range(len(s)):
            window.append(s[r])
            countW[s[r]] += 1

            while (isValid(countW, countT)):
                if len(res) == 0 or len(window) < len(res):
                    res = "".join(window)
                l = window.pop(0)
                countW[l] -= 1

        return res