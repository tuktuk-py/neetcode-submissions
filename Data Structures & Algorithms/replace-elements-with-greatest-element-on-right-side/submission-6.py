class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        prefix = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = prefix
            prefix = max(prefix,arr[i])
        return ans