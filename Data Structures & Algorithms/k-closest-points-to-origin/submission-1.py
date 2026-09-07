class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        for x,y in points:
            diff = (x ** 2) + (y ** 2)
            output.append([diff,x,y])
        heapq.heapify(output)
        res = []
        for i in range(k):
            diff,x,y = heapq.heappop(output)
            res.append([x,y])
        return res