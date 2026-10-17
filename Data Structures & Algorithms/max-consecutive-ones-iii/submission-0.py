class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        given k counts that represents how many times we can flip a zero to one
        k is the constraint for this window
        getting the size of the window is like this with two pointers
        r-l+1
        keep on track of max window size 
        """
        l = 0
        max_window = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            window = r - l + 1
            max_window = max(window,max_window)
        return max_window
        