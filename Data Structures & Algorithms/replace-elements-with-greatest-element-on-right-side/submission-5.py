class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        maxnum = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = maxnum
            maxnum = max(maxnum,arr[i])
        return ans