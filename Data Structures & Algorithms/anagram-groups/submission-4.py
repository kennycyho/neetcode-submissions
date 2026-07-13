class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {} #freqMap : List[str]

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in anagramMap:
                anagramMap[sortedWord] = []
            anagramMap[sortedWord].append(word)
        return list(anagramMap.values())