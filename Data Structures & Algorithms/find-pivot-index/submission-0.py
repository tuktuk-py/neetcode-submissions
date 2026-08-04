class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix += nums[i]
        postfix = 0
        output2 = [0] * len(nums)
        for j in range(len(nums)-1,-1,-1):
            output2[j] = postfix
            postfix += nums[j]
        # print(output)
        # print(output2)
        for i in range(len(output)):
            if output[i] == output2[i]:
                return i
        return -1 