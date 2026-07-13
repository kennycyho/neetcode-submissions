class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        min_heap = []
        for num, count in frequency.items():
            heapq.heappush(min_heap, (count, num))
            if (len(min_heap)) > k:
                heapq.heappop(min_heap)
        
        res = []
        for pair in min_heap:
            res.append(pair[1])
        return res