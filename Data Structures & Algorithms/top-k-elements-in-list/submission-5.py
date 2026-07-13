class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        
        minheap = []
        for key, v in freqMap.items():
            heapq.heappush(minheap, (v, key))
            while len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for count, num in minheap:
            res.append(num)
        return res