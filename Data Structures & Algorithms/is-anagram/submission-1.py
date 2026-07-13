class Solution:
    def getFreqMap(self, s) -> dict:
        freq_map = {}
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1
        return freq_map

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getFreqMap(s) == self.getFreqMap(t)