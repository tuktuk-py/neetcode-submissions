class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)
        while len(stone) > 1:
            one = heapq.heappop(stone)
            two = heapq.heappop(stone)
            diff = abs(one) - abs(two)
            if diff > 0:
                heapq.heappush(stone,-diff)
        if stone:
            return abs(stone[0])
        else:
            return 0