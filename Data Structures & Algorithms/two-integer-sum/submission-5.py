class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in index:
                return [index[need],i]
            else:
                index[nums[i]] = i 