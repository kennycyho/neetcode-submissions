class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list) #freqMap : List[str]

        for word in strs:
            charFreq = [0] * 26
            for c in word:
                charFreq[ord(c) - ord('a')] += 1
            anagramMap[tuple(charFreq)].append(word)
        return list(anagramMap.values())