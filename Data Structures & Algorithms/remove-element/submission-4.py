class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace = 0
        for i in nums:
            if i != val:
                nums[replace] = i
                replace += 1
        return replace