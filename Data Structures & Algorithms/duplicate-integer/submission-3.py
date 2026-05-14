class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums is set of integer array, i have to have two pointer (outer loop that stays at the first integer and become the index point) (inner loop that goes through the inegers in the array to check duplication with outer loop) if inner loop integer is the same as outer loop integer return True
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False