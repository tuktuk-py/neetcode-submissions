class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]
        return output

