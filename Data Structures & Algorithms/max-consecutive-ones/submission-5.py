class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_count = max(count,max_count)
                count = 0
            else:
                count += 1
        return max(max_count,count)