class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = now = 0
        for i in nums:
            if i == 0:
                max_cnt = max(now,max_cnt)
                now = 0
            else:
                now += 1
        return max(now,max_cnt)