class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        i = 0
        while i < len(nums):
            cnt = 0
            while i < len(nums) and nums[i] == 1:
                cnt += 1
                i += 1
            max_cnt = max(max_cnt,cnt)
            i += 1
        return max_cnt
    