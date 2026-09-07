class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = []
        for i in range(len(nums)):
            heapq.heappush(num,nums[i])
            while len(num) > k:
                heapq.heappop(num)
        return num[0]
        