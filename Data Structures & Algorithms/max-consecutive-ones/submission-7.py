class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = now = 0
        for i in nums:
            if i == 0:
                maxcount = max(maxcount,now)
                now = 0
            else:
                now += 1
        return max(maxcount,now)