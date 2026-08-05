class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = now = 0
        for i in nums:
            if i == 0:
                cnt = max(cnt,now)
                now = 0
            else:
                now += 1
        return max(cnt,now)