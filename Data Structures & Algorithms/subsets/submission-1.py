class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        res = []
        def backtrack(i):
            if i >= len(nums):
                output.append(res.copy())
                return
            res.append(nums[i])
            backtrack(i+1)
            res.pop()
            backtrack(i+1)
        backtrack(0)
        return output
            