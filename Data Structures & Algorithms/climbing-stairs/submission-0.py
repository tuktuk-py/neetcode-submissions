class Solution:
    def climbStairs(self, n: int) -> int:
        def dsf(i):
            if i >= n:
                return i==n
            return dsf(i+1)+dsf(i+2)
        return dsf(0)