class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # need to iterate twice
        # have the inner loop to go through every int in the list
        for i in range(2):
            for n in range(len(nums)):
                ans.append(nums[n])
        return ans
