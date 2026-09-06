class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1: 
            pop1 = heapq.heappop(stones)
            pop2 = heapq.heappop(stones)
            diff = abs(pop1) - abs(pop2)
            if diff > 0:
                heapq.heappush(stones,-diff)
        if stones:
            return abs(stones[0])
        else:
            return 0