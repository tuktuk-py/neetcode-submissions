class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,a in enumerate(nums):
            need = target - a
            if need in seen:
                return [seen[need],i]
            else:
                seen[a] = i
         
