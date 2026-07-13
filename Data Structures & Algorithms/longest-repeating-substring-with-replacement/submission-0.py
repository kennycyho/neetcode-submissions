class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            cur_len = r - l + 1
            max_f = max(count.values())
            while cur_len - max_f > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
                cur_len -= 1
                max_f = max(count.values())                
            res = max(res, cur_len)
        return res