class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we only care if the number has been seen or not so use set()
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False