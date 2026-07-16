
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap) == 0:
            self.minheap.append(num)
        
        elif self.findMedian() < num:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        #balance heaps 
        while abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                element = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -element)
            else:
                element = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, element)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2